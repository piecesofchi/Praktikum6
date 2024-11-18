# Inisialisasi list untuk menyimpan data
data_mahasiswa = []

while True:
    print("\nMasukkan data mahasiswa")
    nama = input("Nama: ")
    nim = input(("NIM: "))
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    # Hitung nilai akhir
    nilai_akhir = (0.3 * tugas) + (0.35 * uts) + (0.35 * uas)

    # Tambahkan data ke list
    data_mahasiswa.append({
        "Nama": nama,
        "NIM": nim,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": nilai_akhir
    })

    # Tanya apakah ingin menambah data lagi
    lanjut = input("Tambah data lagi? (y/t): ").lower()
    if lanjut == 't':
        break

# Tampilkan data mahasiswa
print("\nDaftar Data Mahasiswa")
print("=============================================")
print("No  | Nama       | NIM | Tugas | UTS   | UAS   | Nilai Akhir")
print("=============================================")
for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"{i:<4}| {mahasiswa['Nama']:<5} | {mahasiswa['NIM']:<5} | {mahasiswa['Tugas']:<5} | {mahasiswa['UTS']:<5} | {mahasiswa['UAS']:<5} | {mahasiswa['Nilai Akhir']:<11.2f}")
print("=============================================")
