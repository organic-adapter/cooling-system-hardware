import time
import board
import digitalio
from Distributor import *
from DistributorStatus import *

class CoolantDistributor(Distributor):
	def __init__(self, config):
		self.config = config
		self.initHardware()

	def disable(self):
		self.output.value = False

	def enable(self):
		self.output.value = True

	def initHardware(self):
		self.output_pin_name = self.config.output_pin_name
		self.output_pin = getattr(board, self.config.output_pin_name)
		self.output = digitalio.DigitalInOut(self.output_pin)
		self.output.direction = digitalio.Direction.OUTPUT

	def isEnabled(self):
		return self.output.value

	def status(self):
		try:
			return DistributorStatus.On if self.isEnabled() else DistributorStatus.Off
		except Exception as error:
			return DistributorStatus.Error
