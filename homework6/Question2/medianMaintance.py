import heapq

minHeap = []
maxHeap = []

def rebalance():
    if(len(minHeap) > len(maxHeap) + 1 ):
        num = abs(heapq.heappop(minHeap))
        heapq.heappush(maxHeap, num)
    elif(len(maxHeap) > len(minHeap) + 1):
        num = heapq.heappop(maxHeap)
        heapq.heappush(minHeap, num)

def main():
    with open('Median.txt') as inputfile:
        num = int(inputfile.readline()) # dont know if I need to calculate when I only have one element
        heapq.heappush(minHeap, -num)
        round = 1
        sum = num

        for line in inputfile:
            num = int(line)
            if (num < abs(minHeap[0])): 
                heapq.heappush(minHeap, -num)
            elif(maxHeap and (num > maxHeap[0])):
               heapq.heappush(maxHeap, num) 
            elif(len(maxHeap) > len(minHeap)):
                heapq.heappush(minHeap, -num)
            else:
                 #dont forget to balanceate the heaps
               heapq.heappush(maxHeap, num) 

            round += 1
            if (round % 2 == 0):
                rebalance()
                sum += abs(minHeap[0])
            else:
                if(len(minHeap) > len(maxHeap)):
                    sum += abs(minHeap[0])
                else:
                    sum += maxHeap[0]

    print(sum % 10000)
    print(len(minHeap), len(maxHeap))

main()

# tested answer 1414, 5083
