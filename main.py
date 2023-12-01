
import sys

import serial

def work(dev):
    while True:
        ser:serial.Serial
        with serial.Serial(dev, 115200, timeout=1) as ser:
            line = ser.read_until(expected=b'\xE2\x80\xA8')
            print(line.decode('utf-8'))





if __name__ == '__main__':

    dev = sys.argv[1]
    work(dev)
