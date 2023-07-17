def Insert(sorted, value):
    i = 0
    if len(sorted) == 0 or value < sorted[0]:
        sorted.insert(0, value)
        return

    while i < len(sorted) and value > sorted[i]:
        i = i + 1

    sorted.insert(i, value)


def InsertionSort(input):
    sorted = []

    for i in range(len(input)):
        Insert(sorted, input[i])

    return sorted
