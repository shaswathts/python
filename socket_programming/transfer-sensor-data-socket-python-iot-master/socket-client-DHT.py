import socket
import threading
import time


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def process_data_from_server(x):
    x1, y1, z1, a1 = x.split(",")
    return x1,y1,z1,a1


def my_client():
    threading.Timer(11, my_client).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        my = input("Enter command ")

        my_inp = my.encode('utf-8')

        s.sendall(my_inp)

        data = s.recv(1024).decode('utf-8')

        x_temperature,y_humidity,z_air,a_light = process_data_from_server(data)

        print("Temperature {}".format(x_temperature))
        print("Humidity {}".format(y_humidity))
        print("Air {}".format(z_air))
        print("Light {}".format(a_light))
        

        s.close()
        time.sleep(5)


if __name__ == "__main__":
    while 1:
        my_client()