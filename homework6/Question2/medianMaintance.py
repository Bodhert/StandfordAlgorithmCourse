import heapq

minHeap = []
maxHeap = []

def main():
    with open('Median.txt') as inputfile:
        num = int(inputfile.readline()) # dont know if I need to calculate when I only have one element
        heapq.heappush(minHeap, -num)

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

    print(len(maxHeap), len(minHeap))

main()
