#!/home/szbaijie/usb_serial/env/bin/python3
import argparse
import time

ALLOW_BAUDRATE = [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                  9600, 19200, 38400, 57600, 115200, 230400, 460800, 500000,
                  576000, 921600, 1000000, 1152000, 1500000, 2000000, 2500000,
                  3000000, 3500000, 4000000]

import serial


def work(port_parameter):
    while True:
        ser: serial.Serial
        try:
            with serial.Serial(port_parameter.port, port_parameter.baudrate, timeout=port_parameter.timeout) as ser:
                line = ser.read_until(expected=b'\xE2\x80\xA8')
                print(line.decode('utf-8', errors='ignore'))
        except Exception as e:

            print(f'error read {e}, next attempt after 10 seconds')
            time.sleep(10)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='USB Serial reader')
    parser.add_argument("port", type=str, help='port')
    parser.add_argument('-b', '--baudrate', type=int, help='baudrate',
                        choices=ALLOW_BAUDRATE, default=1152000)
    parser.add_argument('-t', '--timeout', type=int, help='read timeout', default=3)

    args = parser.parse_args()
    try:
        work(args)
    except KeyboardInterrupt:
        print('closed')
        exit(0)
