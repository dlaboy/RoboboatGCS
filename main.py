from flask import Flask
import json
from flask import render_template, jsonify, request

import zmq
import keyboard
from time import sleep

# from pub import message
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://127.0.0.1:8090")

autoIndicator = False

def killMessage():
    socket.send_string("Kill Switch Pressed")

def autoON():
    socket.send_string("Autonomous Mode ON")

def autoOFF():
    socket.send_string("Autonomous Mode OFF")








app = Flask(__name__)



@app.route('/data_json')
def data_json():
    dummy_data = [{
        "id":1,
        "location": "41.856,23.352",
        "distance": "125.45 m",
        "battery_status":"90%",
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
    # dummy_data2 = [{
    #     "task":2,
    #     "name":"Magellan's Route/ Count the Manatees and Jellyfish",
    #     "manatees":3,
    #     "jellyfish":4,
        
    # }]
    # dummy_data3 =[{
    #     "task":3,
    #     "name":"Beaching & Inspecting Turtle Nests",
    #     "nest_of_the_day":"blue",
    #     "eggs_in_nest":4,


    # }]
    return jsonify(dummy_data)

@app.route('/')
def index():
    dummy_data = data_json()
  

    return render_template('index.html',data=dummy_data.json)


@app.route("/killSwitch", methods = ["POST", "GET"])
def killSwitch():
    dummy_data = data_json()
   
 
    output = request.form.to_dict()

    print(output)
    action = output["action"]

    # message()
    n = 0

    while True:

        n+=1

        killMessage()
        print("message sent")
      
        sleep(2)

        if(n == 1):
            break




    
    return render_template('index.html', action = action, data=dummy_data.json)

@app.route("/autonomous_mode", methods = ["POST","GET"])
def autonomous_mode():
    dummy_data = data_json()


    salida = request.form.to_dict()
    print(salida)
    status = salida["status"]
    task = salida["task"]


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
            socket.send_string("Task to complete: Task #"+task)
            print("message sent")
      
            sleep(2)



            if(n == 1):
                break

    return render_template('index.html', status = status, task = task, data=dummy_data.json)
    

        

if __name__=='__main__':
    app.run(debug=True)
