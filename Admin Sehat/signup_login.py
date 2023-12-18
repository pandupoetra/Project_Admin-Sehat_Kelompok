import os
import gui
import menu 

gui.load_animation()
#deklarasi varaibel user sebaagai list penyimpan daftar pengguna
users = {}
def is_valid_password(password):
    return (
        len(password) <= 8 and # Password maksimal 8 karakter
        any(char.isupper() for char in password) and  # Password setidaknya ada huruf kapital
        any(char.isdigit() for char in password) and  # Passsword setidaknya ada angka
        any(char in "!@#$%^&*()_-+=<>?/.,:;" for char in password)  # Password setidaknya ada simbol unik
    )
def check_awal():
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
    
        if username=="admin" and password=="Adset@1":
            print("Pengecekan selesai, silahkan masuk atau tambahkan pengguna")
            break
        if username!="admin":
            print("Username salah, mohon ulangi kemabali!!")
        else:
            print("Password salah, mohon ulangi kembali!!")

# Fungsi untuk masuk (login)
def log_in():
    print("\n---------- Log In User -----------")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username not in users:
        print("Anda belum terdaftar harap Sign-UP terlebih dahulu")
    if username in users and users[username] == password:
        print(f"Selamat datang, {username}!")
        menu.menu()
    else:
        print("password tidak sesuai. Silakan coba lagi.")
    
# Fungsi untuk mendaftarkan pengguna
def sign_up():
    print("\n---------- Sign UP User -----------")
    print("Masukan Password default sistem:")
    check_awal()
    cek_ulang = input("Tambahkan pengguna baru? (Y/N): ")
    username = ""  # Inisialisasi variabel username
    password = ""  # Inisialisasi variabel password

    if cek_ulang.upper().strip() == "Y":
        while True:
            username = input("Masukkan username (maksimal 8 karakter dan harus memuat angka): ")
            if (
            len(username) <= 8 and
            username.isalpha() == True
            ):
                print("Username tidak sesuai ketentuan. Harap ulangi kembali!!")
            elif username in users:
                print("Username sudah digunakan. Silakan coba lagi!!")
            else:
                break
        while True:
            password = input("Masukkan password (maksimal 8 karakter, huruf kapital, angka, dan simbol unik): ")
            if not is_valid_password(password):
                print("Password tidak memenuhi syarat. Harap ulangi kembali!!")
            else:
                break
    else:
        os.system('cls')
        print("MASUK SEBAGAI AKUN GUEST\n")
        menu.menu()
        # menu()

    users[username] = password
    print(f"Pendaftaran dengan username {username} sudah berhasil.")
    os.system('cls')

# Fungsi untuk memulai program
def registery():
    while True:
        print("\n--------------------------------")
        print("Registrasi Admin".center(30))
        print("--------------------------------")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Keluar")
        print("--------------------------------")
        
        choice = input("Pilih menu (1/2/3): ")
        
        if choice == "1":
            sign_up()
        elif choice == "2":
            log_in()
        elif choice == "3":
           break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    registery()