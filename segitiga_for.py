"""
{
    Author : Bima Derian Al-Bachry,
    Kelas : 02TPLP004,
},{
    Semester : 002,
    Fakultas : Ilmu Komputer,
    Jurusan : Teknik Informatika,
}
"""

# Membuat segitiga dengan for loop
def satu():
    alas = int(input('Masukan Alas :'))
    for i in range(0, alas):
        for j in range(0, i + 1):
            print('* ' , end='')
        print('')
    

def dua():
    alas = int(input('Masukan Alas :'))
    for i in range(0, alas):
        for j in range(0, alas - 1):
            print('* ' , end='')
        alas -= 1
        print('')
    

def tiga():
    alas = int(input('Masukan Alas :'))
    sisi = 2 * alas - 2 # for spaces
    for i in range(0, alas):
        for j in range(0, sisi):
            print(' ',end='')
        sisi -= 2
        for j in range(0, i + 1):
            print('* ', end='')
        print('')
    

def empat():
    alas = int(input('Masukan Alas :'))
    sisi = 0 # for spaces
    for i in range(0, alas):
        for j in range(0, sisi):
            # print(j, end='')
            print(' ',end='')
        sisi += 2
        for j in range(0, alas):
            print('* ' , end='')
        alas -= 1
        print('')
    

def lima():
    alas = int(input('Masukan Alas :'))
    sisi = alas - 1 # for spaces
    for i in range(0, alas):
        for j in range(0, sisi):
            print(' ', end='')
        sisi -= 1
        for j in range(0, i + 1):
            print('* ', end='')
    
        print('')
    

def enam():
    alas = int(input('Masukan Alas :'))
    sisi = 0 # for spaces
    for i in range(0, alas):
        for j in range(0, sisi):
            print(' ',end='')
        sisi += 1
        for j in range(0, alas):
            print('* ' , end='')
        alas -= 1
        print('')
      
# execute program
satu()
dua()
tiga()
empat()
lima()
enam()