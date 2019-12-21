import heapq

minHeap = []
maxHeap = []

def rebalance():
    if((len(minHeap) - len(maxHeap)) >= 2 ):
        num = abs(heapq.heappop(minHeap))
        heapq.heappush(maxHeap, num)
    elif((len(maxHeap) - len(minHeap)) >=  2):
        num = heapq.heappop(maxHeap)
        heapq.heappush(minHeap, -num)

def addNumber(num):
    if (len(minHeap) == 0 or num < abs(minHeap[0])):
        heapq.heappush(minHeap, -num)
    else:
        heapq.heappush(maxHeap, num)

def getMedian():
    biggerHeap = minHeap if (len(minHeap) > len(maxHeap)) else maxHeap
    smallerHeap = maxHeap if (len(minHeap) > len(maxHeap)) else minHeap

    if(len(biggerHeap) == len(smallerHeap)):
        return abs(smallerHeap[0])
    else:
        return abs(biggerHeap[0])

def main():
    sum = 0
    with open('Median.txt') as inputfile:
        num = int(inputfile.readline()) # dont know if I need to calculate when I only have one element
        for line in inputfile:
            num = int(line)
            addNumber(num)
            rebalance()
            sum += getMedian()

    print (sum)
    print(sum % 10000)
    print(len(minHeap), len(maxHeap))

main()

# tested answer 1414, 5083, 5129, 6596, 324, 4882
# hacer el naive aproach e ir comparando el resultado
