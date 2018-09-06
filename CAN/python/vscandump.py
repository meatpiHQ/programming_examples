#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
Example for receiing CAN frames via ASCII protocol (slcan).
"""

import sys

import can
import serial

CAN_DEV = '/dev/ttyUSB0@3000000'


def main():
    """main routine."""
    try:
        bus = can.interface.Bus(bustype='slcan',
                                channel=CAN_DEV,
                                rtscts=True,
                                bitrate=1000000)
    except serial.serialutil.SerialException as err:
        print(err)
        sys.exit(1)

    while True:
        msg = bus.recv()
        data = "".join("{:02X} ".format(byte) for byte in msg.data)
        print("{:X} [{}] {}".format(msg.arbitration_id,
                                    msg.dlc,
                                    data))

    bus.shutdown()


if __name__ == '__main__':
    main()
