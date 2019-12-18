mylist = []

def main():
    with open('MedianSmall.txt') as inputfile:
        sum = 0
        for line in inputfile:
            num = int(line)
            mylist.append(num)
            mylist.sort()
            if(len(mylist) % 2 == 0):
                sum += mylist[len(mylist)//2]
            elif(len(mylist) > 1):
                sum += mylist[(len(mylist) + 1) // 2]
            else:
                print('jejej')
                sum += mylist[0]
            print(mylist)
    print(sum % 10000)

main()
