# Membuat segitiga dengan for loop
def satu():
    alas = int(input('Masukan Alas :'))
    for i in range(0, a):
        for j in range(0, i + 1):
            print('* ' , end='')
        print('')
    

def dua():
    alas = int(input('Masukan Alas :'))
    for i in range(0, a):
        for j in range(0, a - 1):
            print('* ' , end='')
        a -= 1
        print('')
    

def tiga():
    alas = int(input('Masukan Alas :'))
    s = 2 * a - 2 # for spaces
    for i in range(0, a):
        for j in range(0, s):
            print(' ',end='')
        s -= 2
        for j in range(0, i + 1):
            print('* ', end='')
        print('')
    

def empat():
    alas = int(input('Masukan Alas :'))
    s = 0 # for spaces
    for i in range(0, a):
        for j in range(0, s):
            # print(j, end='')
            print(' ',end='')
        s += 2
        for j in range(0, a):
            print('* ' , end='')
        a -= 1
        print('')
    

def lima():
    alas = int(input('Masukan Alas :'))
    s = a - 1 # for spaces
    for i in range(0, a):
        for j in range(0, s):
            print(' ', end='')
        s -= 1
        for j in range(0, i + 1):
            print('* ', end='')
    
        print('')
    

def enam():
    alas = int(input('Masukan Alas :'))
    s = 0 # for spaces
    for i in range(0, a):
        for j in range(0, s):
            print(' ',end='')
        s += 1
        for j in range(0, a):
            print('* ' , end='')
        a -= 1
        print('')