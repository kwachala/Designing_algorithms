from z2 import *
import matplotlib.pyplot as plt


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(arr:list, low, high):
    if len(arr) == 1:
        return output
    if low < high:
        print(arr, ',')
        #show_robots(create_vec_from_z(vec, arr))
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1,)
        quickSort(arr, pi + 1, high,)
    return arr

def bubble_sort(list):
    n = len(list)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                print(list, ',')
                #show_robots(create_vec_from_z(vec, list))
    return list

def create_vec_from_z(vec, zasieg):
    vec_sorted = []
    for z in zasieg:
        for robot in vec:
            if robot.zasieg == z:
                vec_sorted.append(robot)
                break
    return vec_sorted

vec = multiple_robots(10)
def show_QS(vec):
    zasieg = get_zasieg(vec)
    steps = quickSort(zasieg, 0, len(zasieg)-1)
    print(steps)
    #vec = create_vec_from_z(vec, zasieg)

def show_bubble(vec):
    zasieg = get_zasieg(vec)
    print(bubble_sort(zasieg))

print('Quick sort: ')
show_QS(vec)
print(200*'-', 15*'\n' ,'Bubble sort:')
show_bubble(vec)




steps = [[847, 930, 602, 584, 672, 811, 475, 667, 780, 635] ,
[602, 584, 475, 635, 672, 811, 847, 667, 780, 930] ,
[475, 584, 602, 635, 672, 811, 847, 667, 780, 930] ,
[475, 584, 602, 635, 672, 811, 847, 667, 780, 930] ,
[475, 584, 602, 635, 672, 811, 847, 667, 780, 930] ,
[475, 584, 602, 635, 672, 667, 780, 811, 847, 930] ,
[475, 584, 602, 635, 667, 672, 780, 811, 847, 930] ,
[475, 584, 602, 635, 667, 672, 780, 811, 847, 930]]
x = [1, 2, 3, 4, 5, 6, 7, 8]
steps_b = [[847, 602, 930, 584, 672, 811, 475, 667, 780, 635] ,
[847, 602, 584, 930, 672, 811, 475, 667, 780, 635] ,
[847, 602, 584, 672, 930, 811, 475, 667, 780, 635] ,
[847, 602, 584, 672, 811, 930, 475, 667, 780, 635] ,
[847, 602, 584, 672, 811, 475, 930, 667, 780, 635] ,
[847, 602, 584, 672, 811, 475, 667, 930, 780, 635] ,
[847, 602, 584, 672, 811, 475, 667, 780, 930, 635] ,
[847, 602, 584, 672, 811, 475, 667, 780, 635, 930] ,
[602, 847, 584, 672, 811, 475, 667, 780, 635, 930] ,
[602, 584, 847, 672, 811, 475, 667, 780, 635, 930] ,
[602, 584, 672, 847, 811, 475, 667, 780, 635, 930] ,
[602, 584, 672, 811, 847, 475, 667, 780, 635, 930] ,
[602, 584, 672, 811, 475, 847, 667, 780, 635, 930] ,
[602, 584, 672, 811, 475, 667, 847, 780, 635, 930] ,
[602, 584, 672, 811, 475, 667, 780, 847, 635, 930] ,
[602, 584, 672, 811, 475, 667, 780, 635, 847, 930] ,
[584, 602, 672, 811, 475, 667, 780, 635, 847, 930] ,
[584, 602, 672, 475, 811, 667, 780, 635, 847, 930] ,
[584, 602, 672, 475, 667, 811, 780, 635, 847, 930] ,
[584, 602, 672, 475, 667, 780, 811, 635, 847, 930] ,
[584, 602, 672, 475, 667, 780, 635, 811, 847, 930] ,
[584, 602, 475, 672, 667, 780, 635, 811, 847, 930] ,
[584, 602, 475, 667, 672, 780, 635, 811, 847, 930] ,
[584, 602, 475, 667, 672, 635, 780, 811, 847, 930] ,
[584, 475, 602, 667, 672, 635, 780, 811, 847, 930] ,
[584, 475, 602, 667, 635, 672, 780, 811, 847, 930] ,
[475, 584, 602, 667, 635, 672, 780, 811, 847, 930] ,
[475, 584, 602, 635, 667, 672, 780, 811, 847, 930] ,
[475, 584, 602, 635, 667, 672, 780, 811, 847, 930]
]

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15, 16, 17, 18, 19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

fig, axes = plt.subplots(2)
axes[0].plot(x, steps, label= "Quick_sort")
plt.suptitle("Quick_sort")
axes[1].plot(x1, steps_b, label = "Bubble_sort")
plt.show()