# Python akan mengeksekusi file ini berutut-turut dari atas ke bawah
print('Hallo')

print('Dunia')

print('!')

# Pernyataan/Statement
#statement adalah instruksi yang dapat dieksekusi oleh Python
#contoh statement 
x = 10
# atau 
if x > 5:
    print('x lebih besar dari 5')
# atau 
for i in range(5):
    print(i)

# Identation
# identation adalah tentang penataan baris baris kode program yang mengatur
# bagian mana yang menjorok ke dalam (indent) dan bagian mana yang tidak
# contoh identtation
def salampagi (nama):
    print("Selamat pagi",  nama)
    print("Semoga harimu menyenangkan")
    
salampagi("Andi")
# pada contoh diatas, baris kedua dan ketiga menjorok ke dalam (indent) 
# karena merupakan bagian dari fungsi salampagi

# tipe data python
# tipe data adalah jenis data yang bisa disimpan kedalam sebuah variabel \
# tiope data di python antara lain:
# tipe data numerik (int, float, complex)

a = 10
b = 10.5
c = 3+4j
#type berfungsi untuk mengetahui tipe data dari sebuah variabel
print(type(a))
print(type(b))
print(type(c))

# memunculkan nilai variabel
print(a)
print(b)
print(c)

# Tipe data string (str)
s = "Halo Dunia"
print(type(s))
print(s)

# Tipe data boolean (bool)
benar = True
salah = False
print(type(benar))
print(type(salah))
print(benar)
print(salah)

# Tipe data list
mylist = [1, 2, 3, 4, 5]
print(type(mylist))
print(mylist)

# Tipe data tuple
mytuple = (1, 2, 3, 4, 5)
print(type(mytuple))
print(mytuple)

# Tipe data dictionary
mydict = {'nama': 'Andi', 'umur': 25}
print(type(mydict))
print(mydict)

# Tipe data set
myset = {1, 2, 3, 4, 5}
print(type(myset))
print(myset)

# Tipe data None
x = None
print(type(x))
print(x)

# tipe data bytes
mybytes = b'Hello'
print(type(mybytes))
print(mybytes)

# tipe data bytearray
mybytearray = bytearray(5)
print(type(mybytearray))
print(mybytearray)

# tipe data range
myrange = range(5)
print(type(myrange))
print(myrange)
print(list(myrange))  # mengubah range menjadi list untuk ditampilkan

# Assignment
# Assignment adalah proses pemberian nilai pada variabel
# contoh assignment
print("Selamat datang !")
nama = input("Masukkan nama Anda: ")  # input() digunakan untuk mengambil input dari user
print("Halo,", nama)

angka = 123
idle = "integrated development and learning environment"
jumlah = angka + 100
print(angka)
print(idle)
print(jumlah)

# contoh assignment dengan operator
print("Selamat datang !")
nama = input("Masukkan nama Anda: ")
print("Halo, " + nama + "!")  # menggabungkan string dengan operator
a = 1
a = a + 1
a = a * 2
print(a)

#assignment dengan multiple assignment
# multiple assignment adalah proses pemberian nilai pada beberapa variabel sekaligus
# contoh multiple assignment
a = b = c = 10
print(a)
print(b)
print(c) 
# jika ingin memberikan nilai yang berbeda pada setiap variabel
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
# atau
nama, umur, tinggi = "Andi", 25, 175
print(nama)
print(umur)
print(tinggi)

# Mengubah tipe data operator 
usia = 10
print(usia)
# akan menghasilkan output dalam bentuk angka 10

usia = "sepuluh"
print (usia)
# akan menghasilkan output dalam bentuk string sepuluh
