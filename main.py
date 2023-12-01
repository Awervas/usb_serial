
import sys

import serial

def work(dev):
    while True:
        with serial.Serial(dev, 115200, timeout=1) as ser:
            line = ser.readline()
            print(line)

if __name__ == '__main__':

    dev = sys.argv[1]
    work(dev)
