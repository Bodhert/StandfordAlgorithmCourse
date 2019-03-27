class Graph:
    import random
    vertices = {}

    def addEdge(self, u, v):
        self.vertices[u] = v

    def joinAdjacentNodes(self, u, v):
        uNodes = self.vertices[u]
        vNodes = self.vertices[v]
        neighborsToModify = []

        for vNode in vNodes:
            if vNode != u:
                neighborsToModify.append(vNode)

        for i in neighborsToModify:
            tempNodes = self.vertices[i]
            self.vertices[i] = [u if x == v else x for x in tempNodes]

        uNodes = uNodes + vNodes
        uNodes = [value for value in uNodes if value != u and value != v]

        self.vertices[u] = uNodes
        self.vertices.pop(v, None)

    def selectRandomAdjacentNodes(self):
        node = self.random.choice(list(self.vertices.keys()))
        randomNeighbor = self.random.choice(self.vertices[node])
        return node, randomNeighbor

def main():
    import copy

    graphInfoFile = open("kargerMinCut.txt", "r")
    line = graphInfoFile.readline()
    graph = Graph()
    while line:
        x, *y = map(int, line.split())
        line = graphInfoFile.readline()
        graph.addEdge(x, y)

    unmutableGraph = copy.deepcopy(graph.vertices)

    ans = 250

    for i in range(0,15):
        while len(graph.vertices) != 2:
            node, neighbor = graph.selectRandomAdjacentNodes()
            graph.joinAdjacentNodes(node,neighbor)

        node, neighbor = next(iter( graph.vertices.items()))
        ans = min(ans, len(neighbor))
        graph.vertices = copy.deepcopy(unmutableGraph)

    print (ans)
if __name__ == "__main__":
    main()
