a = float(input('Masukan angka ke-1 = '))
b = float(input('Masukan angka ke-2 = '))

def pilih() : 
    print('=== Pilih Operasi Aritmatika di Bawah ini : ===')
    print('1. Jumlah')
    print('2. Kurang')
    print('3. Kali')
    print('4. Bagi')
    print('5. Exponen (Pangkat)')
    print('6. Modula')
    print('7. Operasi Floor devision')
    print('8. Prioritas Operasi (urutan operasi => a ** b * c + a / b - b % c // a)')
    print('==================')


pilih()

def jumlah (a,b):
    return print('Hasilnya adalah : ' , a + b)

def kurang (a,b):
    return print('Hasilnya adalah : ' , a - b)

def kali (a,b):
    return print('Hasilnya adalah : ' , a * b)

def bagi (a,b):
    return print('Hasilnya adalah : ' , a / b)

def pangkat (a,b):
    return print('Hasilnya adalah : ' , a ** b)

def modula (a,b):
    return print('Hasilnya adalah : ' , a % b)

def floorDevision (a,b):
    return print('Hasilnya adalah : ' , a // b)

def prioritasOperasi (a,b,c):
    return print('Hasilnya adalah : ' , a ** b * c + a / b - b % c // a)

def operasiBilangan(pilihan):
    if pilihan is '1':
        jumlah(a,b)
    elif pilihan == '2':
        kurang(a,b)
    elif (pilihan is '3'):
        kali(a,b)
    elif (pilihan == '4'):
        bagi(a,b)
    elif pilihan is '5':
        pangkat(a,b)
    elif pilihan == '6':
        modula (a,b)
    elif pilihan == '7':
        floorDevision (a,b)
    elif pilihan == '8':
        c = float(input('Masukan angka ke-3 = '))
        prioritasOperasi (a,b,c)

    

pilihan = input('Pilih nomor berapa ? : ')



