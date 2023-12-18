import os

# deklarasi array daftar pasien sebagai wadah penyimpan data pasien
daftar_pasien = []  
# fungsi untuk melakukan penambahan pasien

def tambah_pasien():
    #mencetak nilai awal tiap nomor urut
    num_PU=0
    num_PG=0
    num_PA=0
    num_LP=0
    #malakukan import modul datetime
    import datetime
    x = datetime.datetime.now()
    tanggal = x.strftime("%d %B %Y %H:%M:%S")
    while True:
        #mencetak tampilan awal saat amsuk ke fitur
        print("+" + "-" * 39 + "+")
        print(" Pilihan fasilitas dapat anda pilih ".center(41))
        print("+" + "-" * 39 + "+")
        print("| 1. Poli Umum                          |")
        print("| 2. Poli Gigi                          |")
        print("| 3. Poli Anak                          |")
        print("| 4. Layanan Psikologi                  |")
        print("| 5. Keluar                             |")
        print("+" + "-" * 39 + "+")
        #membuat varaiable pilihan untuk menyimpan inputan yang dimasukkan pasien
        pilihan = str(input("Pilih menu (1/2/3/4/5): "))
        #memasuki metode percabangan jika memilih salah satu menu
        if pilihan == "5":
            break
        elif pilihan == "1" or pilihan == "2" or pilihan == "3" or pilihan == "4":
            while True:
                print("\n---------- Tambah Data Pasien -----------")
                nama = input("Masukkan nama pasien: ")
                while True:
                    try:
                        umur = int(input("Masukkan umur pasien: "))
                        break
                    except ValueError:
                        print("Maaf, data umur harus dalam format angka\n")
                alamat = input("Masukkan alamat pasien: ")
                while True:
                    try:
                        nomor_telepon = int(input("Masukkan nomor telepon pasien: "))
                        break
                    except ValueError:
                        print("Maaf, data nomor telepon harus dalam format angka\n")
                keluhan = input("Masukkan keluhan pasien: ")
                if pilihan == "1":
                    if num_PU <= 1000:
                        num_PU += 1 
                        kode_PU = str(num_PU).zfill(3)
                        kode = "PU" + kode_PU
                    else:
                        print("Maaf untuk hari ini sudah mencapai batas kuota")
                elif pilihan == "2":
                    if num_PG <= 1000:
                        num_PG += 1
                        kode_PG = str(num_PG).zfill(3)
                        kode = "PG" + kode_PG
                    else:
                        print("Maaf untuk hari ini sudah mencapai batas kuota")
                elif pilihan == "3":
                    if num_PA <= 1000:
                        num_PA += 1
                        kode_PA = str(num_PA).zfill(3)
                        kode = "PA" + kode_PA
                    else:
                        print("Maaf untuk hari ini sudah mencapai batas kuota")
                elif pilihan == "4":
                    if num_LP <= 1000:
                        num_LP += 1
                        kode_LP = str(num_LP).zfill(3)
                        kode = "LP" + kode_LP
                    else:
                        print("Maaf untuk hari ini sudah mencapai batas kuota")
                #mendeklarasikan variabel pasien dalam dictionary
                pasien = {
                    "nama": nama,
                    "umur": umur,
                    "alamat": alamat,
                    "tanggal": tanggal,
                    "keluhan": keluhan,
                    "nomor urutan": kode,
                    "nomor telepon":nomor_telepon
                }
                #menambahkan pasien baru ke dalam variabel daftar pasien 
                if int(num_PU) < 1000 or int(num_PG) < 1000 or int(num_PA) < 1000 or int(num_LP) < 1000:
                    daftar_pasien.append(pasien)
                    print("\nData pasien", nama, "telah ditambahkan.")
                    print("Nomor urutan pasien", nama + ":", kode)
                    # cek ulang apakah ingin menambahkan lagi atau tidak
                    cek_ulang = input("Tambahkan data pasien lainnya? (Y/N): ")
                    if cek_ulang.upper() != "Y":
                        os.system('cls')
                        break
                else:
                    break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.\n")

#fungsi untuk melakukan edit data pasien 
def edit_pasien():
    print("\n---------- Edit Data Pasien -----------")
    #deklarasi dan inisialisasi dari nama pasien yang ingin diedit
    nama = input("Masukkan nama pasien: ")
    #melakukan pengecualian jika pasien tidak terdapat di variabel daftar pasien
    ketemu = False

    #melakukan pencetakan data dengan perulangan jika pasien ada didalam variabel daftar pasien
    for pasien in daftar_pasien:
        if pasien['nama'] == nama:
            ketemu = True
            print(f"\nData pasien dengan nama {nama} ditemukan. \nSilakan edit data berikut:")

            nama = input("Nama pasien: ")
            while True:
                    try:
                        umur = int(input("Masukkan umur pasien: "))
                        break
                    except ValueError:
                        print("Maaf, data umur harus dalam format angka\n")
            alamat  = input("Masukan Alamat pasien: ")
            while True:
                    try:
                        nomor_telepon = int(input("Masukkan nomor telepon pasien: "))
                        break
                    except ValueError:
                        print("Maaf, data nomor telepon harus dalam format angka\n")
            keluhan = input("Masukan Keluhan pasien: ")

            pasien['nama'] = nama
            pasien['umur'] = umur
            pasien['alamat'] = alamat
            pasien['nomor telepon']=nomor_telepon
            pasien['keluhan'] = keluhan

            print("\nData pasien telah diperbarui.")
            
            check_ulang = input("Apakah ingin mengedit lagi? (Y/N): ")
            if check_ulang.upper() == "N":
                os.system('cls')
                break
            if check_ulang.upper() == "Y":
                edit_pasien()
            else:
                print("Masukan yang anda masukan salah, pastikan masukan anda sesuai dengan ketentuan")
    #mencetak opsi output jika data pasien tidak ditemukan dalam variabel daftar pasien 
    if not ketemu:
        print(f"Data pasien dengan nama {nama} tidak ditemukan.")

#fungsi untuk melakuakan hapus data pasien
def hapus_pasien():
    print("\n---------- Hapus Data Pasien -----------")
    #deklarasi dan inisialisasi dari nama pasien yang ingin dihapus
    nama = input("Masukkan nama pasien: ")
    chek_lagi=input(f"Apakah anda yakin ingin menghapus data pasien {nama} ? (Y/N): ")
    if chek_lagi.upper() == "Y" :
        #melakukan pengecualian jika pasien tidak terdapat di variabel daftar pasien
        ketemu = False

        #melakukan pencetakan data dengan perulangan jika pasien ada didalam variabel daftar pasien
        for pasien in daftar_pasien:
            if pasien['nama'] == nama:
                ketemu = True
                daftar_pasien.remove(pasien)
                print(f"\nData pasien dengan nama {nama} telah dihapus.")
                break
        #mencetak opsi output jika data pasien tidak ditemukan dalam variabel daftar pasien
        if not ketemu:
            print(f"Data pasien dengan nama {nama} tidak ditemukan.")
    else:
        print("Proses dibatalakan")
        os.system('cls')


def cari_pasien():
    # membuat informasi awal ketika masuk menu cari pasien
    print("\n---------- Cari Data Pasien -----------")
    # membuat variabel yang menyimpan nama pasien yang dingin dicari oleh user
    nama_cari = input("Masukkan nama pasien: ")
    ditemukan=False 
    hasil_cari = []
    #membuat perulangan untuk menyampaikan informasi pasien yang dicari
    for pasien in daftar_pasien:
        if pasien["nama"] == nama_cari:
            hasil_cari.append(pasien)
            ditemukan = True

    # membuat percabangan sebagai opsi jika nama pasien yang dicari tidak ditemukan
    if not ditemukan:
        print(f"Data pasien dengan nama {nama_cari} tidak ditemukan.")
    else:
        print("\n----------------------------------------")
        print("Faskes Sehat".center(40))
        print("----------------------------------------")
        for pasien in hasil_cari:
            print(f"Data pasien ditemukan:")
            print(f"Nama: {pasien['nama']}")
            print(f"Umur: {pasien['umur']}")
            print(f"Alamat: {pasien['alamat']}")
            print(f"Tanggal: {pasien['tanggal']}")
            print(f"Nomor Telepon: {pasien['nomor telepon']}")
            print(f"Keluhan: {pasien['keluhan']}")
            print(f"Nomor Urut: {pasien['nomor urutan']}")
            print("----------------------------------------")

        check_ulang = input("Apakah ingin mencari lagi? (Y/N): ")
        if check_ulang.upper() == "Y":
            cari_pasien()
        else:
            print("Pencarian selesai.")
            os.system('cls')


def print_table(headers, data):
    # Mencari panjang maksimum tiap kolom
    # Mencari panjang maksimum untuk setiap kolom
    col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *data)]

    # Mencetak header
    # Mencetak baris header dengan format yang benar
    header_row = "| " + " | ".join(f"{header:<{width}}" for header, width in zip(headers, col_widths)) + " |"
    line = "-" * len(header_row)
    print(line)
    print(header_row)
    print(line)

    # Mencetak data
    # Mencetak baris data dengan format yang benar
    for row in data:
        row_str = "| " + " | ".join(f"{item:<{width}}" for item, width in zip(row, col_widths)) + " |"
        print(row_str)
        print(line)

def tampilkan_daftar_pasien():
    # Memeriksa jika daftar pasien kosong
    if not daftar_pasien:
        print("Daftar pasien kosong.")
    else:
        # Mendefinisikan header untuk tabel
        headers = ["Nama", "Umur", "Alamat", "Tanggal", "No. Telepon", "Keluhan", "No. Urut"]
        
        # Membuat list of lists (data) dari informasi pasien
        data = [[
            pasien['nama'],
            pasien['umur'],
            pasien['alamat'],
            pasien['tanggal'],
            pasien['nomor telepon'],
            pasien['keluhan'],
            pasien['nomor urutan']
        ] for pasien in daftar_pasien]

        # Memanggil fungsi print_table untuk menampilkan tabel
        print_table(headers, data)

