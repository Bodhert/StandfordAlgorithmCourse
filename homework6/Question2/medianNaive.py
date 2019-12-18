mylist = []

def main():
    with open('Median.txt') as inputfile:
        sum = 0
        for line in inputfile:
            num = int(line)
            mylist.append(num)
            mylist.sort()
            sum += mylist[len(mylist)//2]
    print(sum % 10000)

main()
