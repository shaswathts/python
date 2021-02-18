import socket
import numpy as np
import encodings
#import Adafruit_DHT
import random


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


# Function to read sensor values
def random_data():
    temp = random.randint(25,45)
    hum = random.randint(50,60)
    air = random.randint(55,60)
    light = random.randint(100,180)
    
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, hum))
    print('Air={0:0.1f}*PPM  Light={1:0.1f}*LUX'.format(air, light))
    print("data was written on database T{} H{} A{} L{}".format(temp, hum, air, light))
    data = '{},{},{},{}'.format(temp, hum, air, light)
    return data

#def random_data():
#    pin = 4
#    sensor = Adafruit_DHT.DHT22
#    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#
#    if humidity is not None and temperature is not None:
#        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
#        print("data was written on database T{} H{}".format(temperature,humidity))
#        data = '{},{}'.format(temperature,humidity)
#        return data


def my_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server Started waiting for client to connect ")
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)
            while True:

                data = conn.recv(1024).decode('utf-8')

                if str(data) == "Data":

                    print("Ok Sending data ")

                    my_data = random_data()

                    x_encoded_data = my_data.encode('utf-8')

                    conn.sendall(x_encoded_data)

                elif  str(data) == "Quit":
                    print("shutting down server ")
                    break

                # if not data:
                #   break
                else:
                    pass


if __name__ == '__main__':
    while 1:
        my_server()

