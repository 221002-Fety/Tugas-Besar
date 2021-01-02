import csv
import datetime
import os
filecsv= 'loginPass.csv'


def clear():
    os.system('cls')

def backtoMenuWarga():
    print("\n")
    input("Tekan ENTER untuk kembali...")
    menuWarga()

def backtoMenuAdmin():
    print("\n")
    input("Tekan ENTER untuk kembali...")
    menuAdmin()


def buatAkun() :
    clear()
    paswarga= '085232'
    pasadmin= '128432'
    subject = input('Warga/Admin= ')
    penampung= []
    
    if subject == 'warga':
        nama    = input('Nama       = ')
        password= input('Password   = ')
        penampung.append(nama)
        penampung.append(password)

        if password == paswarga:
            with open(filecsv, 'w', newline='') as file:
                penulis= csv.writer(file, delimiter=',')
                penulis.writerow(penampung)
            clear()
            menuWarga()
        else:
            print('Password yang anda masukan salah!')

    elif subject == 'admin':
        nama    = input('Nama       = ')
        password= input('Password   = ')
        penampung.append(nama)
        penampung.append(password)

        if password == pasadmin:
            with open(filecsv, 'w', newline='') as file:
                penulis= csv.writer(file, delimiter=',')
                penulis.writerow(penampung)
            clear()
            menuAdmin()
        else:
            print('Password yang anda masukan salah!')

    else :
        print('Input anda salah, coba lagi!')



def login() :
    clear()
    print('===LOG IN===')
    nama    = input('nama    = ')
    password= input('password= ')
    data    = []
    data.append(nama)
    data.append(password)
    dataDiri= []

    with open(filecsv, 'r') as file:
        pembaca= csv.reader(file, delimiter=',')
        for data in pembaca:
            dataDiri.append(data)

    for sel in dataDiri:
        sandi= sel[1]
        if sandi=='085232':
            clear()
            menuWarga()
        elif sandi== '128432':
            clear()
            menuAdmin()
        else:
            print('Password/nama yang anda masukan salah!')
    



def logout() :
    clear()
    menuWellcome()




fileSaran= 'saran.csv'
fileBerita= 'berita.csv'
iniPass= []

x = datetime.datetime.now()
tanggal= x.strftime("%A, %d-%b-%Y")


def tambahsaran() :
    clear()
    namaKolom = ['Tanggal', 'Nama', 'Saran']

    nama     = input('Nama penulis = ')
    saran    = input('Saran penulis= ')

    databaru= dict()     
    penampung= []  

    databaru['Tanggal'] = tanggal
    databaru['Nama'] = nama
    databaru['Saran'] = saran

    with open(fileSaran, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for data in reader:
            penampung.append(data)

    penampung.append(databaru)

    with open(fileSaran, 'w', newline='') as csvFile:
        writer= csv.DictWriter(csvFile, delimiter=',', fieldnames=namaKolom)  
        writer.writeheader()
        writer.writerows(penampung)
    clear()
    backtoMenuWarga()



def bacasaran() :
    clear()
    with open(fileSaran, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for data in reader:
            for key, value in data.items() :
                print("{} = {}".format(key, value))
            print()
    clear()
    backtoMenuAdmin()




def tambahberita() :
    clear()
        
    namaKolom = ['Tanggal', 'Judul', 'Isi Berita']

    judul= input('Judul berita= ')
    isi  = input('Isi berita  = ')

    databaru= dict()     
    penampung= []  

    databaru['Tanggal'] = tanggal
    databaru['Judul'] = judul
    databaru['Isi Berita'] = isi

    penampung.append(databaru)

    with open(fileBerita, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for data in reader:
            penampung.append(data)

    with open(fileBerita, 'w', newline='') as csvFile:
        writer= csv.DictWriter(csvFile, delimiter=',', fieldnames=namaKolom)  
        writer.writeheader()
        writer.writerows(penampung)
    clear()
    backtoMenuAdmin()


def bacaberita() :
    clear()
    with open(fileBerita, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for data in reader:
            for key, value in data.items() :
                print("{} = {}".format(key, value))
            print()

    sandi= iniPass[0][1]
    if sandi== '085232':
        clear()
        backtoMenuWarga()
    elif sandi=='128432':
        clear()
        backtoMenuAdmin()




filesoal= 'kuesioner.csv'
filejawab= 'hasilvoting.csv'




def kirimQ() :
    clear()
    hasil=[]
    with open(filejawab, 'w', newline='') as file:
        penulis= csv.writer(file, delimiter=',')
        penulis.writerows(hasil)
        
    penampung= []
    kuesioner= dict()
    header= ['Apa pendapat anda tentang    ', 'Pilih salah satu jawaban dari']
    soal= '\n' + input('Tulis pertanyaan anda= ') + '\n'
    pilihan= '\na. Sangat setuju\nb. Setuju\nc. Kurang setuju\nd. Tidak setuju'

    kuesioner['Apa pendapat anda tentang    ']= soal
    kuesioner['Pilih salah satu jawaban dari']= pilihan

    penampung.append(kuesioner)

    with open(filesoal, 'w', newline='') as soal :
        penulis= csv.DictWriter(soal, delimiter=',', fieldnames=header)
        penulis.writeheader()
        penulis.writerows(penampung)
    clear()
    print('Kuesioner berhasil di tambah.')
    clear()
    backtoMenuAdmin()




def bacaQ() :
    with open(filesoal, 'r') as soal:
        pembaca= csv.DictReader(soal, delimiter=',')
        for data in pembaca:
            for key, value in data.items() :
                print("{} = {}".format(key, value))
            print()




def voteUser():
    clear()
    bacaQ()
    masukan= input('Jawab= ')

    penampung= []

    with open(filejawab, 'a', newline='') as file:
        penulis= csv.writer(file, delimiter=',')
        penulis.writerow(masukan)

    jumlaha = []
    jumlahb = []
    jumlahc = []
    jumlahd = []
    with open(filejawab, 'r') as file:
        scanner= csv.reader(file, delimiter=',')
        for sel in scanner:
            penampung.append(sel)

    for data in penampung:
        if data== ['a']:
            jumlaha.append(1)
        elif data== ['b']:
            jumlahb.append(1)
        elif data== ['c']:
            jumlahc.append(1)
        elif data== ['d']:
            jumlahd.append(1)
    
    print('=======Hasil Kuesioner=======')
    print('     Sangat setuju= ', len(jumlaha))
    print('     Setuju       = ', len(jumlahb))
    print('     Kurang setuju= ', len(jumlahc))
    print('     Tidak setuju = ', len(jumlahd))
    print('~Terimakasih untuk masukannya~')
    clear()
    backtoMenuWarga()



def voteAdmin():
    clear()
    bacaQ()

    penampung= []
    #nanti modelnya buat admin gausah ada inputan
    #kalo user abis input langsung ada hasil

    jumlaha = []
    jumlahb = []
    jumlahc = []
    jumlahd = []
    with open(filejawab, 'r') as file:
        scanner= csv.reader(file, delimiter=',')
        for sel in scanner:
            penampung.append(sel)

    for data in penampung:
        if data== ['a']:
            jumlaha.append(1)
        elif data== ['b']:
            jumlahb.append(1)
        elif data== ['c']:
            jumlahc.append(1)
        elif data== ['d']:
            jumlahd.append(1)

    print('=======Hasil Kuesioner=======')
    print('     Sangat setuju= ', len(jumlaha))
    print('     Setuju       = ', len(jumlahb))
    print('     Kurang setuju= ', len(jumlahc))
    print('     Tidak setuju = ', len(jumlahd))
    print('~Terimakasih atas masukannya~')
    clear()
    backtoMenuAdmin()



def menuWarga():
    while True:
        print('''
        ::::::DESA BOX::::::
               *MENU*
        1. Kotak Saran
        2. Berita Hari Ini
        3. Isi Kuesioner
        4. Keluar dari Akun
        5. Keluar dari Menu
        ::::::::::::::::::::\n''')
        menu= int(input('        Pilih Menu= '))

        if menu == 1:
            tambahsaran()
        elif menu == 2:
            bacaberita()
        elif menu == 3:
            voteUser()
        elif menu == 4:
            logout()
        elif menu == 5:
            clear()
            break
        else:
            print('Input yang anda masukan salah!')


def menuAdmin() :
    while True:
        print('''
        ::::::DESA BOX::::::
               *MENU*
        1. Baca Kotak Saran
        2. Tulis Berita
        3. Baca Berita
        4. Buat Kuesioner
        5. Hasil Kuesioner
        6. Keluar dari Akun
        7. Keluar dari Menu
        ::::::::::::::::::::\n''')
        menu= int(input('        Pilih Menu= '))

        if menu == 1:
            bacasaran()
        elif menu == 2:
            tambahberita()
        elif menu == 3:
            bacaberita()
        elif menu == 4:
            kirimQ()
        elif menu == 5:
            voteAdmin()
        elif menu == 6:
            logout()
        elif menu == 7:
            clear()
            break
        else:
            print('Input yang anda masukan salah!')
        


def menuWellcome() :
    clear()
    while True:
        print('''
        ::::::DESA BOX::::::
          ~Selamat Datang~

        1. Login
        2. Buat Akun Baru
        3. Keluar
        ::::::::::::::::::::\n''')
        menu= int(input('        Pilih Menu= '))
        
        if menu == 1 :
            login()
        elif menu == 2 :
            buatAkun()
        elif menu == 3 :
            clear()
            break


with open(filecsv, 'r') as file:
    pembaca= csv.reader(file, delimiter=',')
    for sel in pembaca:
        iniPass.append(sel)
    print ("iniPass")

if len(iniPass) == 0:
    menuWellcome()
elif len(iniPass) > 0:
    sandi= iniPass[0][1]
    if sandi=='085232':
        menuWarga()
    elif sandi== '128432':
        menuAdmin()
    print ("iniPass")
