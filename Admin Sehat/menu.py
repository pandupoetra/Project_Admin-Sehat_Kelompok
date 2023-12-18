import fitur
import os

def menu():
    while True:
        #membuat menu tampilan awal
        print("\n")
        print("+" + "-" * 39 + "+")
        print(" Menu Manajemen Rumah Sakit ".center(41))
        print("+" + "-" * 39 + "+")
        print("| 1. Tambah Data Pasien                 |")
        print("| 2. Edit Data Pasien                   |")
        print("| 3. Hapus Daftar Pasien                |")
        print("| 4. Cari Data Pasien                   |")
        print("| 5. Tampilkan Semua Data               |")
        print("| 6. Keluar                             |")
        print("+" + "-" * 39 + "+")
        #membuat variabel menyimpan inputan yang akan diberikan oleh user
        pilihan = input("Pilih menu (1/2/3/4/5/6): ")
        print("")

        #membuat percabangan untuk memanggil fungsi yang dipilih user pada menu
        if pilihan == '1':
            fitur.tambah_pasien()
        elif pilihan == '2':
            fitur.edit_pasien()
        elif pilihan == '3':
            fitur.hapus_pasien()
        elif pilihan == '4':
            fitur.cari_pasien()
        elif pilihan == '5':
            fitur.tampilkan_daftar_pasien()
        elif pilihan == '6':
            print("Terima kasih, sampai jumpa kembali 🤗🤗")
            os.system('cls')
            break
        #membuat opsi jika user tidak memasukan pilihan yang sesuai
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
