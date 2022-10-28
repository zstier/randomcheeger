import networkx as nx
from regular import make_connected_graph
import pickle
import matplotlib.pyplot as plt

n = 24
hpl = pickle.load(open("halfpowerlists/" + str(n) + ".p", "rb"))

G = make_connected_graph(n,4)
print(nx.to_numpy_matrix(G))
nx.draw(G)
# plt.show()
plt.savefig("G.png")
plt.close()
print("saved graph")

data = [ nx.conductance(G,S) for S in hpl ]
plt.hist(data, bins=100, range=[0,1], log=True)
# plt.show()
plt.savefig("hist.png")
plt.close()
print("saved histogram")
