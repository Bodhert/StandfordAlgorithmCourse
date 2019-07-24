from PriorityQueue import PriorityQueue
adjList = {}



def buildGraphFromInput():
    with open('dijkstraData.txt') as inputFile:
        for line in inputFile:
            source, *dest = map(str, line.split())
            source = int(source)
            dest = [tuple(element.split(',')) for element in dest]
            dest = [tuple(map(int, tup)) for tup in dest]
            adjList[source] = dest
            
def main():
    buildGraphFromInput()
    


if __name__ == '__main__':
    main()
