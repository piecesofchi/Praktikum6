# Praktikum6
![Screenshot (54)](https://github.com/user-attachments/assets/a38e24bc-0f64-4759-a231-5df59a494203)
![Screenshot (55)](https://github.com/user-attachments/assets/746cabec-1664-4d83-b6c3-832902cff70d)
![Screenshot (56)](https://github.com/user-attachments/assets/0e85ded5-58c3-4211-ad2b-d2a02f1d7720)
![Screenshot (57)](https://github.com/user-attachments/assets/89d73afb-ea29-4eb2-be66-518733beced3)
![Screenshot (58)](https://github.com/user-attachments/assets/dddd2476-153b-4de1-b8cf-486de473a95a)
![Screenshot (52)](https://github.com/user-attachments/assets/09199112-4f9f-4883-ac50-ea4f33fd4a96)
![Screenshot (53)](https://github.com/user-attachments/assets/a46668d0-0e3e-4f39-9ec9-0579fe00c3b7)

Program ini adalah alat sederhana untuk mengelola data nilai mahasiswa. Dengan program ini, kamu bisa:
1. Menambahkan data mahasiswa: seperti NIM, nama, nilai tugas, UTS, dan UAS.
2. Mengubah data mahasiswa: memperbarui nilai jika ada perubahan.
3. Menghapus data mahasiswa: menghilangkan data mahasiswa yang tidak diperlukan.
4. Mencari data mahasiswa: menemukan informasi mahasiswa tertentu berdasarkan NIM.
5. Melihat daftar semua mahasiswa: tampil dalam format tabel yang rapi.
Semua data disimpan sementara di dalam program (di memory), jadi begitu program ditutup, data akan hilang.

Komponen Utama Program
1. Penyimpanan Data (mahasiswa)
Data disimpan dalam bentuk dictionary. Anggap saja dictionary ini seperti buku catatan, di mana setiap mahasiswa diwakili oleh NIM sebagai "kunci", dan detail mereka (nama, nilai tugas, UTS, UAS, dan nilai akhir) sebagai isinya.
2. Menghitung Nilai Akhir
Nilai akhir dihitung dengan rumus:
30% dari nilai tugas + 35% dari nilai UTS + 35% dari nilai UAS
Ini memastikan setiap komponen nilai punya pengaruh tertentu terhadap nilai akhir.
3. Fungsi Utama
Tambah Data: Memasukkan data baru.
Ubah Data: Memperbaiki nilai jika ada kesalahan atau pembaruan.
Hapus Data: Menghapus mahasiswa dari daftar berdasarkan NIM.
Cari Data: Menemukan informasi mahasiswa berdasarkan NIM.
Lihat Data: Menampilkan semua mahasiswa dan nilai mereka dalam tabel.
4. Tampilan Menu
Program menampilkan menu pilihan seperti ini:
Menu Pilihan:
(L)ihat Daftar Nilai
(T)ambah Data
(U)bah Data
(H)apus Data
(C)ari Data
(K)eluar
Lalu tinggal pilih huruf sesuai aksi yang ingin dilakukan, dan program akan memandu langkah-langkahnya.

Bagaimana Cara Kerja Program?
1. Program akan terus berjalan sampai kamu memilih opsi Keluar (K).
2. Kamu bisa menambahkan, mengubah, menghapus, atau melihat data mahasiswa kapan saja.
3. Program juga memberi notifikasi jika kamu mencoba mencari atau mengubah data mahasiswa yang NIM-nya tidak ditemukan.
4. Semua data ditampilkan dalam bentuk tabel yang rapi, sehingga mudah dibaca.

Kelebihan Program
1. Sederhana: Mudah dipahami bahkan untuk pemula.
2. Modular: Setiap fitur punya fungsi tersendiri, jadi programnya rapi dan terorganisir.
3. Interaktif: Kamu bisa langsung mencoba dan melihat hasilnya.

Kekurangan Program
1. Data tidak disimpan secara permanen. Begitu program ditutup, semua data hilang. Untuk mengatasi ini, bisa ditambahkan fitur penyimpanan ke file (misalnya CSV).
2. Validasi input bisa diperbaiki, misalnya memastikan nilai hanya 0-100 dan input lainnya sesuai format.
3. Bisa ditambahkan fitur untuk mengurutkan data, seperti berdasarkan nama atau nilai akhir.

Program ini adalah alat sederhana tapi sangat berguna untuk mengelola data mahasiswa. Cocok untuk belajar dasar-dasar pemrograman Python sambil membuat sesuatu yang praktis!

![Screenshot (59)](https://github.com/user-attachments/assets/b8d757d3-890c-4217-af7b-5500a7a57f76)
