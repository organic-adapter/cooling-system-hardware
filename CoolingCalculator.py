from TemperatureHumiditySensor import TemperatureHumiditySample, TemperatureSample, HumiditySample

class CoolingCalculator:
	def __init__(self, cooling_config):
		self.cooling_config = cooling_config

	def isSampleWithinRange(self, sample: TemperatureHumiditySample):
		return self.isTemperatureWithinRange(sample.temperature_sample) \
			and self.isHumidityWithinRange(sample.humidity_sample)

	def isTemperatureWithinRange(self, sample: TemperatureSample):
		return sample.temperatureCelcius >= self.cooling_config.tempC_min - self.cooling_config.tempC_variance \
                        and sample.temperatureCelcius <= self.cooling_config.tempC_max + self.cooling_config.tempC_variance

	def isHumidityWithinRange(self, sample: HumiditySample):
		return sample.relativeHumidity >= self.cooling_config.rh_min - self.cooling_config.rh_variance \
			and sample.relativeHumidity <= self.cooling_config.rh_max + self.cooling_config.rh_variance
