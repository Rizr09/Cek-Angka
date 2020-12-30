# Masukkan angka
angka = int(input("Masukkan angka "))

# Cek angka 1
if angka % 2 == 0 and angka != 0:
    print(angka, "angka genap")
elif angka % 2 != 0:
    print(angka, "angka ganjil")
else:
    print("nol")
# Cek angka 2
if angka < 0:
    print(angka, "angka negatif")
elif angka == 0:
    print()
else:
    print(angka, "angka positif")
# Cek angka 3
if angka > 1:
    for i in range(2, angka):
        if (angka % i) == 0:
            print(angka, "bukan prima")
            break
    else:
        print(angka, "angka prima")
else:
    print(angka, "bukan prima")
