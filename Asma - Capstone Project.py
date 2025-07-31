#!/usr/bin/env python
# coding: utf-8

# In[29]:


#DICTIONARY DAFTAR BARANG DI GUDANG
gudang_minimarket = {
    '1' : {'nama' : 'Beras 2kg', 'stok' : 30, 'harga' : 15000},
    '2' : {'nama' : 'Minyak 1L', 'stok' : 50, 'harga' : 20000},
    '3' : {'nama' : 'Gula Pasir 5kg', 'stok' : 80, 'harga' : 30000},
    '4' : {'nama' : 'Telur', 'stok' : 100, 'harga' : 10000},
    '5' : {'nama' : 'Susu', 'stok' : 30, 'harga' : 25000},
}

#MENAMPILKAN MENU UTAMA
def menampilkan_menu():
    print("\n=== Selamat datang di Sistem Manajemen Gudang Minimarket ===\n")
    print("Main Menu:")
    print("1. Menampilkan daftar barang di gudang")
    print("2. Menambahkan data barang baru")
    print("3. Menghapuskan data barang dari gudang")
    print("4. Update jumlah stok di gudang")
    print("5. Exit program")

#MENAMPILKAN DAFTAR BARANG
def menampilkan_daftar():
    print("\n📋 DAFTAR BARANG DI GUDANG")
    print("Kode\t| Nama\t\t\t| Stok\t| Harga")
    print ("-" * 50)
    for kode, data in gudang_minimarket.items():
        print(f"{kode}\t| {data['nama']:<20}\t| {data['stok']}\t| {data['harga']}")
    print ("-" * 50 + "\n")

#MENAMBAHKAN DAFTAR BARANG
def menambahkan_barang():
    print("\n➕ TAMBAH DATA BARANG DI GUDANG")
    while True:
        kode = input("Kode Barang (dalam angka): ")
        if kode in gudang_minimarket:
            print("⚠️ Kode barang sudah ada, input nomor lain!")
        else:
            break
            
    nama = input("Nama Barang:").capitalize()
    stok = int(input("Stok Barang:"))
    harga = int(input("Harga Barang:")) 
    
#Konfirmasi Penyimpanan Data
    konfirmasi = input("\nApakah Data ingin disimpan? (y/n): ").lower()
    if konfirmasi == 'y':
        gudang_minimarket[kode] = {'nama' : nama, 'stok' : stok, 'harga' : harga}
        print("✅ Barang berhasil ditambahkan ke gudang.")
        menampilkan_daftar()
    else:
        print("❌ Data tidak disimpan")
        
#Pilihan antara tambah barang atau kembali ke menu utama
    kembali = input("Apakah ingin input data lain? (y/n): ").lower()
    if kembali == 'y':
        menambahkan_barang()
    else:
        return

#MENGHAPUSKAN DAFTAR BARANG
def menghapuskan_barang():
    print("🗑️ HAPUS DATA BARANG DI GUDANG")
    while True:
        kode_hapus = input("Kode Barang (dalam angka):")
        if kode_hapus in gudang_minimarket:
            barang = gudang_minimarket[kode_hapus]
            print(f"Data ditemukan Nama: {barang['nama']}, Stok: {barang['stok']}, Harga: {barang['harga']}")
                     
#Konfirmasi hapus barang
            konfirmasi = input("\nApakah yakin data dihapus? (y/n): ").lower()
            if konfirmasi == 'y':
                del gudang_minimarket[kode_hapus]
                print(f"✅ Barang dengan kode {kode_hapus} berhasil dihapus.")
                menampilkan_daftar()
            else:
                print("❌ Data tidak jadi dihapus")
        else:
            print("⚠️Kode barang tidak ditemukan!")
            
#Pilihan antara hapus barang atau kembali ke menu utama
        kembali = input("Apakah ingin hapus data lain? (y/n): ").lower()
        if kembali != 'y':
            break

#UPDATE JUMLAH STOK 
def update_stok():
    print("✏️ UPDATE JUMLAH STOK DI GUDANG")
    while True:
        kode = input("Masukkan kode barang yang ingin di-update stoknya: ")
        if kode in gudang_minimarket:
            barang = gudang_minimarket[kode]
            print("\nData Eksisting: ")
            print(f"Nama : {barang['nama']}")
            print(f"Stok : {barang['stok']}")
            print(f"Harga :{barang['harga']}")        
            stok_baru = int(input("Masukkan jumlah stok baru: "))
            
#Konfirmasi Update 
            konfirmasi = input("Apakah yakin update stok? (y/n): ").lower()
            if konfirmasi == 'y':
                gudang_minimarket[kode]['stok'] = stok_baru
                print("✅ Stok berhasil di-update")
                menampilkan_daftar()
            else:
                print("❌ Update dibatalkan")
        else:
            print("⚠️ Kode barang tidak ditemukan!") 
            
#Pilihan antara update stok atau kembali ke menu utama
        kembali = input("Apakah ingin update stok lagi? (y/n): ").lower()
        if kembali != 'y':
            break

#LOOPING MENU UTAMA
while True:
    menampilkan_menu()
    pilihan = input("\nMasukkan pilihan menu (1-5): ")

    if pilihan == "1":
        menampilkan_daftar()
    elif pilihan == "2":
        menambahkan_barang()
    elif pilihan == "3":
        menghapuskan_barang()
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        print("\nTerima kasih telah menggunakan sistem ini.\n")
        break
    else:
        print("⚠️ Pilihan tidak valid. Coba lagi.")


# In[ ]:




