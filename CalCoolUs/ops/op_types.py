from enum import Enum

from CalCoolUs.ops.add import Add
from CalCoolUs.ops.sub import Sub

class OpType(Enum):
	ADD = Add("ADD")
	SUB = 1 #Sub("works_again?")
	MUL = 2
	DIV = 3
	POW = 4
	CONST = 5
	VAR = 6