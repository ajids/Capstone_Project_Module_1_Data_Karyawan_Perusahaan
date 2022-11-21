# Nama: Aji Dwi Septian
# Capstone project: data perusahaan karyawan
# Video: 10 Menit
# Fungsi: Create, read, update, delete, integrasi sistem dan efisiensi code

daftarKaryawan = [
    ['D01', 'Agus Tiger', 'Laki-laki', '23', 'Data Engineer'],
    ['S02', 'Roger Sumatra', 'Laki-laki', '27', 'Sales Engineer'],
    ['S03', 'Olivia Aqua', 'Perempuan', '24', 'Account Manager'],
    ['D04', 'Maya Livia', 'Perempuan', '21', 'Data Scientist'],
]

# Tampilan menu utama
mainMenu = 0
def lihatMenu():
    if daftarKaryawan == []:
        print("-----Data karyawan tidak ditemukan.----\n")
    else:
        print('''
        ----- Database karyawan perusahaan PT. Berkah Ridho-----\nSelamat datang di database karyawan perusahaan, silahkan pilih menu dibawah\n''')
        print("1. Tampilkan Data Karyawan\n2. Menambahkan Data Karyawan\n3. Mengubah Data Karyawan\n4. Menghapus Data Karyawan\n5. Exit\n")

# Tampilkan data karyawan (fungsi read)
def read():
    lokalMenu = 0

    while(True):
        print('''---- Tampilkan Data Karyawan ----\n
        1. Tampilkan seluruh data
        2. Cari data tertentu
        3. Kembali ke menu utama\n''')
        lokalMenu = int(input("Silakan pilih [1-3] : "))

        if lokalMenu == 1:
            print('Daftar Karyawan:\n')
            print('ID\t\t| Nama\t\t\t| Jenis Kelamin\t\t| Umur\t\t| Job Position\t\t\t')
            for daftar in daftarKaryawan:
               print(f"{daftar[0]}\t\t| {daftar[1]}\t\t| {daftar[2]}\t\t| {daftar[3]}\t\t| {daftar[4]}\t\t")
        elif lokalMenu == 2:
            id = input("Masukkan ID : ")
            ada = False
            data = []
            
            for daftar in daftarKaryawan:
                if daftar[0] == id:
                    ada = True
                    data = daftar
            
            if ada:
                print(f"Data Karyawan dengan ID : {id}")
                print(f"ID: {data[0]}, Nama: {data[1]}, Jenis kelamin: {data[2]}, Umur: {data[3]}, Job position: {data[4]}")
            else:
                print("!!! Data karyawan tidak ditemukan !!!")
        elif lokalMenu == 3:
            break
        else:
            pass
        print()
# Buat data karyawan (fungsi create)
def create():
    lokalMenu = 0

    while(True):
        print('''---- Tambah Data Karyawan ----\n
        1. Tambahkan data karyawan
        2. Kembali ke menu utama\n''')
        lokalMenu = int(input("Silakan pilih [1 dan 2] : "))

        if lokalMenu == 1:
            id = input("Masukkan ID : ")
            ada = False

            for daftar in daftarKaryawan:
                if daftar[0] == id:
                    ada = True
            
            if ada:
                print("Data sudah ada")
            else:
                nama = input("Masukkan nama: ")
                jenisKelamin = input("Masukkan jenis kelamin: ")
                umur = input("Masukkan umur: ")
                jobPosition = input("Masukkan job position: ")

                while(True):
                    konfirmasi = input("Apakah Data akan disimpan? (Y/N) : ")

                    if konfirmasi == "Y":
                        daftar = [id, nama, jenisKelamin, umur, jobPosition]
                        daftarKaryawan.append(daftar)
                        print("Data Tersimpan")
                        break
                    
                    if konfirmasi == "N":
                        break
                print()
                                        
        elif lokalMenu == 2:
            break
        else:
            pass

# Mengubah data karyawan (fungsi update)
def update():
    lokalMenu = 0

    while(True):
        print('''---- Mengubah Data Karyawan ----\n
        1. Ubah data karyawan
        2. Kembali ke menu utama\n''')
        lokalMenu = int(input("Silakan pilih [1 dan 2] : "))
        if lokalMenu == 1:
            id = input("Masukkan ID : ")
            ada = False
            index = 0
            i = 0
            for daftar in daftarKaryawan:
                if daftar[0] == id:
                    ada = True
                    index = i
                    break
                i = i + 1
            
            if ada:
                data = daftarKaryawan[index]
                print(f"ID: {data[0]}, Nama: {data[1]}, Jenis Kelamin: {data[2]}, Umur: {data[3]}, Job position : {data[4]}")
                while(True):
                    konfirmasi = input("Tekan Y jika ingin perbaharui data atau N jika batal perbaharui (Y/N): ")
                    if konfirmasi == "Y":
                        kolom = input("Masukkan keterangan yang ingin diperbaharui: ")
                        if kolom == "nama":
                            namaBaru = input("Masukkan Nama Baru: ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diupdate? (Y/N): ")
                                if konfirmasi2 == "Y":
                                    daftarKaryawan[index][1] = namaBaru
                                    print("Data telah berhasil diperbaharui")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data tidak diperbaharui")
                                    break
                                else:
                                    pass
                        elif kolom == "Jenis kelamin":
                            genderBaru = input("Masukkan jenis kelamin baru: ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diperbaharui? (Y/N): ")
                                if konfirmasi2 == "Y":
                                    daftarKaryawan[index][2] = genderBaru
                                    print("Data telah berhasil diperbaharui")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data tidak diperbaharui")
                                    break
                                else:
                                    pass
                        elif kolom == "umur":
                            umurBaru = input("Masukkan umur baru: ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diupdate? (Y/N) : ")
                                if konfirmasi2 == "Y":
                                    daftarKaryawan[index][3] = umurBaru
                                    print("Data telah berhasil diperbaharui")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data tidak diperbaharui")
                                    break
                                else:
                                    pass
                        elif kolom == "job":
                            jobBaru = input("Masukkan job position Baru: ")
                            while(True):
                                konfirmasi2 = input("Apakah Data akan diupdate? (Y/N): ")
                                if konfirmasi2 == "Y":
                                    daftarKaryawan[index][4] = jobBaru
                                    print("Data telah berhasil diperbaharui")
                                    break
                                elif konfirmasi2 == "N":
                                    print("Data tidak diperbaharui")
                                    break
                                else:
                                    pass
                        break
                    if konfirmasi == "N":
                        print("Data batal diperbaharui")
                        break
                print()
            else:
                print("Data Tidak Ada\n")

        elif lokalMenu == 2:
            break
        else:
            pass
# Menghapus data karyawan (fungsi delete)
def delete():
    lokalMenu = 0

    while(True):
        print('''---- Mengubah Data Karyawan ----\n
        1. Hapus data karyawan
        2. Kembali ke menu utama\n''')
        lokalMenu = int(input("Silakan pilih [1 dan 2] : "))

        if lokalMenu == 1:
            id = input("Masukkan ID: ")
            ada = False
            index = 0

            i = 0
            for daftar in daftarKaryawan:
                if daftar[0] == id:
                    ada = True
                    index = i
                    break
                i = i + 1
            
            if ada:
                while(True):
                    konfirmasi = input("Anda yakin data dihapus? (Y/N): ")
                    if konfirmasi == "Y":
                        daftarKaryawan.pop(index)
                        print("Data telah dihapus")
                        break
                    if konfirmasi == "N":
                        print("Data Tidak Terhapus")
                        break
                print()
            else:
                print("Data tidak Ada")
                print()
        elif lokalMenu == 2:
            break
        else:
            pass
# Main menu
while(True):
    lihatMenu()
    menuUtama = int(input("Silakan pilih menu utama [1-5]: "))
    print()

    if menuUtama == 1:
        read()
    elif menuUtama == 2:
        create()
    elif menuUtama == 3:
        update()
    elif menuUtama == 4:
        delete()
    elif menuUtama == 5:
        print("Terima kasih, sampai jumpa lagi\n")
        break
    else:
        print("!!!!! Pilihan yang anda masukkan salah !!!!!")
    print()

