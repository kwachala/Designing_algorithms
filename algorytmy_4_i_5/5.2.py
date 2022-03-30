from main import *
from z2 import *

def minmax(vec):
    min = vec[0]
    max = vec[0]
    for i in vec:
        if i > max:
            max = i
        if i < min:
            min = i
    array = []
    array.append(min)
    array.append(max)
    return array

def sort(robots):
    vec = get_rozdzielczosc(robots)
    n = len(vec)
    print('------------------------------------------------')
    print('Wartosci rozdzielczosci:')
    print(vec)
    print('------------------------------------------------')
    min_max = minmax(vec)
    min_vec = min_max[0]
    max_vec = min_max[1]
    print('1. Znalezlismy min i max: ')
    print('min = ' + str(min_vec))
    print('max = ' + str(max_vec))
    print('------------------------------------------------')
    size = max_vec - min_vec + 1
    print('2. Znalezlismy dlugosc nowej tablicy do zliczania: ' + str(size))
    print('------------------------------------------------')
    counters = [0] * size

    for x in range(n):
        counters[vec[x] - min_vec] += 1

    lastIndex = 0
    count = min_vec
    print('3. Moment zliczania wystapien liczb')
    print('------------------------------------------------')
    new_robots = multiple_robots(len(vec))
    robot_counter = 0
    for x in range(size):
        counter = 0
        print('Liczymy ilosc wystapien ' + str(count))
        y = lastIndex
        while y < counters[x] + lastIndex:
            counter += 1
            print(str(count) + ' wystapilo ' + str(counter) + ' raz(y)')
            vec[y] = x + min_vec
            for i in range(len(vec)):
                if robots[i].rozdzielczosc == vec[y]:
                    tmp = 0
                    for j in range(len(vec)):
                        if robots[i] != new_robots[j]:
                            tmp += 1
                            if tmp == len(vec):
                                new_robots[robot_counter] = robots[i]
                                robot_counter += 1
            y += 1
        lastIndex = y
        count += 1



    print('------------------------------------------------')
    return vec, new_robots

vec = multiple_robots(10)

print('Roboty:')
show_robots(vec)

sorted_rozdzialka, sorted_robots = sort(vec)

print('Posortowane wartosci rozdzielczosci:')
print(sorted_rozdzialka)
print('------------------------------------------------')

print('Poczatkowa kolejnosc robotow:')
show_robots(vec)
print('------------------------------------------------')
print('Kolejnosc robotow po posortowaniu wzgledem rozdzielczosci:')
show_robots(sorted_robots)

print('------------------------------------------------')
