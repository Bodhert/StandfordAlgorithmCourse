class Graph:
    MAXN = 200
    import random
    vertices = set()
    parent = []

    def addEdge(self, u, v):
        self.vertices.add((u, v))

    def setParents(self):
        self.parent = []
        for i in range(0, self.MAXN):  # 0  to the total num of vertices
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

        self.vertices =  set(map(tuple, map(sorted, self.vertices))) 

        V = self.MAXN
        while V > 2:

            edge = self.random.choice(tuple(self.vertices))
            subset1 = self.find(edge[0])
            subset2 = self.find(edge[1])

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
        u -= 1  # indexes fix
        for v in y:
            v -= 1 # indexes fix
            graph.addEdge(u, v)

    ans = 250

    for i in range(0, 150):
        graph.setParents()
        ans = min(ans, graph.krager())

    print(ans)


if __name__ == "__main__":
    main()
