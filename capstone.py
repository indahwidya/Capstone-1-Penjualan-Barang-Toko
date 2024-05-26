#list barang tersedia
stok_barang = {
    'Toner' : {'Nama' : 'Toner', 'Merk' : 'Dena', 'Tipe' : 'Skincare', 'Stok' : 10, 'Harga' : 100000},
    'Serum' : {'Nama' : 'Serum', 'Merk' : 'Dena', 'Tipe' : 'Skincare', 'Stok' : 8, 'Harga' : 120000},
    'Masker' : {'Nama' : 'Masker', 'Merk' : 'Dena', 'Tipe' : 'Skincare', 'Stok' : 10, 'Harga' : 50000},
    'Sunscreen' : {'Nama' : 'Sunscreen', 'Merk' : 'Dena', 'Tipe' : 'Skincare', 'Stok' : 6, 'Harga' : 75000},
    'Cushion' : {'Nama' : 'Cushion', 'Merk' : 'Dena', 'Tipe' : 'Makeup', 'Stok' : 5, 'Harga' : 60000},
}

#FUNGSI READ
#read barang keseluruhan
def read_dataSeluruh():
    if len(list(stok_barang.keys())) > 0:
        print('Stok barang tersedia') 
        for key in stok_barang.keys():
            print('Nama : {}, Merk : {}, Tipe : {}, Stok : {}, Harga : {}'.format(stok_barang[key]['Nama'], stok_barang[key]['Merk'], stok_barang[key]['Tipe'], stok_barang[key]['Stok'], stok_barang[key]['Harga']))
    else:
        print('Tidak ada data barang')

#read barang tertentu
def read_dataTertentu():
    keys_barang = list(stok_barang.keys())
    if len(keys_barang) == 0:
        print('Tidak ada data barang')
    else:
        print(keys_barang)
        while True:
            tampilkan_barang = input('Masukkan barang yang ingin ditampilkan: ').capitalize()
            try:
                print('Nama : {}, Merk : {}, Tipe : {}, Stok : {}, Harga : {}'.format(stok_barang[tampilkan_barang]['Nama'], stok_barang[tampilkan_barang]['Merk'], stok_barang[tampilkan_barang]['Tipe'], stok_barang[tampilkan_barang]['Stok'], stok_barang[tampilkan_barang]['Harga']))
            except:
                print('Barang tidak tersedia')
                continue
            break

#Menu Read
def read_menu():
    while True:
        menuRead = int(input('Menu Tampilkan Barang: \n1. Tampilkan Data Barang Keseluruhan \n2. Tampilkan Data Barang Tertentu \n3. Kembali ke menu sebelumnya \n\nSilahkan pilih nomor menu: '''))
        if menuRead == 1:
            read_dataSeluruh()
        elif menuRead == 2:
            read_dataTertentu()
        elif menuRead == 3:
            staf()
        else:
            print('Menu yang diinput tidak valid, mohon masukan menu kembali')

#FUNGSI CREATE
#create 
def create_stok():
    while True:
        tambah_barang = input('Apakah Anda ingin memasukkan stok barang?(Ya/Tidak): ').lower()
        if tambah_barang == 'ya': 
            nama = input('Masukkan nama barang: ').capitalize()
            try:
                stok_barang[nama]
                print('Barang sudah ada, silahkan masukkan barang lain')
                continue
            except:
                merk = input('Masukkan merk barang: ')
                tipe = input('Masukkan tipe barang: ')
                stok = int(input('Masukkan jumlah stok: '))
                harga = int(input('Masukkan harga barang: '))
                save = input('Apakah anda mau menyimpan data diatas (Ya/Tidak)? ').lower()
                if save == 'ya':
                    stok_barang[nama.capitalize()]={'Nama':nama.capitalize(),'Merk':merk.capitalize(),'Tipe':tipe.capitalize(),'Stok':int(stok),'Harga':int(harga)}
                    print('Data berhasil disimpan')
                elif save == 'tidak':
                    continue
                else:
                    print('Input yang Anda masukkan tidak valid')
                    continue
        elif tambah_barang == 'tidak':
            break
        else:
            continue

def menu_tambahBarang():
    while True:
        menuCreate = int(input('Menu Create Barang : \n1. Menambahkan data barang \n2. Kembali ke menu sebelumnya \n\nSilahkan masukkan nomor menu: '))
        if menuCreate == 1:
            create_stok()
            break
        elif menuCreate== 2:
            staf()
        else:
             print('Menu yang diinput tidak valid, mohon masukkan menu kembali')


#FUNGSI UPDATE
#update
def update_barang():
    list_barang = list(stok_barang.keys())
    print('''Berikut adalah barang yang bisa di update''')
    for i, item in enumerate(list_barang):
        print(f" {i+1} - {item}")
    while True:
        updateBarang = input('Masukkan nama barang: ').capitalize()
        if updateBarang in list_barang:
            print('Nama : {}, Merk : {}, Tipe : {}, Stok : {}, Harga : {}'.format(stok_barang[updateBarang]['Nama'], stok_barang[updateBarang]['Merk'], stok_barang[updateBarang]['Tipe'], stok_barang[updateBarang]['Stok'], stok_barang[updateBarang]['Harga']))
            while True:
                jenis_update = input('Pilih bagian yang akan di update: ').capitalize()
                if jenis_update in list(stok_barang[updateBarang].keys()) :
                    stok_barang[updateBarang][jenis_update] = input('Masukkan update baru: ').capitalize()
                    print('Nama : {}, Merk : {}, Tipe : {}, Stok : {}, Harga : {}'.format(stok_barang[updateBarang]['Nama'], stok_barang[updateBarang]['Merk'], stok_barang[updateBarang]['Tipe'], stok_barang[updateBarang]['Stok'], stok_barang[updateBarang]['Harga']))
                    break
                else :
                    print('Bagian yang dimasukkan tidak ada silakan pilih bagian lain')
            break                
        else:
            print('Silakan masukkan barang yang ada')

def menu_update():
    if len(list(stok_barang.keys())) > 0:
        while True:
            menuCreate = int(input('Menu Update Barang : \n1. Update data barang \n2. Kembali ke Menu sebelumnya \n\nSilahkan masukkan nomor menu: '))
            if menuCreate == 1:
                update_barang()
            elif menuCreate== 2:
                staf()
            else:
                print('Menu yang diinput tidak valid, mohon masukkan menu kembali')
    else:
        print('Tidak ada data barang')

#FUNGSI DELETE
#delete
def delete_barang():
    semua_data = list(stok_barang.keys())
    print('''Berikut adalah barang yang bisa di pilih''')
    for i, item in enumerate(semua_data):
        print(f" {i+1} - {item}")
    while len(semua_data) > 0:
        delete_barang = input('Masukkan nama barang yang ingin dibuang atau ketik 0 untuk kembali ke menu sebelumnya: ').capitalize()
        if delete_barang in semua_data :
            makeSure = input('Apakah Anda ingin men-delete barang ini (Ya/Tidak)? ').lower()
            if makeSure == 'ya':
                del stok_barang[delete_barang]
                print('Barang tersebut berhasil dihapus')
                semua_data = list(stok_barang.keys())
            elif makeSure == 'tidak':
                return
            else:
                print('Masukkan pilihan yang benar')
        elif delete_barang == '0':
            menu_delete()
        else:
            print('Barang tidak ada')
            continue
    print('Barang sudah habis')

def menu_delete():
    if len(list(stok_barang.keys())) > 0:
        while True:
            menuDelete = int(input('Menu Delete Barang : \n1. Delete data barang \n2. Kembali ke Menu sebelumnya \n\nSilahkan masukkan nomor menu: '))
            if menuDelete == 1:
                delete_barang()
            elif menuDelete == 2:
                staf()
            else:
                print('Menu yang diinput tidak valid, mohon masukkan menu kembali')
    else:
        print('Tidak ada data barang')

#FUNGSI READ & MENGHITUNG REVENUE
#Revenue
def revenue():
    listBarang = list(stok_barang.keys())
    if len(listBarang) == 0:
        print('Tidak ada data barang')
    else:
        while True:
            print('Daftar Barang yang tersedia')
            for i, item in enumerate(listBarang):
                print(f" {i+1} - {item}")
            revenueBarang = input('Masukkan nama barang yang akan dihitung revenuenya atau masukkan angka 0 untuk kembali ke menu sebelumnya: ').capitalize()
            if revenueBarang == '0':
                menu_revenue()
            elif revenueBarang in listBarang :
                hitung = 0
                barang = stok_barang[revenueBarang]
                hitung += barang['Stok'] * barang['Harga']
                print(f"Total revenue untuk {revenueBarang}: {hitung}")
            else:
                print(f"Barang '{revenueBarang}' tidak ditemukan di stok.")

def menu_revenue():
    while True:
        menurev = int(input('Berikut adalah menu revenue: \n1. Hitung revenue barang tertentu \n2. Hitung total revenue seluruh barang di toko \n3. Kembali ke menu sebelumnya \n\nSilahkan pilih nomor menu diatas : '))
        if menurev == 1:
            revenue()
        elif menurev == 2:
            total_revenue = 0  # Inisialisasi variabel total revenue
            for barang in stok_barang.values():
                total_revenue += barang['Stok'] * barang['Harga']
            barangRev= list(stok_barang.keys())
            print('Daftar barang yang ada di toko adalah {}'.format(barangRev))
            print(f"Total revenue semua barang: {total_revenue}")
        elif menurev == 3:
            staf()
        else:
            print('Pilihan yang dimasukkan tidak ada, silahkan masukkan pilihan yang benar')

#FUNGSI MENU
def staf():
    while True:
        stafMenu = int(input('Selamat datang di Inventory Toko Cantik Dena \n\nSilahkan pilih menu dibawah ini: \n1. Tampilkan list barang toko \n2. Ubah detail barang \n3. Tambah barang baru \n4. Hapus data barang \n5. Revenue Toko Dena \n6. Kembali ke menu utama \n\nSilahkan pilih salah satu menu diatas : '))
        if stafMenu == 1:
            read_menu()
        elif stafMenu == 2:
            menu_update()
        elif stafMenu == 3:
            menu_tambahBarang()
        elif stafMenu == 4:
            menu_delete()
        elif stafMenu == 5:
            revenue()
        elif stafMenu == 6:
            menuUtama()
        else:
            print('Pilihan yang dimasukkan tidak ada, silahkan masukkan pilihan yang benar')

def menuUtama():
    while True:
        utama = int(input('Selamat Datang Di Inventory Toko Dena \n\nMasuk sebagai:\n1. Staf Toko \n2. Exit \n\nSilahkan pilih salah satu nomor diatas : '))
        if utama == 1:
            staf()
        elif utama == 2:
            exit()
        else:
            print('Pilihan yang dimasukkan tidak ada, silahkan masukkan pilihan yang benar')



menuUtama()