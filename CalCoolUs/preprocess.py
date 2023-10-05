import random, string
import networkx as nx
from matplotlib import pyplot as plt

class ShuntingYard:
	def __init__(self):
		self.operations = ["+", "-", "/", "*", "^"]

	def tokenize(self, string):
		r = [""]
		for i in string:
			if (i.isdigit() or i == ".") and self.isfloat(r[-1]):
				r[-1] = r[-1] + i
			else:
				r.append(i)
		return r[1:]

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

	def returnOperatorName(self, operator):
		match operator:
			case "+":
				return "ADD"
			case "-":
				return "SUB"
			case "*":
				return "MUL"
			case "/":
				return "DIV"
			case "^":
				return "POW"
		return "UNK"

	def getAST(self, shuntyardresult):
		shuntres = shuntyardresult
		graph = nx.DiGraph()

		while self.checkForOperators(shuntres):
			counter = 0
			while shuntres[counter] not in self.operations:
				counter += 1
			print(f"Stopped @: {counter}")

			if (counter - 2 >= 0 and self.isValue(shuntres[counter - 1]) and self.isValue(shuntres[counter - 2])):
				node_name = self.returnOperatorName(shuntres[counter]) + "_" + ''.join(
					random.choices(string.ascii_uppercase +
					               string.digits, k=3))
				graph.add_edge(str(shuntres[counter - 2]), node_name)
				graph.add_edge(str(shuntres[counter - 1]), node_name)
				print(f"{str(shuntres[counter - 2])} --> {node_name}")
				print(f"{str(shuntres[counter - 1])} --> {node_name}")

				for _ in range(3):
					shuntres.pop(counter - 2)
				shuntres.insert(counter - 2, node_name)

		return graph


