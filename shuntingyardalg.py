import random, string
import networkx as nx
from matplotlib import pyplot as plt
import re

import CalCoolUs.preprocess

graph = nx.DiGraph()
operations = ["+", "-", "/", "*", "^"]

def isfloat(number):
    try:
        float(number)
        return True
    except:
        return False

diffEquation = "( (( x^ -200.31419)) +66 * x) * ( 74 + 75 / x )"
diffEquation = diffEquation.replace(" ", "")



def tokenize(string):
    r = [""]
    for i in diffEquation:
        if (i.isdigit() or i == ".") and isfloat(r[-1]):
            r[-1] = r[-1] + i
        else:
            r.append(i)
    return r[1:]

diffEquation = tokenize(diffEquation)



def isValue(number):
    return isfloat(number) or number == 'x' or isinstance(number, str)


def returnOperatorName(operator):
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

outputQueue = []    
operatorStack = []
def precedence(operator):
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

for value in diffEquation:
    if isfloat(value) or value == "x":
        outputQueue.append(value)
    elif value == "(":
        operatorStack.append(value)

    elif value == ")":   
        while operatorStack[-1] != "(":
            assert(len(operatorStack) != 0)
            outputQueue.append(operatorStack.pop())
        assert(operatorStack[-1] == "(")
        operatorStack.pop()
    elif value in operations:

        while (operatorStack and operatorStack[-1] != "("
               and precedence(operatorStack[-1]) >= precedence(value)):
            outputQueue.append(operatorStack.pop())
        operatorStack.append(value)
while operatorStack:
    outputQueue.append(operatorStack.pop())

from CalCoolUs.preprocess import ShuntingYard

myshunt = ShuntingYard()

shuntres = myshunt.getPostfix("( (( x^ -200.31419)) +66 * x) * ( 74 + 75 / x )")
assert myshunt.getPostfix("( (( x^ -200.31419)) +66 * x) * ( 74 + 75 / x )") == outputQueue

from CalCoolUs.preprocess import ASTGraph

myASTGraph = ASTGraph()
newGraph = myASTGraph.getAST(shuntres)
pos = nx.spring_layout(graph, scale=3)
nx.draw_networkx(graph, pos=pos, with_labels=True)
# plt.savefig("fig.png")
plt.show(bbox_inches='tight')

exit(4)

def checkForOperators(queue):
    for q in queue:
        if q in operations:
            return True
    return False


while checkForOperators(outputQueue):
    counter = 0
    while outputQueue[counter] not in operations:
        counter += 1
    print(f"Stopped @: {counter}")

    if (counter - 2 >= 0 and isValue(outputQueue[counter-1]) and isValue(outputQueue[counter-2])):
        node_name = returnOperatorName(outputQueue[counter]) + "_" + ''.join(random.choices(string.ascii_uppercase +
                                                                 string.digits, k=3))
        graph.add_edge(str(outputQueue[counter-2]), node_name)
        graph.add_edge(str(outputQueue[counter-1]), node_name)
        print(f"{str(outputQueue[counter - 2])} --> {node_name}")
        print(f"{str(outputQueue[counter - 1])} --> {node_name}")

        for _ in range(3):
            outputQueue.pop(counter-2)
        outputQueue.insert(counter-2, node_name)

    print(outputQueue)

pos = nx.spring_layout(graph, scale=3)
nx.draw_networkx(graph, pos=pos, with_labels=True)
# plt.savefig("fig.png")
plt.show(bbox_inches='tight')

