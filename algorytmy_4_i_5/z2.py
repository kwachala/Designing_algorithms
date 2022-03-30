from main import *
import operator


def robot_sort_masa(vec):
    vec.sort(key=operator.attrgetter('masa'))
    return vec


def robot_sort_zasieg(vec):
    vec.sort(key=operator.attrgetter('zasieg'))
    return vec


def robot_sort_rozdzielczosc(vec):
    vec.sort(key=operator.attrgetter('rozdzielczosc'))
    return vec



def get_masa(vec):
    tmp = []
    for i in range(len(vec)):
        tmp.append(vec[i].masa)
    return tmp


def get_zasieg(vec):
    tmp = []
    for i in range(len(vec)):
        tmp.append(vec[i].zasieg)
    return tmp


def get_rozdzielczosc(vec):
    tmp = []
    for i in range(len(vec)):
        tmp.append(vec[i].rozdzielczosc)
    return tmp


def find_robot_bin(arr, low, high, x, i):
    if high >= low:
        print('Aktualna ilosc wykonania funkcji dla danego parametru z listy: ' + str(i))
        mid = (high + low) // 2
        if arr[mid] == x:
            i += 1
            return mid
        elif arr[mid] > x:
            i += 1
            return find_robot_bin(arr, low, mid - 1, x, i)
        else:
            i += 1
            return find_robot_bin(arr, mid + 1, high, x, i)

def printing(a):
    if a == None:
        print('-------------------')
        print("Nie znaleziono elementu dla podanych parametrów")
    else:
        print('-------------------')
        print('Pierwszy znaleziony robot: ')
        print(vec[a].identyfikator, vec[a].typ, vec[a].masa, vec[a].zasieg, vec[a].rozdzielczosc)

def binary_zasieg(vec):
    robot_sort_zasieg(vec)
    print('-------------------')
    show_robots(vec)
    arr = get_zasieg(vec)
    print('-------------------')
    for i in range(len(x)):
        print('Aktualny parametr: ' + str(x[i]))
        a = find_robot_bin(arr, 0, len(arr) - 1, x[i], 1)
        if a != None:
            break
    printing(a)

def binary_masa(vec):
    robot_sort_masa(vec)
    print('-------------------')
    show_robots(vec)
    arr = get_masa(vec)
    print('-------------------')
    for i in range(len(x)):
        print('Aktualny parametr: ' + str(x[i]))
        a = find_robot_bin(arr, 0, len(arr) - 1, x[i], 1)
        if a != None:
            break
    printing(a)

def binary_rozdzielczosc(vec):
    robot_sort_rozdzielczosc(vec)
    print('-------------------')
    show_robots(vec)
    arr = get_rozdzielczosc(vec)
    print('-------------------')
    for i in range(len(x)):
        print('Aktualny parametr: ' + str(x[i]))
        a = find_robot_bin(arr, 0, len(arr) - 1, x[i], 1)
        if a != None:
            break
    printing(a)



#vec = multiple_robots(5)
#show_robots(vec)
#x = [8, 2]

#binary_zasieg(vec)
#binary_masa(vec)
#binary_rozdzielczosc(vec)
