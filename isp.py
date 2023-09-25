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

    def __mul__(self, other):
        self.name = self.join_head
        self.join_head = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=7))
        self.rootscope.scope.add_edge(self.name, self.join_head)
        self.rootscope.scope.add_edge(str(other), self.join_head)
        return self

x = Variable('x')
x *= 3
x *= 4
pos = nx.nx_pydot.pydot_layout(x.rootscope.scope)
nx.draw_networkx(x.rootscope.scope, pos=pos, with_labels=True)
plt.show()