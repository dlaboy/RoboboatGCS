import zmq

# def killSwitchSub():
context = zmq.Context()
socket = context.socket(zmq.SUB)
# accept all topics (prefixed) - default is none
socket.setsockopt_string(zmq.SUBSCRIBE, "")
socket.bind("tcp://*:8090")

n = 0

while True:
    n+=1
    message = socket.recv_string()        
    print(message)