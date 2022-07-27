from abc import ABC, abstractmethod

class Distributor(ABC):
	@abstractmethod
	def enable(self):
		pass

	@abstractmethod
	def disable(self):
		pass

	@abstractmethod
	def status(self):
		pass
