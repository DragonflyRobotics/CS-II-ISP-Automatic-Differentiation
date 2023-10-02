diffEquation = "( ( x^ 2) +6 * x) * ( 4 + 5 / x )"
diffEquation = diffEquation.replace(" ", "")


def tokenize(string):
    string = string.replace(" ", "")
    array = []
    for c in string:
        array.append(c)
    return array

diffEquation = tokenize(diffEquation)

def isfloat(number):
    try: 
        float(number)
        return True
    except:
        return False
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
operations = ["+", "-", "/", "*", "^"]
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
        operatorStack.pop
    elif value in operations:
        while (operatorStack and operatorStack[-1] != "("
               and precedence(operatorStack[-1]) >= precedence(value)):
            outputQueue.append(operatorStack.pop())
        operatorStack.append(value)
while operatorStack:
    outputQueue.append(operatorStack.pop())        
for value in outputQueue:
    if value == "(":
        outputQueue.remove(value) 
print(outputQueue)
