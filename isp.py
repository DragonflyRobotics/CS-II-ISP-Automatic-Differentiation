import random, string

import networkx as nx
from matplotlib import pyplot as plt

class Scope:
    def __init__(self):
        self.scope = nx.DiGraph()

class Variable:
    def __init__(self, name):
        self.name = name
        self.rootscope = Scope()
        self.rootscope.scope.add_node(self.name)
        self.join_head = 'x'
        self.variableName = 'x'

    def __str__(self):
        return self.variableName

    def __mul__(self, other):
        if type(other) == Variable:
            self.name = self.join_head
            print(f"Name: {self.name}")
            self.join_head = "MUL_" + ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=7))
            self.rootscope.scope.add_edge(self.name, self.join_head)
            self.rootscope.scope.add_edge(self.variableName, self.join_head)
            print(f"{self.name} --> {self.join_head}")
            print(f"{str(other)} --> {self.join_head}")
        else:
            self.name = self.join_head
            self.join_head = "CMUL_" + ''.join(random.choices(string.ascii_uppercase +
                                                             string.digits, k=7))
            self.rootscope.scope.add_edge(self.name, self.join_head)
            self.rootscope.scope.add_edge(str(other), self.join_head)
            print(f"{self.name} --> {self.join_head}")
            print(f"{str(other)} --> {self.join_head}")
        return self
    def __add__(self, other):
        if type(other) == Variable:
            self.name = self.join_head
            self.join_head = "ADD_" + ''.join(random.choices(string.ascii_uppercase +
                                                             string.digits, k=7))
            self.rootscope.scope.add_edge(self.name, self.join_head)
            self.rootscope.scope.add_edge(self.variableName, self.join_head)
            print(f"{self.name} --> {self.join_head}")
            print(f"{str(other)} --> {self.join_head}")
        else:
            self.name = self.join_head
            self.join_head = "CADD_" + ''.join(random.choices(string.ascii_uppercase +
                                                             string.digits, k=7))
            self.rootscope.scope.add_edge(self.name, self.join_head)
            self.rootscope.scope.add_edge(str(other), self.join_head)
            print(f"{self.name} --> {self.join_head}")
            print(f"{str(other)} --> {self.join_head}")
        return self

    def __sub__(self, other):
        if type(other) == Variable:
            self.name = self.join_head
            self.join_head = "SUB_" + ''.join(random.choices(string.ascii_uppercase +
                                                             string.digits, k=7))
            self.rootscope.scope.add_edge(self.name, self.join_head)
            self.rootscope.scope.add_edge(self.variableName, self.join_head)
            print(f"{self.name} --> {self.join_head}")
            print(f"{str(other)} --> {self.join_head}")
        else:
            self.name = self.join_head
            self.join_head = "CSUB_" + ''.join(random.choices(string.ascii_uppercase +
                                                             string.digits, k=7))
            self.rootscope.scope.add_edge(self.name, self.join_head)
            self.rootscope.scope.add_edge(str(other), self.join_head)
            print(f"{self.name} --> {self.join_head}")
            print(f"{str(other)} --> {self.join_head}")
        return self

    def __pow__(self, other):
        if type(other) == Variable:
            self.name = self.join_head
            self.join_head = "POW_" + ''.join(random.choices(string.ascii_uppercase +
                                                             string.digits, k=7))
            self.rootscope.scope.add_edge(self.name, self.join_head)
            self.rootscope.scope.add_edge(self.variableName, self.join_head)
            print(f"{self.name} --> {self.join_head}")
            print(f"{str(other)} --> {self.join_head}")
        else:
            self.name = self.join_head
            self.join_head = "CPOW_" + ''.join(random.choices(string.ascii_uppercase +
                                                             string.digits, k=7))
            self.rootscope.scope.add_edge(self.name, self.join_head)
            self.rootscope.scope.add_edge(str(other), self.join_head)
            print(f"{self.name} --> {self.join_head}")
            print(f"{str(other)} --> {self.join_head}")
        return self

    def __(self):
        print(f"ABS: {self.variableName}")
        self.join_head = self.variableName
        return self

    def __eq__(self, other):
        return self


x = Variable('x')
x = x**2
x = x * (x*8)

# x = x._paren()==(x**2) * x._paren()==(x*8)#+ (x*8) + x#x-(x * 8)
# x = (x+2) * (8 * x) - 4 + (2 * x)
pos = nx.nx_pydot.pydot_layout(x.rootscope.scope)
nx.draw_networkx(x.rootscope.scope, pos=pos, with_labels=True)
plt.savefig("fig.png")