# Operator unary
# hanya memiliki satu operand
a = -10
b = +5
print(a)
print(b)

# Operator binary/operator aritmatika
# memiliki dua operand
x = 10
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x // y)
print(x ** y)

# Operator ternary
# memiliki tiga operand
z = 10 if x > y else 5
print(z)
print("selesai")

# Operator Perbandingan
# hasilnya boolean (True/False)
print(x > y)   # lebih besar
print(x < y)   # lebih kecil
print(x >= y)  # lebih besar sama dengan
print(x <= y)  # lebih kecil sama dengan
print(x == y)  # sama dengan
print(x != y)  # tidak sama dengan
print("selesai")

# Operator Logika
# memiliki dua operand
print(x > 5 and y < 10)  # AND
print(x > 5 or y < 5)    # OR
print(not(x > 5 and y < 10))  # NOT
print("selesai")

# operator gabungan
# menggabungkan beberapa operator
print((x + y) * (x - y))
print("selesai")
angka1 +=10  # sama dengan angka = angka + 10
print(angka1)
angka2 *=2   # sama dengan angka = angka * 2
print(angka2)
angka3 -=5   # sama dengan angka = angka - 5
print(angka3)
angka4 /=3   # sama dengan angka = angka / 3
print(angka4)  
angka5 //=2  # sama dengan angka = angka // 2
print(angka6)
angka7 %=3   # sama dengan angka = angka % 3
print(angka7)
angka8 **=2  # sama dengan angka = angka ** 2
print(angka8)
print("selesai")

# Operator membership
# untuk mengetahui apakah sebuah data terdaoat didalam list (array) atau squence 

# Membership di String
teks = "Halo Dunia"
print("Halo" in teks)      # True, karena "Halo" ada di dalam teks
print("halo" in teks)      # False, karena huruf besar/kecil berbeda
print("Hai" not in teks)   # True, karena "Hai" tidak ada di teks

# Membership di List
angka = [1, 2, 3, 4, 5]
print(3 in angka)           # True
print(10 in angka)          # False
print(7 not in angka)       # True

# Membership di Tuple
buah = ("apel", "pisang", "mangga")
print("apel" in buah)       # True
print("jeruk" not in buah)  # True

# Membership di Dictionary
data = {"nama": "Raihan", "umur": 21}
print("nama" in data)           # True (karena 'nama' adalah key)
print("Raihan" in data)         # False (karena itu value)
print("umur" not in data)       # False (karena 'umur' ada)

# Operator Identity
# Dasar penggunaan is dan is not
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)       # False → karena x dan y punya isi sama tapi beda objek
print(x == y)       # True  → karena isi (nilai) list-nya sama
print(x is z)       # True  → karena z menunjuk ke objek yang sama dengan x
print(y is not z)   # True  → karena y bukan objek yang sama dengan z
print(x is not y)   # True  → karena x bukan objek yang sama dengan y

# Pada tipe data immutable (seperti int, str, tuple)
a = 10
b = 10
print(a is b)       # True (karena Python menyimpan angka kecil di memori yang sama)

c = "halo"
d = "halo"
print(c is d)       # True (string literal biasanya menunjuk ke objek yang sama)

# Pada None
x = None
print(x is None)        # True
print(x is not None)    # False

# ======================================================
# PRIORITAS (PRECEDENCE) OPERATOR DALAM PYTHON
# ======================================================

# 1. Operator tanda kurung () → Paling tinggi (ekspresi di dalamnya dievaluasi dulu)
hasil = (2 + 3) * 4
print(hasil)  # 20 → karena (2+3)=5 dihitung dulu baru dikali 4

# 2. Operator pangkat **
hasil = 2 ** 3 ** 2
print(hasil)  # 512 → karena 3**2 dihitung dulu (9), lalu 2**9 = 512

# 3. Operator unary (+, -, ~)
x = 5
print(-x)     # -5 → membalik tanda
print(+x)     # 5  → tetap sama
print(~x)     # -6 → bitwise NOT (mengubah semua bit biner)

# 4. Operator perkalian / pembagian / modulus / floor division (*, /, %, //)
print(10 * 2)   # 20
print(10 / 3)   # 3.333...
print(10 // 3)  # 3 (dibulatkan ke bawah)
print(10 % 3)   # 1 (sisa bagi)

# 5. Operator penjumlahan dan pengurangan (+, -)
print(5 + 2)    # 7
print(5 - 2)    # 3

# 6. Operator bitwise shift (<<, >>)
print(5 << 1)   # 10 → geser bit ke kiri (setara *2)
print(5 >> 1)   # 2  → geser bit ke kanan (setara /2)

# 7. Operator bitwise AND (&)
print(5 & 3)    # 1 → 0101 & 0011 = 0001

# 8. Operator bitwise XOR (^)
print(5 ^ 3)    # 6 → 0101 ^ 0011 = 0110

# 9. Operator bitwise OR (|)
print(5 | 3)    # 7 → 0101 | 0011 = 0111

# 10. Operator perbandingan (<, <=, >, >=)
print(5 > 3)    # True
print(5 <= 3)   # False

# 11. Operator kesetaraan (==, !=)
print(5 == 5)   # True
print(5 != 4)   # True

# 12. Operator identity (is, is not)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)       # True → karena objeknya sama
print(a is c)       # False → karena objeknya berbeda meskipun nilainya sama
print(a is not c)   # True

# 13. Operator membership (in, not in)
buah = ["apel", "mangga", "jeruk"]
print("apel" in buah)       # True
print("pisang" not in buah) # True

# 14. Operator logika (not, and, or)
print(not False)     # True → not membalik nilai
print(True and False) # False → True hanya jika keduanya True
print(True or False)  # True  → True jika salah satu True

# 15. Operator penugasan (assignment)
x = 10
x += 5  # Sama seperti x = x + 5
print(x)  # 15

# 16. Operator ekspresi kondisional (ternary) → (True_expr if condition else False_expr)
umur = 18
status = "Dewasa" if umur >= 17 else "Anak-anak"
print(status)  # Dewasa

# 17. Operator urutan evaluasi (lambda, yield, walrus :=)
# lambda → untuk membuat fungsi anonim
f = lambda a: a * 2
print(f(5))  # 10

# Walrus operator (:=) → menyimpan nilai sekaligus digunakan dalam ekspresi
if (n := len([1, 2, 3])) > 2:
    print(f"Panjangnya {n}")  # Panjangnya 3
