from zad1 import *
import matplotlib.pyplot as plt


def heapSort(intList):
    out = []
    plotlist = []
    h = priorityQueue()
    for i in intList:
        h.insert(i)
        out.append(i)
    x = h.deleteMax()
    i = -1
    while x != None:
        out[i] = x
        x = h.deleteMax()
        i -= 1
        plotlist.append(out[:])
    return out, plotlist


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr: list, low, high, plotlist):
    if len(arr) == 1:
        return arr
    if low < high:
        plotlist.append(arr[:])
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1, plotlist)
        quickSort(arr, pi + 1, high, plotlist)

    return arr, plotlist


list = [847, 930, 602, 584, 642, 811, 475, 667, 780, 635]
plotlist = []

sorted1, plotlist1 = heapSort(list)
sorted2, plotlist2 = quickSort(list, 0, len(list) - 1, plotlist)

print(sorted1)
print(sorted2)

x1 = range(1, len(plotlist1) + 1)
x2 = range(1, len(plotlist2) + 1)

fig, axes = plt.subplots(2)
axes[0].plot(x1, plotlist1)
axes[0].set_title('Heapsort')
axes[1].plot(x2, plotlist2)
axes[1].set_title('Quicksort')
plt.show()

