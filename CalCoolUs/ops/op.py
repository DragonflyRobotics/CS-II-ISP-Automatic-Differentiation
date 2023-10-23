from abc import ABC, abstractmethod
from enum import Enum

class Generic_Op(ABC):
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	@abstractmethod
	def getDerivative(self, *args, **kwargs):
		pass

	@abstractmethod
	def __call__(self, *args, **kwargs):
		pass

