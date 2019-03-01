
calls = 0
i = 1


def medianOfTheTree(nums, leftLimit, rightLimit):
    size = (rightLimit + leftLimit)
    print('left', 'rigth', 'size', leftLimit, rightLimit, size)
    midIndex = size // 2
    if size % 2 == 0:
        midIndex -= 1

    firstNum = nums[leftLimit]
    midNum = nums[midIndex]
    secondNum = nums[rightLimit-1]

    pivot = sorted([firstNum, midNum, secondNum])[1]

    index = -1

    if firstNum == pivot:
        index = leftLimit
    elif midNum == pivot:
        index = midIndex
    else:
        index = rightLimit-1

    nums[leftLimit], nums[index] = nums[index], nums[leftLimit]


def pivotPartition(nums, leftLimit, rightLimit):
    pivot = nums[leftLimit]
    pivotEndingLocation = leftLimit
    for i in range(leftLimit + 1, rightLimit):
        if nums[i] < pivot:
            pivotEndingLocation += 1
            nums[i], nums[pivotEndingLocation] = nums[pivotEndingLocation], nums[i]
    nums[pivotEndingLocation], nums[leftLimit] = pivot, nums[pivotEndingLocation]
    return pivotEndingLocation


def quickSort(nums, leftLimit, rightLimit):
    if rightLimit - leftLimit <= 1:
        return

    global calls
    calls += (rightLimit - leftLimit) - 1

    # nums[rightLimit-1],nums[leftLimit]  = nums[leftLimit],nums[rightLimit-1]
    medianOfTheTree(nums, leftLimit, rightLimit)     # for the second problem

    pivotPosition = pivotPartition(nums, leftLimit, rightLimit)
    quickSort(nums, leftLimit, pivotPosition)
    quickSort(nums, pivotPosition + 1, rightLimit)


def main():
    file = open('inVid.txt', 'r')
    nums = []
    for line in file.readlines():
        nums.append(int(line))
    quickSort(nums, 0, len(nums))

    global calls
    print(calls)

    file.close()


if __name__ == '__main__':
    main()
