import random

# Menentukan angka rahasia
angka_rahasia = random.randint(1, 100)

tebakan = 0

while tebakan != angka_rahasia:
  # Menanyakan tebakan pengguna
  tebakan = int(input("Masukkan tebakan Anda (1-100): "))

  # Memberikan petunjuk
  if tebakan > angka_rahasia:
    print("Tebakan Anda terlalu tinggi!")
  elif tebakan < angka_rahasia:
    print("Tebakan Anda terlalu rendah!")
  else:
    print("Selamat! Anda berhasil menebak angkanya!")
