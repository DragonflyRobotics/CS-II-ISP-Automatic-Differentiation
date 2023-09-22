class Scope:
    def __init__(self):
        self.scope = []
    def add(self, variable, constant):
        variable.value += constant
        return variable.value, 1

    def multiply(self, variable, constant):
        variable.value *= constant
        return variable.value, constant

    def gradient(self):
        gradient = 1
        for s in self.scope:

            if type(s[0]) == Variable:
                print(s[0]())
                print(s[0].value)
            else:
                print(s[0](s[1], s[2]))
                print(s)
                gradient *= s[0](s[1], s[2])[1]
        print(gradient)

class Variable:
    def __init__(self, value):
        self.value = value
        self.scope = Scope()
        self.scope.scope.append([self])
    def __add__(self, constant):
        self.scope.scope.append([self.scope.add, self, constant])
        return self
    def __mul__(self, constant):
        self.scope.scope.append([self.scope.multiply, self, constant])
        return self
    def __call__(self):
        return self.value, 1

x = Variable(3)
x = x + 5
x = x + 7
x = x*2
# print(x.scope.scope)
x.scope.gradient()
