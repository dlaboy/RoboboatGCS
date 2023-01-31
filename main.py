from flask import Flask
import json
from flask import render_template, jsonify, request

import zmq
from time import sleep

# to send messages to boat
contextA = zmq.Context()
socketA = contextA.socket(zmq.PUB)
socketA.connect("tcp://localhost:%s" % "8090")

def killMessage():
    socketA.send_string("Kill Switch Pressed")

def autoON():
    socketA.send_string("Autonomous Mode ON")

def autoOFF():
    socketA.send_string("Autonomous Mode OFF")

app = Flask(__name__)

@app.route('/data_json')
def data_json():
    # to receive messages from boat 
    contextB = zmq.Context()
    socketB = contextB.socket(zmq.SUB)
    # accept all topics (prefixed) - default is none
    socketB.setsockopt_string(zmq.SUBSCRIBE, "")
    socketB.connect("tcp://localhost:%s" % "8091")


    message = socketB.recv_string()
    
    dummy_data = [{
        "id":1,
        "location": str(message),
        "distance": "125",
        "battery_status": "99",
        "thrusters_speed":"75% (LOW)",
        "thrusters_status":"Not Working",

    },
    {
        "task1":1,
        "name1":"Navigate the Panama Canal",

    },
    {
        "task2":2,
        "name2":"Magellan's Route/ Count the Manatees and Jellyfish",
        "manatees":3,
        "jellyfish":4,
        
    }
    ]
    return jsonify(dummy_data)



@app.route("/killSwitch")
def killSwitch():
    dummy_data = data_json()


    

    n = 0

    while True:

        n+=1

        killMessage()
        print("message sent")
      
        sleep(2)

        if(n == 1):
            break



    status=""
    task=""

  
    return render_template('index.html', status = status, task = task, data=dummy_data.json)

@app.route("/autonomous_mode", methods = ["POST","GET"])
def autonomous_mode():
    dummy_data = data_json()


    salida = request.form.to_dict()

    print(salida)

    if(len(salida) == 0):
        task = 0
        print(task)
        status = "OFF"
        print(status)

    else:
        task = salida["task"]
        status = salida["status"]

  


    n = 0




    while True:
        n+=1

        # if autonomous mode was on
        if(status == "OFF"):
            autoOFF()
            print("message sent")
      
            sleep(2)


            if(n == 1):
                break
        else:
            # if autonomous mode was off
            autoON()
            socketA.send_string("Task to complete: Task #"+task)
            print("message sent")
      
            sleep(2)



            if(n == 1):
                break

    return render_template('index.html', status = status, task = task, data=dummy_data.json),task
    

@app.route('/')
def index():
    
    dummy_data = data_json()

    status=""
    task=""

  
    return render_template('index.html', status = status, task = task, data=dummy_data.json)
        

if __name__=='__main__':
    app.run(debug=True)
