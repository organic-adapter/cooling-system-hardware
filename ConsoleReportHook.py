class ConsoleReportHook:
	def report(self, *reports):
		for report in reports:
			print ("SampleId:{} = {}: {}".format(report.getId(), report.getKey(), report.getValue()))
