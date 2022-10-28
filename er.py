import networkx as nx
from random import sample
from numpy import sqrt
import matplotlib.pyplot as plt

def make_connected_graph(n, d):
	G = nx.fast_gnp_random_graph(n, d/(n-1))
	while not nx.is_connected(G):
		G = nx.random_regular_graph(d, n)
	return G

def sample_conductance_of_size(G, k):
	n = G.number_of_nodes()
	assert 0 < k < n, "can't get a subset of that size"
	S = sample(range(n), k)
	return nx.conductance(G, S)

def estimate_ub_Cheeger_IC(G): # upper bound the Cheeger constant, using the "improved Cheeger" approach
	# remark: this is unlikely to be useful in the random case because a.s. we get a ramanujan graph
	n = G.number_of_nodes()
	d = 2*G.number_of_edges()//n
	gls = 1 - np.sort(nx.adjacency_spectrum(G))[::-1]/d
	gl1 = gls[1]
	phi = sqrt(2*gl1)
	for k in range(2, n):
		ub = 10*sqrt(2)*gl1/sqrt(gls[k])
		phi = min(ub, phi)
	return phi

def compile_samples(n, d, amts):
	# amts is a list of nonnegative ints, the kth of which tells how many size-(k+1) cuts to sample
	assert len(amts) <= n//2, "only sample for cuts of size up to half the graph"
	G = make_connected_graph(n,d)
	conductances = []
	for k in range(len(amts)):
		for _ in range(amts[k]):
			conductances.append(sample_conductance_of_size(G, k+1))
	conductances.sort()
	plt.plot(conductances)
	plt.show()
	plt.close()

# compile_samples(500, 6, (100,)*50)
# compile_samples(500, 6, (0,)*170 + (100,)*30)
