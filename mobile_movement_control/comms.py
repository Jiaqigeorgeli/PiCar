"""PiCar's communication library

Communication Protocols:
I2C
SPI - ...
Serial - ...
"""

import smbus

ADDRESS = 0x04 # Arduino I2C address

class I2C:
    """I2C class for PiCar"""
    
    def __init__(self):
      self.bus = smbus.SMBus(1)

    def writeNumber(self, value):
      """Send value to I2C device"""
      self.bus.write_byte(ADDRESS, value)
      return -1

    def readNumber(self):
      """Return number sent by I2C device"""
      number = self.bus.read_byte(ADDRESS)
      return number

