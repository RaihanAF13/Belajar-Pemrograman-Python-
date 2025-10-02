# soal no 1 fungsi
def salam(nama):
      print("Assalamualaikum", nama)
      print("Semoga harimu menyenangkan")
salam("Raihan")

# soal no 2 variabel dan tipe data
a = 10
b = 20.5
c = 3+4j
print(type(a))
print(type(b))
print(type(c))

# soal no 3 multiple assignment
nama, umur, hobi = "Raihan", 21, "Membaca"
print(nama)
print(umur)
print(hobi)

# soal no 4 input dan output
nama=input("Masukkan nama Anda: ")
umur=int(input("Masukkan umur Anda: "))
hobi=input("Masukkan hobi Anda: ")
print("Nama saya adalah", nama,", umur saya", umur, "tahun dan hobi saya adalah", hobi)

# soal no 5 menukar tipe data
a= 5
b= 10
c = 15
a, b, c = c, a, b
print(a)
print(b)
print(c)

# soal no 6 Formatting
print("Saya suka belajar Python karena {}" .format("mudah dipelajari"))

# soal no 7 mengubah tipe data
angka_strng = "1000"
angka_strng = int(angka_strng)
hasil = angka_strng + 500
print(hasil)

# soal no 8 konstanta
PI = 3.14
GRAVITY = 9.8
SPEED_OF_LIGHT = 299792458
PLANCK_CONSTANT = 6.626e-34   # ditambahkan

print("PI =", PI)
print("GRAVITY =", GRAVITY)
print("SPEED_OF_LIGHT =", SPEED_OF_LIGHT)
print("PLANCK_CONSTANT =", PLANCK_CONSTANT)
