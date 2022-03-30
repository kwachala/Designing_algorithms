from math import isclose
#1
def rek_x(n):
    if n == 0:
        return 0
    else:
        return 3**n + rek_x(n-1)

#print(rek_x(2))

def ind_x(n):
    return 0.5*(2*0 + 3**(n+1) - 3)


def check_x(N):
    for n in range(1, N):
        if isclose(rek_x(n),ind_x(n)):
            print(rek_x(n), '  ', ind_x(n), '  ',True)
        else:
            print(rek_z(n), '  ', ind_z(n), '  ', False)

check_x(10)
#2

def rek_y(n):
    if n == -1 or n == 0:
        return 0
    else:
        return n + rek_y(n-2)

def ind_y(n):
    if n%2 == 0: # (n-1) = =2k+1
        return n + (n/2)*(n/2-1)
    else: #(n-1) = 2k
        return n + ((n-1)/2)**2


def check_y(N):
    for n in range(1, N):
        if isclose(rek_y(n),ind_y(n)):
            print(rek_y(n), '  ', ind_y(n), '  ',True)
        else:
            print(rek_y(n), '  ', ind_y(n), '  ',False)

check_y(10)
#3

def rek_z(n): #ciag Febinacciego
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return rek_z(n-1) + rek_z(n-2)


def ind_z(n):
    return (((1+5**0.5)/2)**n / 5**0.5) - (((1-5**0.5)/2)**n / 5**0.5)

#print(rek_z(n))
#print(ind_z(n))

def check_z(N):
    for n in range(1, N):
        if isclose(rek_z(n),ind_z(n)):
            print(rek_z(n), '  ', ind_z(n), '  ',True)
        else:
            print(rek_z(n), '  ', ind_z(n), '  ',False)

check_z(10)