def maxIndex(list):
    maxIndex = 0
    for i in range(len(list)):
        if (list[i] > list[maxIndex]):
            maxIndex = i
    return maxIndex