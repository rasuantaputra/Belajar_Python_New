a = float(input('Masukan angka ke-1 = '))
b = float(input('Masukan angka ke-2 = '))


def pilih():
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


def jumlah(a, b):
    return print('Hasilnya adalah : ', a + b)


def kurang(a, b):
    return print('Hasilnya adalah : ', a - b)


def kali(a, b):
    return print('Hasilnya adalah : ', a * b)


def bagi(a, b):
    return print('Hasilnya adalah : ', a / b)


def pangkat(a, b):
    return print('Hasilnya adalah : ', a ** b)


def modula(a, b):
    return print('Hasilnya adalah : ', a % b)


def floorDevision(a, b):
    return print('Hasilnya adalah : ', a // b)


def prioritasOperasi(a, b, c):
    return print('Hasilnya adalah : ', a ** b * c + a / b - b % c // a)


while True:
    pilihan = int(input('Pilih nomor berapa ? : '))

    if (pilihan in range(1, 9)):
        if (pilihan == 1):
            jumlah(a, b)
            break
        elif (pilihan == 2):
            kurang(a, b)
            break
        elif (pilihan == 3):
            kali(a, b)
            break
        elif (pilihan == 4):
            bagi(a, b)
            break
        elif (pilihan == 5):
            pangkat(a, b)
            break
        elif (pilihan == 6):
            modula(a, b)
            break
        elif (pilihan == 7):
            floorDevision(a, b)
            break
        else:
            print('PILIH YANG BENER !!!')

# ===Keterangan Prioritas Operasi ===
"""
Prioritas operasi sama dengan pengoprasian di dunia nyata 

urutannya gini :
1. () => yg ada kurungnya
2. exponen
3. Perkalian / pembagian
4. Penjumlahan / Pengurangan
"""
