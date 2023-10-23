import networkx as nx
from matplotlib import pyplot as plt

from CalCoolUs.preprocess import ShuntingYard, OpType


# sub = OpType.SUB
# print(sub.value)
#
# print(sub.value.)

myshunt = ShuntingYard()

shuntres = myshunt.getPostfix("( (( x^ 200.31419)) +66 * x) * ( 74 + 75 * x )")
print(shuntres)

from CalCoolUs.preprocess import ASTGraph

myASTGraph = ASTGraph()
graph = myASTGraph.getAST(shuntres)
pos = nx.planar_layout(graph, scale=40)
nx.draw_networkx(graph, with_labels=True)
# plt.savefig("fig.png")
plt.show(bbox_inches='tight')