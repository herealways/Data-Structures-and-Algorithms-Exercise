# Unweighted and undirected graph


class Graph:
    def __init__(self):
        self.num_of_nodes = 0
        self.adjacent_list = {}

    def addNode(self, node):
        self.adjacent_list[node] = set()
        self.num_of_nodes += 1

    def addEdge(self, node, target):
        if node not in self.adjacent_list:
            raise KeyError(f'Cannot find {node} in the graph')
        if target not in self.adjacent_list[node]:
            self.adjacent_list[node].add(target)
            self.adjacent_list[target].add(node)  # Undirected


if __name__ == "__main__":
    myGraph = Graph()
    myGraph.addNode('0')
    myGraph.addNode('1')
    myGraph.addNode('2')
    myGraph.addNode('3')
    myGraph.addNode('4')
    myGraph.addNode('5')
    myGraph.addNode('6')
    myGraph.addEdge('0', '1')
    myGraph.addEdge('0', '2')
    myGraph.addEdge('1', '2')
    myGraph.addEdge('1', '3')
    myGraph.addEdge('2', '4')
    myGraph.addEdge('3', '4')
    myGraph.addEdge('4', '5')
    myGraph.addEdge('5', '6')
    print(myGraph.adjacent_list)
