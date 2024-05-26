## CRUD PENJUALAN BARANG TOKO - CAPSTONE PURWADHIKA MODUL 1

Capstone project for additional portfolio Purwadhika Data Science Modul 1 (JCDSOL-014) 2024 

Dibuat oleh : Indah Widya Putri

**Program ini bertujuan untuk user dapat mengakses data inventory barang di Toko Dena yang terdiri dari barang kecantikan seperti Skincare dan Makeup**

Deskripsi kolom data barang pada program ini adalah sebagai berikut:

| Keys = Nama  | Nama | Merk  | Tipe | Stok  | Harga |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Toner  | Toner  | Dena  | Skincare  | 10  | 100000  |
| Serum | Serum   | Dena  | Skincare  | 8  | 120000  |
| Masker  | Masker  | Dena  | Skincare  | 10  | 50000  |
| Sunscreen | Sunscreen  | Dena  | Skincare  | 6  | 75000  |
| Cushion  | Cushion  | Dena  | Makeup  | 5  | 60000  |

Detail data kolom diatas pada program akan dikemas dalam dictionary

Pada program ini terdapat beberapa bagian menu yang terintegrasi di dalam main menu

## MAIN MENU
Main menu akan menghubungkan seluruh sub-menu yang ada dalam program ini. Terdapat 2 main-menu yang ada dalam program ini, yaitu menu untuk masuk sebagai staf toko yang selnjutnya user akan masuk ke menu untuk mengakses seluruh sub-menu

## SUB-MENU READ
Sub-Menu Read akan menampilkan data barang toko yang dikemas dalam sebuah dictionary. Pada bagian menu ini user mendapatkan 2 pilihan, yaitu menampilkan seluruh data barang atau menampilkan data barang tertentu sesuai keys barang yang di input dalam program

## SUB-MENU CREATE
Sub-Menu Create berfungsi untuk menambahkan data barang toko. Program akan memerintahkan user untuk menginput detail data barang sesuai kolom. Data barang baru yang dimasukkan tidak boleh memiliki kesamaan nama dengan data barang sebelumnya. Sebelum program menyimpan detail barang baru, program akan meminta persetujuan kembali kepada user terkait input-an yang user telah masukkan ke dalam program

## SUB-MENU UPDATE
Sub-Menu Update berfungsi untuk memperbarui detail barang yang tersedia dalam dictionary. Perbaharuan detail barang akan terbagi menjadi per-bagian kolom per-barang. User akan diminta untuk meng-input bagian kolom mana yang akan diperbaharui ke informasi baru

## SUB-MENU DELETE
Sub-Menu Delete berfungsi untuk menghapus barang berdasarkan keys/nama barang yang diinput oleh user. Sebelum program menghapus barang, program akan meminta persetujuan kembali setuju atau tidaknya user ingin menghapus barang tersebut

## SUB-MENU QUIT
Sub-Menu Quit akan membuat user keluar dari program Data Penjualan Barang Toko Dena


--- MENU TAMBAHAN ---
## SUB-MENU REVENUE
Sub-Menu Revenue berfungsi agar user dapat menghitung revenue yang akan didapatkan dari penjualan barang di Toko Dena. Terdapat 2 pilihan yang bisa user pilih, yaitu menghitung revenue keseluruhan barang dan menghitung revenue barang tertentu berdasarkan input keys/nama barang
