# main.py

import os
from utils import nilai_ke_label, hitung_ip

biodata = {}
sks_list = []
nilai_list = []


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print("------------ Menu Utama ------------")
    print("1. Biodata")
    print("2. Input SKS")
    print("3. Input Nilai")
    print("4. Lihat Nilai")
    print("5. Lihat IP")
    print("6. Keluar")


while True:
    clear()
    menu()
    pilihan = input("Pilihan: ")

    if pilihan == "1":
        print("---------- Biodata Mahasiswa ----------")
        mode = input("Lihat Biodata atau Input Biodata? (1/2): ")

        if mode == "1":
            if not biodata:
                print("Biodata belum diinput.")
            else:
                print(f"Nama : {biodata['nama']}")
                print(f"NIM  : {biodata['nim']}")

        elif mode == "2":
            biodata['nama'] = input("Nama: ")
            biodata['nim'] = input("NIM : ")
            print("Biodata berhasil diinput.")

    elif pilihan == "2":
        print("---------- Input SKS ----------")
        sks_input = input("Masukkan SKS (pisahkan spasi): ")
        sks_list = list(map(int, sks_input.split()))
        print("SKS berhasil disimpan.")

    elif pilihan == "3":
        print("---------- Input Nilai ----------")
        mode = input("Input angka atau huruf? (1/2): ")
        nilai_list.clear()

        if mode == "1":
            nilai_input = input("Nilai angka (pisahkan spasi): ")
            angka_list = list(map(int, nilai_input.split()))
            nilai_list = [nilai_ke_label(n) for n in angka_list]

        elif mode == "2":
            nilai_input = input("Nilai huruf (pisahkan spasi): ")
            nilai_list = nilai_input.upper().split()

        print("Nilai berhasil disimpan.")

    elif pilihan == "4":
        print("---------- Data Nilai ----------")
        if not biodata:
            print("Biodata belum diinput.")
        else:
            print(f"Nama : {biodata['nama']}")
            print(f"NIM  : {biodata['nim']}")
            print(f"Nilai: {nilai_list}")

    elif pilihan == "5":
        print("---------- IP Mahasiswa ----------")
        hasil = hitung_ip(nilai_list, sks_list)
        print(f"IP: {hasil}")

    elif pilihan == "6":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid.")

    input("\nTekan Enter untuk kembali ke menu...")