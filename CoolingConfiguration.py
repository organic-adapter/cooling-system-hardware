import json
class CoolingConfiguration:
	def __init__(self):
		self.load()
	def load(self):
		f = open("cooling-config.json", "r")
		json_str = f.read()
		json_dict = json.loads(json_str)
		self.rh_min = json_dict['rhMin']
		self.rh_max = json_dict['rhMax']
		self.tempC_min = json_dict['tempCMin']
		self.tempC_max = json_dict['tempCMax']
		self.rh_variance = json_dict['rhVariance']
		self.tempC_variance = json_dict['tempCVariance']
		self.sample_wait_s = json_dict['sampleWaitS']
