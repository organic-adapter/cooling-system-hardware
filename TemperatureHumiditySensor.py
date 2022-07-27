import pytz
from datetime import datetime
import time
import board
import adafruit_dht
import uuid

class Sample:
	def __init__(self, id, key, value):
		self.id = id
		self.key = key
		self.value = value
	def getId(self):
		return self.id
	def getKey(self):
		return self.key
	def getValue(self):
		return self.value

class TemperatureSample:
	def __init__(self, id, timestamp, tempC):
		self.id = id
		self.timestamp = timestamp
		self.temperatureCelcius = tempC # CONTRACTS MATTER: standard JSON compatible naming

class HumiditySample:
	def __init__(self, id, timestamp, relative_humidity):
		self.id = id
		self.timestamp = timestamp
		self.relativeHumidity = relative_humidity # CONTRACTS MATTER: standard JSON combatible naming

class TemperatureHumiditySample:
	def __init__(self, id, timestamp, tempC, humidity):
		self.temperature_sample = TemperatureSample(id, timestamp, tempC)
		self.humidity_sample = HumiditySample(id, timestamp, humidity)
		self.humidity = humidity
	def getTempC(self):
		return self.temperature_sample.temperatureCelcius
	def getTempF(self):
		return (self.getTempC * 5 / 9) + 32
	def getHumidity(self):
		return self.humidity_sample.relativeHumidity

class KeyValuePair:
	def __init__(self, key, value):
		self.key = key
		self.value = value

class SensorConfiguration:
	def __init__(self, data_pin_name, *kvps):
		self.data_pin_name = data_pin_name
		for kvp in kvps:
			setattr(self, kvp.key, kvp.value)

class TemperatureHumiditySensor:
	def __init__(self, config:SensorConfiguration):
		self.data_pin_name = config.data_pin_name
		self.data_pin = getattr(board, config.data_pin_name)
		self.sensor = adafruit_dht.DHT11(self.data_pin)

		if hasattr(config, "report_hook"): # now that we have a manager this is in the wrong spot
			self.report_hook = config.report_hook

	def takeSample(self):
		now = datetime.now()
		utcFormat = now.astimezone(pytz.UTC).isoformat()
		sensor = self.sensor

		try:
			tempC = sensor.temperature
			tempF = (tempC * 9 / 5) + 32
			humidity = sensor.humidity
			self.report(utcFormat, tempC, tempF, humidity)
			return TemperatureHumiditySample(uuid.uuid4(), utcFormat, tempC, humidity)
		except RuntimeError as error:
			print (error.args[0])
			raise error
		except Exception as error:
			sensor.exit()
			raise error

	def report(self, timestamp, tempC, tempF, humidity):
		if(hasattr(self, "report_hook")):
			id = uuid.uuid4()
			self.report_hook \
				.report \
				(\
					Sample(id, "timestamp", timestamp)\
					, Sample(id, "tempC", tempC)\
					, Sample(id, "tempF", tempF)\
					, Sample(id, "humidity", humidity)\
				)
		else:
			print(timestamp)
			print("Temperature: {}C ({}F)   Humidity: {}% ".format(tempC, tempF, humidity))
