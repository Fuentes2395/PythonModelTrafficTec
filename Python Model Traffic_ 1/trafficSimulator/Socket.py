    

def draw_vehicles(self):
    contr = 0
    for road in self.sim.roads:
        # Draw vehicles
        contv = 0 
        for vehicle in road.vehicles:
            x, y  = self.draw_vehicle(vehicle, road)
            print (contr, contv, x, y)
            contv += 1
        contr += 1


import socket
import struct
import traceback
import logging
import time

def sending_and_reciveing():
    s = socket.socket()
    socket.setdefaulttimeout(None)
    print('socket created ')
    port = 60000
    s.bind(('127.0.0.1', port)) #local host
    s.listen(30) #listening for connection for 30 sec?
    print('socket listensing ... ')
    while True:
        try:
            c, addr = s.accept() #when port connected
            bytes_received = c.recv(4000) #received bytes
            array_received = np.frombuffer(bytes_received, dtype=np.float32) #converting into float array

            nn_output = return_prediction(array_received) #NN prediction (e.g. model.predict())

            bytes_to_send = struct.pack('%sf' % len(nn_output), *nn_output) #converting float to byte
            c.sendall(bytes_to_send) #sending back
            c.close()
        except Exception as e:
            logging.error(traceback.format_exc())
            print("error")
            c.sendall(bytearray([]))
            c.close()
            break

sending_and_reciveing() 