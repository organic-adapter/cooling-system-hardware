import time
from DistributorStatus import *

class CoolingManager:
	def __init__\
		( \
			self, \
			cooling_config, \
			tempHumidSensor, \
			coolant_distributor, \
			cooling_calculator
		):
		self.cooling_config = cooling_config
		self.sensor = tempHumidSensor
		self.coolant_distributor = coolant_distributor
		self.cooling_calculator = cooling_calculator

	def adjustCooling(self):
		sample = self.sensor.takeSample()

		if self.cooling_calculator.isSampleWithinRange(sample):
			self.setCoolantDistributor(DistributorStatus.On)
		else:
			self.setCoolantDistributor(DistributorStatus.Off)

		time.sleep(self.cooling_config.sample_wait_s)

	def setCoolantDistributor(self, status: DistributorStatus):
		if status == DistributorStatus.On:
			self.coolant_distributor.enable()
		else:
			self.coolant_distributor.disable()

	def getCoolantDistributorStatus(self):
		return self.coolant_distributor.status()
