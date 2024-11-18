# 1. Membuat sebuah list dengan 5 elemen
A = [10, 20, 30, 40, 50]

# 2. Akses list:
# • Menampilkan elemen ke-3
print("Elemen ke-3:", A[2])

# • Mengambil nilai elemen ke-2 sampai ke-4
print("Elemen ke-2 sampai ke-4:", A[1:4])

# • Mengambil elemen terakhir
print("Elemen terakhir:", A[-1])

# 3. Ubah elemen list:
# • Mengubah elemen ke-4 dengan nilai lainnya
A[3] = 100
print("Setelah mengubah elemen ke-4:", A)

# • Mengubah elemen ke-4 sampai elemen terakhir
A[3:] = [200, 300]
print("Setelah mengubah elemen ke-4 sampai ke-akhir:", A)

# 4. Tambah elemen list:
# • Ambil 2 bagian dari list pertama (A) dan jadikan list ke-2 (B)
B = A[0:2]
print("List B (bagian dari A):", B)

# • Tambah list B dengan nilai string
B.append("Python")
print("List B setelah ditambah string:", B)

# • Tambah list B dengan 3 nilai
B.extend([30, 40, 50])
print("List B setelah ditambah 3 nilai:", B)

# • Gabungkan list B dengan list A
B.extend(A)
print("List B setelah digabungkan dengan A:", B)