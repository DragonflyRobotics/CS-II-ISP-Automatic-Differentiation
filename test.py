import networkx as nx
from matplotlib import pyplot as plt

from CalCoolUs.preprocess import ShuntingYard

myshunt = ShuntingYard()

shuntres = myshunt.getPostfix("( (( x^ 200.31419)) +66 * x) * ( 74 + 75 / x )")
print(shuntres)

from CalCoolUs.preprocess import ASTGraph

myASTGraph = ASTGraph()
graph = myASTGraph.getAST(shuntres)
pos = nx.planar_layout(graph, scale=40)
nx.draw_networkx(graph, pos=pos, with_labels=True)
# plt.savefig("fig.png")
plt.show(bbox_inches='tight')