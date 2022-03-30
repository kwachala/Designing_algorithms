from main import *

i = []
t = ['AUV', 'AFV']
m = [51, 52, 53]
z = []
r = []


def find_robot(vector):
    tmp2 = 0
    wanted_robot = robot(i, t, m, z, r)
    for k in range(len(vector)):
        tmp = 0
        if len(i) == 0:
            tmp += 1
        else:
            for j in range(len(i)):
                if vector[k].identyfikator == wanted_robot.identyfikator[j]:
                    tmp += 1
        if len(t) == 0:
            tmp += 1
        else:
            for j in range(len(t)):
                if vector[k].typ == wanted_robot.typ[j]:
                    tmp += 1
        if len(m) == 0:
            tmp += 1
        else:
            for j in range(len(m)):
                if vector[k].masa == wanted_robot.masa[j]:
                    tmp += 1
        if len(z) == 0:
            tmp += 1
        else:
            for j in range(len(z)):
                if vector[k].zasieg == wanted_robot.zasieg[j]:
                    tmp += 1
        if len(r) == 0:
            tmp += 1
        else:
            for j in range(len(r)):
                if vector[k].rozdzielczosc == wanted_robot.rozdzielczosc[j]:
                    tmp += 1

        print('Aktualny robot:', vector[k].identyfikator, vector[k].typ, vector[k].masa, vector[k].zasieg,
              vector[k].rozdzielczosc)
        print('Szukane parametry w robocie: ', wanted_robot.identyfikator, wanted_robot.typ, wanted_robot.masa,
              wanted_robot.zasieg, wanted_robot.rozdzielczosc)

        if tmp == 5:
            print('Robot znaleziony na pozycji ' + str(k + 1))
            tmp2 = "Znaleziono"
        if tmp2 == "Znaleziono":
            return vector[k]


vec = multiple_robots(15)
find_robot(vec)
