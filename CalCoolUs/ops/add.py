from CalCoolUs.ops.op import Generic_Op

class Add(Generic_Op):
	def __init__(self, name):
		super().__init__(name)

	def getDerivative(self, *args, **kwargs):
		return 1

	def __call__(self, a, b):
		return a+b

