# Membuat dictionary daftar kontak
kontak = {
    "Ari": "081267888",
    "Dina": "087677776"
}

# Menampilkan kontak Ari
print("Kontak Ari:", kontak["Ari"])

# Menambah kontak baru dengan nama Riko
kontak["Riko"] = "087654544"

# Mengubah kontak Dina dengan nomor baru
kontak["Dina"] = "088999776"

# Menampilkan semua nama
print("Daftar Nama:", list(kontak.keys()))

# Menampilkan semua nomor
print("Daftar Nomor:", list(kontak.values()))

# Menampilkan daftar nama dan nomor
print("Daftar Nama dan Nomor:")
for nama, nomor in kontak.items():
    print(f"{nama}: {nomor}")

# Menghapus kontak Dina
del kontak["Dina"]

# Menampilkan daftar kontak setelah Dina dihapus
print("Daftar Kontak setelah Dina dihapus:")
for nama, nomor in kontak.items():
    print(f"{nama}: {nomor}")