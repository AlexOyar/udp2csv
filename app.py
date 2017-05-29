import socket
import csv
import numpy as np
from numpy import genfromtxt

#Initialize UDP connection
UDP_IP = "0.0.0.0"
UDP_PORT = 8888
i = 0

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(1)
#sock.settimeout(5.0)

#Read from socket and save values to numpy array and csv file
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames =['Sample','F1','F2','F3','Ax','Ay','Az']
    writer = csv.DictWriter(csvfile, delimiter=',',
                        quotechar='h', quoting=csv.QUOTE_MINIMAL,fieldnames=fieldnames)
    #writer.writerow(['F1 ','F2 ','F3 ','Ax ','Ay ','Az '])
    writer.writeheader()
    while True:
        try:
            data = sock.recv(8096) # buffer size is 1024 bytes
            data = data.decode("utf-8")
            final = np.fromstring(data, sep=',')
            i = i + 1
            print("received message: ",i, " ", final[0], final[1], final[2], final[3], final[4], final[5])
            writer.writerow({'Sample':i,'F1':final[0],'F2':final[1],'F3':final[2],'Ax':final[3],'Ay':final[4],'Az':final[5],})
        except Exception as e:
            print(e)
    sock.close()

