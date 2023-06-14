
def masukan(): # masukan data
    print('SEPATU KEKINIAN'.center(51)) # judul
    print("="*51) # garis
    print(" Kode\t Merek\t\tJenis\t\tHarga") # judul tabel
    print("="*51) # garis
    print("|  1  |\tAdidas  |\tCasual      |\t600.000   |") # isi tabel
    print("|     |\tAdidas  |\tRunning     |\t700.000   |") # isi tabel
    print("|  2  |\tReebok  |\tCasual      |\t700.000   |") # isi tabel
    print("|     |\tReebok  |\tRunning     |\t500.000   |") # isi tabel
    print("|  3  |\t Nike   |\tCasual      |\t900.000   |") # isi tabel
    print("|     |\t Nike   |\tRuninng     |\t1.500.000 |") # isi tabel
    print("|  4  |\tArdiles |\tCasual      |\t200.000   |") # isi tabel
    print("|     |\tArdiles |\tRunning     |\t250.000   |") # isi tabel
    print("="*51) # garis
    print("\n") # enter


# variabel publik
merk_sepatu = [] # list
kode_sepatu = [] # proses
jenis_sepatu = [] # list
harga_sepatu = [] # proses
opsi = [] # proses
opsi_sepatu = [] # proses
jumlah_beli = [] # proses
jumlah = [] # proses

# mengambil inputan

def get_input(): # proses inputan
    i = 0 # variabel lokal
    while i < get_jumlah: # perulangan
        print('-'*20) # garis
        print('   pesanan ke -', i+1) # judul
        print('-'*20) # garis
        kode_sepatu.append( 
            int(input("Masukan kode sepatu yang ingin dibeli 1-4 : "))) # inputan
        if kode_sepatu[i] == 1: # percabangan
            print('-'*20) # garis
            print('ADIDAS'.center(20)) # judul
            print('-'*20) # garis
            opsi_sepatu.append(input("Running atau Casual : ")) # inputan
            if opsi_sepatu[i] == "running" or opsi_sepatu[i] == "Running": # percabangan
                jumlah_beli.append(int(input("Jumlah beli         : "))) # inputan
                merk_sepatu.append("Adidas") # proses
                jenis_sepatu.append("Adidas Running") # proses
                harga_sepatu.append("700.000") # proses
                jumlah.append(jumlah_beli[i]*700000) # proses
            elif opsi_sepatu[i] == "Casual" or opsi_sepatu[i] == "casual": # percabangan
                jumlah_beli.append(int(input("Jumlah beli         : "))) # inputan
                merk_sepatu.append("Adidas") # proses
                jenis_sepatu.append("Adidas Casual") # proses
                harga_sepatu.append("600.000") # proses
                jumlah.append(jumlah_beli[i]*600000) # proses
            else: # percabangan
                merk_sepatu.append('Merek sepatu tidak diketahui') # proses
                jenis_sepatu.append('jenis sepatu tidak diketahui') # proses
                harga_sepatu.append("0") # proses
                jumlah.append(jumlah_beli[i]*0) # proses
        elif kode_sepatu[i] == 2: # percabangan
            print('-'*20) # garis
            print('REEBOK'.center(20)) # judul
            print('-'*20) # garis
            opsi_sepatu.append(input("Running atau Casual : ")) # inputan
            if opsi_sepatu[i] == "Running" or opsi_sepatu[i] == "running": # percabangan
                jumlah_beli.append(int(input("Jumlah beli         : "))) # inputan
                merk_sepatu.append("Rebook") # proses
                jenis_sepatu.append("Reebok Running") # proses
                harga_sepatu.append("500.000") # proses
                jumlah.append(jumlah_beli[i]*500000) # proses
            elif opsi_sepatu[i] == "Casual" or opsi_sepatu[i] == "casual": # percabangan
                jumlah_beli.append(int(input("Jumlah beli         : "))) # inputan
                merk_sepatu.append("Rebook") # proses
                jenis_sepatu.append("Reebok Casual ") # proses
                harga_sepatu.append("700.000") # proses
                jumlah.append(jumlah_beli[i]*700000) # proses
            else: # percabangan
                merk_sepatu.append('Merek sepatu tidak diketahui') # proses
                jenis_sepatu.append('jenis sepatu tidak diketahui') # proses
                harga_sepatu.append("0") # proses
                jumlah.append(jumlah_beli[i]*0) # proses
        elif kode_sepatu[i] == 3: # percabangan
            print('-'*20)
            print('NIKE'.center(20))
            print('-'*20)
            opsi_sepatu.append(input("Running atau Casual : "))
            if opsi_sepatu[i] == "Running" or opsi_sepatu[i] == "running":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Nike")
                jenis_sepatu.append("Nike Running")
                harga_sepatu.append("1.500.000")
                jumlah.append(jumlah_beli[i]*1500000)
            elif opsi_sepatu[i] == "Casual" or opsi_sepatu[i] == "casual":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Nike")
                jenis_sepatu.append("Nike Casual")
                harga_sepatu.append("900.000")
                jumlah.append(jumlah_beli[i]*900000)
            else:
                merk_sepatu.append("merek sepatu tidak diketahui")
                jenis_sepatu.append("Jenis sepatu tidak diketahui")
                harga_sepatu.append("0")
                jumlah.append(jumlah_beli[i]*0)
        elif kode_sepatu[i] == 4:
            print('-'*20)
            print('ARDILES'.center(20))
            print('-'*20)
            opsi_sepatu.append(input("Running atau Casual : "))
            if opsi_sepatu[i] == "Running" or opsi_sepatu[i] == "running":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Ardiles")
                jenis_sepatu.append("Ardiles Running")
                harga_sepatu.append("250.000")
                jumlah.append(jumlah_beli[i]*250000)
            elif opsi_sepatu[i] == "Casual" or opsi_sepatu[i] == "casual":
                jumlah_beli.append(int(input("Jumlah beli         : ")))
                merk_sepatu.append("Ardiles")
                jenis_sepatu.append("Ardiles Casual")
                harga_sepatu.append("200.000")
                jumlah.append(jumlah_beli[i]*200000)
            else:
                merk_sepatu.append("merek sepatu tidak diketahui")
                jenis_sepatu.append("Jenis sepatu tidak diketahui")
                harga_sepatu.append("0")
                jumlah.append(jumlah_beli[i]*0)
        else:
            print('\n') # enter
            print('-'*30) # garis
            print(" Kode yang anda masukan salah") # proses
            print('-'*30) # garis
            continue # proses
        i += 1 # proses
# tempalte layar keluar


def template_keluar(): # proses
    print('-'*79)
    print(' Kode\t merk\t\tjenis\t\tharga\t\tbanyak\t\tjumlah')
    print('sepatu\tsepatu\t\tsepatu\t\tsatuan\t\t beli\t\tharga')
    print('-'*79)
# proses bayar


def proses_bayar(): # proses
    j = 0 # proses
    while j < get_jumlah: # proses
        print(
            f'  {kode_sepatu[j]}\t{merk_sepatu[j]}\t     {jenis_sepatu[j]}\t{harga_sepatu[j]}\t          {jumlah_beli[j]}\t        {jumlah[j]}') # proses
        j += 1
    print('-'*79)
# menghitung jumlah bayar


def jumlah_bayar(jumlah): # proses
    z = 0 # proses
    x = jumlah # proses
    jumlah_bayar = len(x) # proses
    for i in range(jumlah_bayar): # range proses
        y = x[i] # proses
        z += y # proses
    return z # proses
# menghitung pajak


def pajak():
    pajak = jumlah_bayar(jumlah)*10/100
    return pajak
# menghitung total bayar


def total_bayar():
    total = pajak() + jumlah_bayar(jumlah)
    return total


# cetak
masukan() # proses
get_jumlah = int(input("Masukan jumlah sepatu yang ingin di beli : ")) # proses
get_input() # proses
template_keluar() # proses
proses_bayar()
print(f'\t\t\t\t\t\t\t Jumlah bayar : Rp. {jumlah_bayar(jumlah)}')
print(f'\t\t\t\t\t\t\t Pajak 10%    : Rp. {int(pajak())}')
print(f'\t\t\t\t\t\t\t Total bayar  : Rp. {int(total_bayar())}')
ubay = int(input("\t\t\t\t\t\t\t uang bayar   : Rp."))
kembali = ubay-total_bayar()
print(f'\t\t\t\t\t\t\t Uang kembali : Rp. {int(kembali)}') # proses