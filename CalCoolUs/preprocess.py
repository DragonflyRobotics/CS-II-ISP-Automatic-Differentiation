import random, string
import networkx as nx
from matplotlib import pyplot as plt


from CalCoolUs.ops.op_types import OpType






class ShuntingYard:
	def __init__(self):
		self.operations = ["+", "-", "/", "*", "^"]
	
	def tokenize(self, string):
		string = string.replace(" ", "")
		tokenized = []
		lowerBound = 0
		upperBound = len(string)
		for i in string:
			if (i.isdigit() or i == ".") and self.isfloat(tokenized[-1]):
				tokenized[-1] = tokenized[-1] + i
			else:
				tokenized.append(i)
		lowerBound = 0    
		upperBound = len(tokenized) - 1
		while lowerBound < upperBound:
			if tokenized[lowerBound] == "-" and (tokenized[lowerBound - 1] in self.operations or tokenized[lowerBound - 1] == "(" or tokenized[lowerBound - 1] == "-(" or lowerBound == 0):
				token = tokenized[lowerBound + 1]
				tokenized[lowerBound] = f"-{token}"
				tokenized.pop(lowerBound + 1)
				upperBound -=1
			lowerBound += 1
    
		lowerBound = 0
		upperBound = len(tokenized) - 1
		while lowerBound < upperBound:
			if tokenized[lowerBound] == "-x":
				tokenized[lowerBound] = "-1"
				tokenized.insert(lowerBound + 1, "*")
				tokenized.insert(lowerBound + 2, "x")
				lowerBound += 2
				upperBound += 2
			lowerBound += 1
		lowerBound = 0
		upperBound = len(tokenized) - 1
		while lowerBound < upperBound:
			if tokenized[lowerBound] == "-(":
				tokenized[lowerBound] = "-1"
				tokenized.insert(lowerBound + 1, "*")
				tokenized.insert(lowerBound + 2, "(")
				lowerBound += 2
				upperBound += 2
			lowerBound += 1
		return tokenized

	def isfloat(self, number):
		try:
			float(number)
			return True
		except:
			return False

	def isValue(self, number):
		return self.isfloat(number) or number == 'x' or isinstance(number, str)

	def precedence(self, operator):
		match operator:
			case "+":
				return 1
			case "-":
				return 1
			case "*":
				return 2
			case "/":
				return 2
			case "^":
				return 3
		return 0

	def getPostfix(self, diffEquation):
		diffEquation = diffEquation.replace(" ", "")
		diffEquation = self.tokenize(diffEquation)
		outputQueue = []
		operatorStack = []
		for value in diffEquation:
			if self.isfloat(value) or value == "x":
				outputQueue.append(value)
			elif value == "(":
				operatorStack.append(value)

			elif value == ")":
				while operatorStack[-1] != "(":
					assert (len(operatorStack) != 0)
					outputQueue.append(operatorStack.pop())
				assert (operatorStack[-1] == "(")
				operatorStack.pop()
			elif value in self.operations:

				while (operatorStack and operatorStack[-1] != "("
				       and self.precedence(operatorStack[-1]) >= self.precedence(value)):
					outputQueue.append(operatorStack.pop())
				operatorStack.append(value)
			
		while operatorStack:
			outputQueue.append(operatorStack.pop())

		print(outputQueue)

		return outputQueue


class ASTGraph:
	def __init__(self):
		self.operations = ["+", "-", "/", "*", "^"]

	def isValue(self, number):
		return self.isfloat(number) or number == 'x' or isinstance(number, str)

	def isfloat(self, number):
		try:
			float(number)
			return True
		except:
			return False

	def checkForOperators(self, queue):
		for q in queue:
			if q in self.operations:
				return True
		return False

	def returnOperatorName(self, operator, name=""):
		match operator:
			case "+":
				return OpType.ADD
			case "-":
				return OpType.SUB
			case "*":
				return OpType.MUL
			case "/":
				return OpType.DIV
			case "^":
				return OpType.POW
		return "UNK"

	def getAST(self, shuntyardresult):
		graph = nx.DiGraph()

		opDict = {}

		while self.checkForOperators(shuntyardresult):
			counter = 0
			while shuntyardresult[counter] not in self.operations:
				counter += 1
			# print(f"Stopped @: {shuntyardresult[counter]}")

			if (counter - 2 >= 0 and self.isValue(shuntyardresult[counter - 1]) and self.isValue(shuntyardresult[counter - 2])):
				node_name = self.returnOperatorName(shuntyardresult[counter]).name + "_" + ''.join(
					random.choices(string.ascii_uppercase +
					               string.digits, k=3))
				graph.add_edge(str(shuntyardresult[counter - 2]), node_name)
				graph.add_edge(str(shuntyardresult[counter - 1]), node_name)
				print(f"{str(shuntyardresult[counter - 2])} --> {node_name}")
				print(f"{str(shuntyardresult[counter - 1])} --> {node_name}")

				nx.set_node_attributes(graph, {node_name: {"Op": self.returnOperatorName(shuntyardresult[counter])}})

				for _ in range(3):
					shuntyardresult.pop(counter - 2)
				shuntyardresult.insert(counter - 2, node_name)
				

		return graph

	def saveGraph(self, graph, filename):
		pos = nx.planar_layout(graph, scale=40)
		nx.draw_networkx(graph, pos=pos, with_labels=True)
		plt.savefig(filename)

	def displayGraph(self, graph):
		pos = nx.planar_layout(graph, scale=40)
		nx.draw_networkx(graph, pos=pos, with_labels=True)
		plt.show(bbox_inches='tight')


