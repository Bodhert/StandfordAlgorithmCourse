
class Graph:
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
        uNodes = [value for value in uNodes if value != u]
        uNodes = [value for value in uNodes if value != v]
        self.vertices[u] = uNodes
        self.vertices.pop(v, None)


def main():
    graphInfoFile = open("kargerMinSmall.txt", "r")
    line = graphInfoFile.readline()
    graph = Graph()
    while line:
        x, *y = map(int, line.split())
        line = graphInfoFile.readline()
        graph.addEdge(x, y)

    # graph.joinAdjacentNodes(1, 3)
    # graph.joinAdjacentNodes(2, 4)

    graph.joinAdjacentNodes(1, 3)
    graph.joinAdjacentNodes(1, 2)
    print("debug")


if __name__ == "__main__":
    main()
