class Graph:
    import random
    vertices = []
    parent = []

    def addEdge(self, u, v):
        self.vertices.append((u, v))

    def setParents(self):
        self.parent = []
        for i in range(0, len(self.vertices)):
            self.parent.append(i)

    def find(self, u):
        if self.parent[u] == u:
            return u
        else:
            self.parent[u] = self.find(self.parent[u])
            return self.parent[u]

    def union(self, u, v):
        a = self.find(u)
        b = self.find(v)
        if a != b:
            self.parent[a] = b

    def krager(self):
        V = len(self.vertices)
        while V > 2:
            print(V)
            edge = self.random.choice(self.vertices)
            subset1 = self.find(edge[0])
            subset2 = self.find(edge[1])

            self.vertices.remove(edge)

            if(subset1 != subset2):
                V -= 1
                self.union(subset1, subset2)

        cutedges = 0
        for edge in self.vertices:
            subset1 = self.find(edge[0])
            subset2 = self.find(edge[1])
            if(subset1 != subset2):
                cutedges += 1

        return cutedges


def main():
    graphInfoFile = open("kargerMinCut.txt", "r")
    line = graphInfoFile.readline()
    graph = Graph()
    while line:
        u, *y = map(int, line.split())
        line = graphInfoFile.readline()
        for v in y:
            graph.addEdge(u, v)

    ans = 250

    for i in range(0, 1):
        graph.setParents()
        ans = min(ans, graph.krager())

    print(ans)


if __name__ == "__main__":
    main()
