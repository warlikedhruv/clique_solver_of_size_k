import itertools
import networkx as nx

class Graph:
    def __init__(self):
        print("graph created")
        self.G = nx.Graph()

    def add_vertex(self, v):
        print("node: ",v," added")
        self.G.add_node(v)

    def add_edge(self,u,v):
        print("edge from",u,"to",v,"added")
        self.G.add_edge(u,v)

    def has_edge(self,u,v):
        return self.G.has_edge(u,v)

    def get_vertices(self):
        return list(self.G.nodes())

    def get_total_edges(self):
        return self.G.number_of_edges()

    def get_total_nodes(self):
        return self.G.number_of_nodes()

    def get_degree(self, node):
        return self.G.degree[node]

    def get_neighbour(self, node):
        return list(self.G.neighbors(node))

    def get_edges(self):
        return self.G.edges()

def clique_solver(G,k):
    # 2-cliques
    cliques = [{i, j} for i, j in G.get_edges() if i != j]
    k1 = 2

    count = 0
    while cliques:
        # result
        # merge k-cliques into (k+1)-cliques

        cliques_1 = set()
        for u, v in itertools.combinations(cliques, 2):
            w = u ^ v
            if len(w) == 2 and G.has_edge(*w):
                cliques_1.add(tuple(u | w))

        # remove duplicates
        cliques = list(map(set, cliques_1))
        k1 += 1
        if k1 == k and cliques != []:
            #print('%d-cliques = %d, %s.' % (k, len(cliques), cliques))
            count += 1

    if count == 0:
        return False
    else:
        return True

if __name__=="__main__":

    G = Graph()
    G.add_vertex(0)
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(0,5)
    G.add_edge(0,6)
    G.add_edge(1,2)
    G.add_edge(1,3)
    G.add_edge(1,4)
    G.add_edge(1,5)
    G.add_edge(2,3)
    G.add_edge(2,4)
    G.add_edge(2,6)
    G.add_edge(3,5)
    G.add_edge(3,6)
    G.add_edge(4,5)
    G.add_edge(4,6)
    G.add_edge(5,6)



    if clique_solver(G,4) == True:
        print("F is satisfiable")
    else:
        print("F is not satisfiable")