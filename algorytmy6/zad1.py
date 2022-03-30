from random import randint

class priorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def __len__(self):
        return self.size

    def parent(self, index):
        if index <= 1 or index > self.size:
            return None
        else:
            return self.heap[index // 2 - 1]

    def leftChild(self, index):
        if index < 1 or 2 * index > self.size:
            return None
        else:
            return self.heap[index * 2 - 1]

    def rightChild(self, index):
        if index < 1 or 2 * index + 1 > self.size:
            return None
        else:
            return self.heap[index * 2]

    def swap(self, index1, index2):
        self.heap[index1 - 1], self.heap[index2 - 1] = self.heap[index2 - 1], self.heap[index1 - 1]

    def insert(self, x):
        self.size += 1
        self.heap.append(x)
        index = self.size
        while index > 1 and x > self.parent(index): # > na < dla min
            parentIndex = index // 2
            self.swap(index, parentIndex)
            index = parentIndex
        #print('Dodawanie elementu do kolejki')
        #print('Kopiec:')
        #print(self.heap)

    def deleteMax(self):
        if self.size <= 0:
            return None
        elif self.size == 1:
            self.size = 0
            return self.heap[0]
        maxint = self.heap[0]
        self.swap(1, self.size)
        self.heap.pop()
        self.size -= 1
        index = 1
        while True:
            if index * 2 + 1 > self.size and index * 2 > self.size:
                break
            elif index * 2 + 1 > self.size and index * 2 <= self.size:
                if self.size == 2 and self.heap[0] > self.heap[1]:
                    break
                self.swap(index, index * 2)
                index = index * 2
                break
            elif self.heap[index - 1] < self.leftChild(index) or self.heap[index - 1] < self.rightChild(index): # < na > do min
                if self.leftChild(index) > self.rightChild(index): # > na < do min
                    self.swap(index, index * 2)
                    index = index * 2
                else:
                    self.swap(index, index * 2 + 1)
                    index = index * 2 + 1
            else:
                break
        #print('Usuwanie maxa z kolejki')
        #print('Kopiec:')
        #print(self.heap)
        return maxint

    def showMax(self):
        if self.size <= 0:
            return None
        elif self.size == 1:
            self.size = 0
            return self.heap[0]
        maxint = self.heap[0]
        #print(maxint)

def create_non_sorted_array_queue(n):
    tab = []
    if n != 0:
        for i in range(n):
            argument = randint(0, 10)
            priority = randint(0, 5)
            tab2 = [argument, priority]
            tab.append(tab2)
        return tab
    else:
        return tab


def insert_to_nsq(tab, a, b):
    tab.append([a, b])
    print('Kolejka po dodaniu elementu:')
    print(tab)


def find_max_in_nsq(tab):
    max = tab[0][1]
    index = 0
    for i in range(len(tab)):
        if max < tab[i][1]:  # < na > do min
            max = tab[i][1]
            index = i
    print('Nasz max znajduje sie na ' + str(index + 1) + ' miejscu w kolejce:')
    print(tab[index])


def delete_max_in_nsq(tab):
    max = tab[0][1]
    index = 0
    for i in range(len(tab)):
        if max < tab[i][1]: # < na > do min
            max = tab[i][1]
            index = i
    print('Nasz max znajduje sie na ' + str(index + 1) + ' miejscu w kolejce:')
    print(tab[index])
    print('Usuwanie maxa z kolejki')
    tab.pop(index)
    print('Kolejka po usunieciu:')
    print(tab)


def create_sorted_array_queue(n):
    tab = []
    if n != 0:
        for i in range(n):
            argument = randint(0, 10)
            priority = randint(0, 5)
            tab2 = [argument, priority]
            tab.append(tab2)
        for i in range(1, len(tab)):
            key = tab[i][1]
            keyel = tab[i]
            j = i - 1
            while j >= 0 and tab[j][1] < key:
                tab[j + 1] = tab[j]
                j = j - 1
            tab[j + 1] = keyel
        return tab
    else:
        return tab


def insert_to_sq(tab, a, b):
    tab.append([a, b])
    for i in range(1, len(tab)):
        key = tab[i][1]
        keyel = tab[i]
        j = i - 1
        while j >= 0 and tab[j][1] < key:
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j + 1] = keyel
    print('Kolejka po dodaniu elementu:')
    print(tab)


def find_max_in_sq(tab):
    print('Nasz max znajduje sie na 1 miejscu w kolejce:') #ostatnim w min
    print(tab[0])   #tab[0] na tab[len(tab)-1] w min


def delete_max_in_sq(tab):
    print('Nasz max znajduje sie na 1 miejscu w kolejce:') #ostatnim w min
    print(tab[0])           #na len(tab)-1 w min
    print('Usuwanie maxa z kolejki')
    #xD = len(tab)-1            #w min
    tab.pop(0)                 #tab.pop(0) na tab.pop(xD) w min
    print('Kolejka po usunieciu:')
    print(tab)



if __name__ == '__main__':
    print('Wybierz rodzaj kolejki:')
    print('Tablica nieposortowana            -  [1]')
    print('Tablica posortowana               -  [2]')
    print('Z wykorzystaniem kopca binarnego  -  [3]')
    x = int(input())
    if x == 1:
        print('Podaj ilosc losowych elementow w kolejce, jesli kolejka ma byc pusta wpisz 0:')
        x = int(input())
        tab = create_non_sorted_array_queue(x)
        print('Kolejka:')
        print(tab)
        while True:
            print('Co chcesz zrobic?')
            print('Dodaj element do kolejki      -  [1]')
            print('Wyswietl max kolejki          -  [2]')
            print('Usun max z kolejki            -  [3]')
            print('Przerwij działanie kolejki    -  [4]')
            x = int(input())
            if x == 1:
                print('Podaj element a nastepnie jego priorytet:')
                el = int(input())
                pr = int(input())
                insert_to_nsq(tab, el, pr)
            elif x == 2:
                find_max_in_nsq(tab)
            elif x == 3:
                delete_max_in_nsq(tab)
            elif x == 4:
                break
    if x == 2:
        print('Podaj ilosc losowych elementow w kolejce, jesli kolejka ma byc pusta wpisz 0:')
        x = int(input())
        tab = create_sorted_array_queue(x)
        print('Kolejka:')
        print(tab)
        while True:
            print('Co chcesz zrobic?')
            print('Dodaj element do kolejki      -  [1]')
            print('Wyswietl max kolejki          -  [2]')
            print('Usun max z kolejki            -  [3]')
            print('Przerwij działanie kolejki    -  [4]')
            x = int(input())
            if x == 1:
                print('Podaj element a nastepnie jego priorytet:')
                el = int(input())
                pr = int(input())
                insert_to_sq(tab, el, pr)
            elif x == 2:
                find_max_in_sq(tab)
            elif x == 3:
                delete_max_in_sq(tab)
            elif x == 4:
                break
    if x == 3:
        heap = priorityQueue()
        print('Podaj ilosc losowych elementow w kolejce, jesli kolejka ma byc pusta wpisz 0:')
        x = int(input())
        if x != 0:
            for i in range(x):
                heap.insert(randint(0,10))
        else:
            heap = priorityQueue()
        print('Kolejka:')
        print(set(heap.heap[0:heap.size]))
        while True:
            print('Co chcesz zrobic?')
            print('Dodaj element do kolejki      -  [1]')
            print('Wyswietl max kolejki          -  [2]')
            print('Usun max z kolejki            -  [3]')
            print('Przerwij działanie kolejki    -  [4]')
            x = int(input())
            if x == 1:
                print('Podaj priorytet:')
                pr = int(input())
                heap.insert(pr)
                print(set(heap.heap[0:heap.size]))
            elif x == 2:
                print('Nasz max:')
                heap.showMax()
            elif x == 3:
                heap.deleteMax()
                print('Kolejka po usunieciu:')
                print(set(heap.heap[0:heap.size]))
            elif x == 4:
                break

