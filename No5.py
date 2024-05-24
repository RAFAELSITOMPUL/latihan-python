# Minta pengguna memasukkan angka
num = int(input("Masukkan angka: "))

# Inisialisasi variabel faktorial
faktorial = 1

# Periksa apakah angka adalah bilangan negatif, nol, atau positif
if num < 0:
    print("Maaf, faktorial tidak didefinisikan untuk bilangan negatif.")
elif num == 0:
    print("Faktorial dari 0 adalah 1")
else:
    # Hitung faktorial menggunakan for loop
    for i in range(1, num + 1):
        faktorial *= i

    # Cetak hasil faktorial
    print("Faktorial dari", num, "adalah", faktorial)
