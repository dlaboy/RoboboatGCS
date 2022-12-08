import zmq
import keyboard
from time import sleep

# Kill switch pub
# def killSwitchPub():
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://127.0.0.1:8090")

def message():
    socket.send_string("Kill Switch Pressed")

n = 0

while True:

    n+=1

    message()
      
    sleep(2)