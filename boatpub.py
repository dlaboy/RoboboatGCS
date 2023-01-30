import zmq
from time import sleep
import time

import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()


from dronekit import connect


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % "8091")


# connection to dronekit
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)




# def locatin():
#     socket.send_string(str(latitude)+","+str(longitude))


# def distancia():
#     socket.send_string(str(distance))


# def bateria():
#     socket.send_string(str(battery))
#     socket.send_string("")



 #Callback to print the location in global frames. 'value' is the updated value




while True:



    time.sleep(1)

    latitude = vehicle.location.global_frame.lat
    roundedLat = round(latitude, 3)

    longitude = vehicle.location.global_frame.lon
    roundedLon = round(longitude, 3)

    # battery = vehicle.battery.level

    # distance = vehicle.location.local_frame.distance_home()

    vehicle.close()


    socket.send_string(str(roundedLat)+","+str(roundedLon))

    # distancia()
    # bateria()

    sleep(1)



