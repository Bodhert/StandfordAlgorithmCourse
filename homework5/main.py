from PriorityQueue import PriorityQueue

MAXN = 205
adjList = {}
dist = []



def dijskstra(source):
    global dist
    global adjList

    pq = PriorityQueue()
    dist[source] = 0
    pq.insertNode((source, 0))

    while pq.getSize() > 1:
        currPair = pq.getMin()
        currNodeIndex = currPair[0]
        currWeight = currPair[1]
        if( currWeight > dist[currNodeIndex]):
            continue
        
        for neighbor in adjList[currNodeIndex]:
            nextNodeIndex = neighbor[0]
            nextWeight = neighbor[1]
            if dist[currNodeIndex] + nextWeight < dist[nextNodeIndex]:
                dist[nextNodeIndex] = dist[currNodeIndex] + nextWeight
                pq.insertNode(neighbor)



def setVariables():
    global dist
    global MAXN

    dist = [float('inf')] * MAXN

def buildGraphFromInput():
    global adjList

    with open('dijkstraData.txt') as inputFile:
        for line in inputFile:
            source, *dest = map(str, line.split())
            source = int(source)
            dest = [tuple(element.split(',')) for element in dest]
            dest = [tuple(map(int, tup)) for tup in dest]
            adjList[source] = dest
            
def main():
    global dist

    buildGraphFromInput()
    setVariables()
    dijskstra(1)

    print(dist[7])
    print(dist[37])
    print(dist[59])
    print(dist[82])
    print(dist[99])
    print(dist[115])
    print(dist[133])
    print(dist[165])
    print(dist[188])
    print(dist[197])
    # 7,37,59,82,99,115,133,165,188,197    


if __name__ == '__main__':
    main()
