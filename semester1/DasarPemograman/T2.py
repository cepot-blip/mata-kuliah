def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp ' + y
    else:
        a = y[-3:]
        b = y[:-3]
        return formatrupiah(a) + '.' + b

print("=" * 52)
print(" " * 14, "Chicken Dajjal Biadab", " " * 20)
print("=" * 52)
print("Kode  Jenis    Harga")
print("-" * 23)
print("D     Dada     Rp 2500")
print("P     Paha     Rp 2000")
print("S     Sayap    Rp 1500")

banyakJenis     = int(input("Berapa Jenis yang akan anda beli :  "))
kodePotong      = []
banyakPotong    = []
jenisPotong     = []
hargaPerPotong  = []
JumlahHarga     = []

# Input Data
i = 0
while i < banyakJenis:
    print("-" * 32)
    print("Jenis ke - ", i+1)
    kodePotong.append(str(input("Kode Potong [D/P/S] : ")))
    banyakPotong.append(int(input("Banyak Potong   : ")))

    if(kodePotong[i] == "D" or kodePotong[i] == "d"):
        jenisPotong.append("Dada ")                      
        hargaPerPotong.append(2500)                      
        JumlahHarga.append(banyakPotong[i] * int(2500)) 
    elif(kodePotong[i] == "P" or kodePotong[i] == "p"):
        jenisPotong.append("Paha ")
        hargaPerPotong.append(2000)
        JumlahHarga.append(banyakPotong[i] * int(2000))
    elif(kodePotong[i] == "S" or kodePotong[i] == "s"):
        jenisPotong.append("Sayap")
        hargaPerPotong.append(1500)
        JumlahHarga.append(banyakPotong[i] * int(1500))
    else:
        jenisPotong.append("Jenis Potong Tidak Tersedia")
        hargaPerPotong.append(0)
        JumlahHarga.append(banyakPotong[i] * int(0))

    i += 1


# Notification
print("")
print("Sedang Mencetak Bil .....")
print("")

print("=" * 52)
print(" " * 14, "Chicken Dajjal Biadab", " " * 20)
print("=" * 52)

print(" No    Jenis      Harga        Jumlah    Jumlah")
print("       Potong     PerPotong    Beli      Harga ")
print("-" * 52)
template = ' {c}     {jenis_potong}      {harga}          {banyak_potong}        {jumlah}'

a = 0
while a < banyakJenis:
    c = a + 1
    print(template.format(c = c, jenis_potong = jenisPotong[a], harga = hargaPerPotong[a], banyak_potong = banyakPotong[a], jumlah = JumlahHarga[a]))
    a = a + 1

print("=" * 52)
totalPembelian = sum(JumlahHarga) 
print("Total Pembelian : ", formatrupiah(totalPembelian))
jumlahBayar = int(input("Jumlah Bayar    :  Rp "))
jumlahPajak = jumlahBayar * 0.1
totalBayar  = jumlahBayar + jumlahPajak
print("Pajak 10%       : ", formatrupiah(str(jumlahPajak).rstrip('0').rstrip('.')))
print("Total Bayar     : ", formatrupiah(str(totalBayar).rstrip('0').rstrip('.')))
print("=" * 52)