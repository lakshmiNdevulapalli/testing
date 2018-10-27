class directedGraph(object):
    def __init__(self, graph=None):
        if graph == None:
            graph = {}
        self.__graph = graph
    
    def add_node(self, node):
        if node not in self.__graph:
            self.__graph[node] = []
    
    def add_edge(self, edge):
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self.__graph:
            self.__graph[node1].append(node2)
        else:
            self.__graph[node1] = [node2]
    
    def nodes(self):
        return list(self.__graph.keys())

    def edges(self):
        edges = []
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                if(neighbour, node) not in edges:
                    edges.append((node, neighbour))
        return edges
    
    def __str__(self):
        res = "nodes: "
        for node in self.nodes():
            res += str(node) + " "
        res += "\nedges: "
        for edge in self.edges():
            res += str(edge) + " "
        print(res)
        return res

graph =  { "A" : ["B", "C", "E", "F"],
          "B" : ["E", "G"],
          "C" : ["E", "B", "D"],
          "D" : ["G", "F", "E"],
          "E" : ["F"],
          "F" : ["A"],
          "G" : ["D"]
}

g = directedGraph(graph)