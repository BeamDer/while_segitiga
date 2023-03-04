# segitiga dengan while loop
def satu():
    string = ""
    bar = 1

    x = int(input("Masukkan angka :"))

    # Looping Baris
    while bar <= x:
        kol = bar

        # Looping Kolom
        while kol > 0:
            string = string + " * "
            kol = kol - 1
            
        string = string + "\n"
        bar = bar + 1
    print (string)
    
def dua():
    string = ""

    bar = int(input("Masukkan angka :"))

    #Looping Baris
    while bar >= 0:
        kol = bar

        # Looping Kolom
        while kol > 0:
            string = string + " * "
            kol = kol - 1
            
        string = string + "\n"
        bar = bar - 1
        
    print (string)
    
def tiga():
    string = ""

    x = int(input("Masukkan angka :"))
    bar = x
    # Looping Baris
    while bar >= 0:

        # Looping Kolom Spasi Kosong
        kol = bar
        while kol > 0:
            string = string + "   "
            kol = kol - 1
        
        # Looping Kolom Bintang	
        kanan = 1
        while kanan < (x - (bar-1)):
            string = string + " * "
            kanan = kanan + 1		
            
        string = string + "\n"
        bar = bar - 1
        
    print (string)
    
def empat():
    string = ""
    bar = 1

    x = int(input("Masukkan angka :"))

    # Looping Baris
    while bar <= x:
        # Looping Kolom Spasi Kosong
        kol = bar	
        while kol > 1:
            string = string + "   "
            kol = kol - 1
        
        # Looping Kolom Bintang	
        kanan = 0
        while kanan <= (x - bar):
            string = string + " * "
            kanan = kanan + 1	
            
        string = string + "\n"
        bar = bar + 1
    print (string)
    
def lima():
    string = ""

    x = int(input("Masukkan angka :"))
    bar = x
    # Looping Baris
    while bar >= 0:
        # Looping Kolom Spasi Kosong
        kol = bar
        while kol > 0:
            string = string + "   "
            kol = kol - 1
        # Looping Kolom Bintang Sisi Kiri	
        kiri = 1
        while kiri < (x - (bar-1)):
            string = string + " * "
            kiri = kiri + 1		
        # Looping Kolom Bintang Sisi Kanan
        kanan = 1
        while kanan < kiri -1:
            string = string + " * "
            kanan = kanan + 1	

        string = string + "\n\n"
        bar = bar - 1
        
    print (string)
    
def enam():
    string = ""
    bar = 1

    x = int(input("Masukkan angka :"))
    print ("\n")
    # Looping Baris
    while bar <= x:
        kol = bar
        # Looping Kolom Spasi Kosong
        while kol > 1:
            string = string + "   "
            kol = kol - 1
        # Looping Kolom Bintang Sisi Kiri	
        kiri = 0
        while kiri <= (x - bar):
            string = string + " * "
            kiri = kiri + 1	
        # Looping Kolom Bintang Sisi Kanan
        kanan = kiri	
        while kanan > 1:
            string = string + " * "
            kanan = kanan - 1

        string = string + "\n\n"
        bar = bar + 1
    print (string)
    
def tujuh():
    string = ""

    x = int(input("Masukkan angka :"))
    bar = x
    # Looping Baris
    while bar >= 0:
        # Looping Kolom Spasi Kosong
        kol = bar
        while kol > 0:
            string = string + "   "
            kol = kol - 1
        # Looping Kolom Bintang Sisi Kiri		
        kiri = 1
        while kiri < (x - (bar-1)):
            string = string + " * "
            kiri = kiri + 1		
        # Looping Kolom Bintang Sisi Kanan
        kanan = 1
        while kanan < kiri -1:
            string = string + " * "
            kanan = kanan + 1	

        string = string + "\n\n"
        bar = bar - 1

    bar = 1	
    # Looping Baris
    while bar <= x:
        kol = bar+1
        # Looping Kolom Spasi Kosong
        while kol > 1:
            string = string + "   "
            kol = kol - 1
        # Looping Kolom Bintang Sisi Kiri	
        kiri = 0
        while kiri < (x - bar):
            string = string + " * "
            kiri = kiri + 1	
        # Looping Kolom Bintang Sisi Kanan
        kanan = kiri	
        while kanan > 1:
            string = string + " * "
            kanan = kanan - 1

        string = string + "\n\n"
        bar = bar + 1
    print (string)
    
def delapan():
    string = ""
    bar = 1

    x = int(input("Masukkan angka :"))
    print ("\n")
    # Looping Baris
    while bar < x:
        # Looping Kolom Spasi Kosong
        kol = bar
        while kol > 1:
            string = string + "   "
            kol = kol - 1
        # Looping Kolom Bintang Sisi Kiri
        kiri = 0
        while kiri <= (x - bar):
            string = string + " * "
            kiri = kiri + 1	
        # Looping Kolom Bintang Sisi Kanan
        kanan = kiri	
        while kanan > 1:
            string = string + " * "
            kanan = kanan - 1

        if (bar+1) <= x:
            string = string + "\n\n"
        bar = bar + 1

    bar = x-1	
    # Looping Baris
    while bar >= 0:
        # Looping Kolom Spasi Kosong
        kol = bar
        while kol > 0:
            string = string + "   "
            kol = kol - 1
        # Looping Kolom Bintang Sisi Kiri	
        kiri = 1
        while kiri < (x - (bar-1)):
            string = string + " * "
            kiri = kiri + 1		
        # Looping Kolom Bintang Sisi Kanan
        kanan = 1
        while kanan < kiri -1:
            string = string + " * "
            kanan = kanan + 1	

        string = string + "\n\n"
        bar = bar - 1
    print (string)

satu()
dua()
tiga()
empat()
lima()
enam()
tujuh()
delapan()