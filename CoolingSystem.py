from CoolingConfiguration import *
from CoolantDistributorConfig import *

from CoolantDistributor import *
from CoolingCalculator import *
from CoolingManager import *
from TemperatureHumiditySensor import *
from ConsoleReportHook import *

def main():
	print ("starting")
	report_hook = KeyValuePair("report_hook", ConsoleReportHook())
	cooling_config = CoolingConfiguration()
	coolant_distributor_config = CoolantDistributorConfig("D17")
	sensor_config = SensorConfiguration("D23", report_hook)

	sensor = TemperatureHumiditySensor(sensor_config)
	coolant_distributor = CoolantDistributor(coolant_distributor_config)
	cooling_calculator = CoolingCalculator(cooling_config)

	cooling_manager = CoolingManager(cooling_config, sensor, coolant_distributor, cooling_calculator)

	while True:
		try:
			cooling_manager.adjustCooling()
		except Exception as error:
			print ("Best message ever => There was an error. But we don't care at this point.")
			print (error)

main()
print ("ending")

quit()
