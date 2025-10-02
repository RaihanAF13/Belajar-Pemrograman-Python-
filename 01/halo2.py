# Swap Variables
x = 10
y = 20

print (x)
# akan menghasilkan output dalam bentuk angka 10
print (y)
# akan menghasilkan output dalam bentuk angka 20
x, y = y, x
print (x)   
# akan menghasilkan output dalam bentuk angka 20
print (y)
# akan menghasilkan output dalam bentuk angka 10
# baris statement x, y, = y, x digunakan untuk menukar nilai variabel x dan y

x = 1000
print (x)

# print berfungsi untuk menampiljab nilai atau data yang tersimpan
# contoh print
print ("Helllo Nama saya Raihan")
print ('Helllo Nama saya Raihan')   

# Escape character
print ("Helllo Nama saya \"Raihan\"")
print ('Helllo Nama saya \'Raihan\'')
print ('Halo\nNama saya Raihan\nPanggil Aku Rehan')
print("\300[1;32;40m Tulisan Ini bewarnalho...]")
# \033 adalah style teks yang akan digunakan untuk menampilkan ANSI code
# 1 adalah style teks yang akan digunakan, 32 adalah teks warna hijau dan 40 adalah background warna hitam

# \' Tanda Kutip Tunggal
# \" Tanda Kutip Ganda
#\t Tab
#\n New Line
#\\ Gariss Miring
#\r Carriage Return
#\b Backspace
#\f Form Feed
#\ooo Octal value
#\xhh Hexadecimal value

# argument end
print ("Hello", end=" ")
print ("Raihan")
#  argument end pada print berfungsi untuk mengatur karakter yang akan ditampilkan di akhir output

# Raw string
# adalah string yang diawali dengan huruf r atau R sebelum tanda kutip pembuka
# pada raw string, karakter escape tidak akan diproses dan akan ditampilkan apa adanya
print (r'Halo\nNama saya Raihan\nPanggil Aku Rehan')

# tanda Kutip tiga
print ("""Halo Nama saya Raihan
Panggil Aku Rehan""")
# Tanda kutip tiga (""" atau ''') digunakan untuk membuat string lebih dari satu baris

# Menggunakan .format
# Formating string dengan metode .format() adalah cara untuk menyisipkan nilai ke dalam string dengan menggunakan placeholder {}
# Teknik ini didalam python sering disebut dengan istilah string interpolation, yaitu memasukkan variabel kedalam string
print ("Halo Nama saya {}. Saya berumur {} tahun".format("Raihan", 21))
print ("Halo Nama saya {0}. Saya berumur {1} tahun. {0} adalah nama saya".format("Raihan", 21))
print ("Halo Nama saya {nama}. Saya berumur {umur} tahun".format(nama="Raihan", umur=21))
print ("Hallo,  Nama saya  {0}. Apa kabar {1}!"
       .format("Raihan", "Teman-teman"))
print ( "Usia saya {1} dan kamu {0} " .format("21", 25))
# Format untuk menulis separator pada angka
txt = "Harganya Rp{:,} "
print (txt.format(1000000))

# Base 
angka_base = 0b100
print ("100 binary = ", angka_base)

angka_base = 0o100
print ("100 octal = ", angka_base)

angka_base = 0x100
print ("100 hexadecimal = ", angka_base)

# Bilangan pecahan atau float number
angka_float =255.0
print ("angka float yang akan ditulis langsung: ", angka_float)

angka_float =2.55e2
print ("angka float yang ditulis dengan scientific notation: ", angka_float)

angka_float = 2.55e-2
print ("angka float yang ditulis menggunakan pangkat negatif: ", angka_float)

# type conversion(Typecasting)
# mengubah tipe data dari satu tipe ke tipe lainnya misalnya dari integer ke string, dari float ke integer, dan sebagainya
# str(x) mengubah tipe data integer ke string
# int(x) mengubah tipe data string ke integer
# float(x) mengubah tipe data float ke menjadi string

# konversi tipe data dari integer ke string
x = 10
x_str = str(x)
print("nilai x =", x_str)
print("tipe data x =", type(x_str))

# Konversi tipe data dari string ke integer
y_str = "20"
y = int(y_str)
print("nilai y =", y)
print("tipe data y =", type(y))

# Konversi tipe data dari string ke float
z_str = "3.14"
z = float(z_str)
print("nilai z =", z)
print("tipe data z =", type(z))

# Konversi tipe data dari integer ke float
a = 100 
a_float = float(a)
print("nilai a =", a_float)
print("tipe data a =", type(a_float))

# Konversi tipe data dari float ke integer
b = 9.99 
b_int = int(b)
print("nilai b =", b_int)
print("tipe data b =", type(b_int))

# Konversi tipe data dari integer ke boolean
c = 0
c_bool = bool(c)
print("nilai c =", c_bool)
print("tipe data c =", type(c_bool))

# Konversi tipe data dari float ke boolean
d = 0.0
d_bool = bool(d)
print("nilai d =", d_bool)
print("tipe data d =", type(d_bool))

# Konversi tipe data dari string ke boolean
e_str = "Raihan"
e_bool = bool(e_str)
print("nilai e =", e_bool)
print("tipe data e =", type(e_bool))

# Konversi tipe data dari string kosong ke boolean
f_str = ""
f_bool = bool(f_str)
print("nilai f =", f_bool)
print("tipe data f =", type(f_bool))

# kosntanta 
PI = 3.14 # contoh variabel konstan dengan nama PI
GRAVITY = 9.8 # contoh variabel konstan dengan nama GRAVITY
SPEED_OF_LIGHT = 299792458 # contoh variabel konstan dengan nama SPEED_OF_LIGHT
