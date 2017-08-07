import serial
import time

ser = serial.Serial("/dev/ttyACM0")
time.sleep(2)

def write_pos(z,y):
    ser.write(0)
    ser.write(y)
    ser.write(1)
    ser.write(z)


while True:
    with open("comm_pipe", "r") as f:
        line = f.readline()
        stripped_line = line.strip()
        data = stripped_line.split(",")
        data = map(int, data)
        if(len(data) == 2):
            write_pos(data[0], data[1])
    if(line == "0\n"):
        break

