print("-"*45)
print("***** SATE KARI'EYEM *****")
print("-"*45)
print("Kode     Jenis Sate         Harga Pertusuk")
print("-"*45)
print("1        Sate Ayam          Rp. 1000")
print("2        Sate Kambing       Rp. 1500")
print("3        Sate Sapi          Rp. 2000")
print("-"*45)

banyak_jenis=int(input("Mau beli berapa jenis sate? : "))
print()
kode=[]
banyak_potong=[]
jenis_potong=[]
harga=[]
jumlah=[]

i=0
while i < banyak_jenis:
    print("-"*45)
    print("Jenis Sate Ke -: ",i+1)
    kode.append(int(input("Kode Sate [1/2/3] : ")))
    print()

    if kode[i]==1 :
        print("-"*10)
        print("Sate Ayam")
        print("-"*10)
        banyak_potong.append(int(input("Banyak Tusuk : ")))
        print()
        jenis_potong.append("Sate Ayam")
        harga.append("1000")
        jumlah.append(banyak_potong[i]*int("1000"))

    elif kode[i]==2 :
        print("-"*12)
        print("Sate Kambing")
        print("-"*12)
        banyak_potong.append(int(input("Banyak Tusuk : ")))
        print()
        jenis_potong.append("Sate Kambing")    
        harga.append("1500")
        jumlah.append(banyak_potong[i]*int("1500"))

    elif kode[i]==3 :
        print("-"*10)
        print("Sate Sapi")
        print("-"*10)
        banyak_potong.append(int(input("Banyak Tusuk : ")))
        print()
        jenis_potong.append("Sate Sapi")    
        harga.append("2000")
        jumlah.append(banyak_potong[i]*int("2000"))

    else :
        jenis_potong.append("Kode Salah")    
        harga.append("0")
        jumlah.append(banyak_potong[i]*int("0"))

    i=i+1

print("-"*60)        
print("******** SATE KARI'EYEM *********")
print("-"*60)
print("Kode       Jenis Sate        Harga       Banyak      Jumlah")
print("                            PerTusuk     Jenis       Harga")
print("-"*60)

x=0
while x < banyak_jenis:
    print("%i       %s           %s          %i           %i" % (x+1,jenis_potong[x], harga[x], banyak_potong[x], jumlah[x]))
    x = x + 1
print("-"*60)    

jumbay=sum(jumlah)

if jumbay > 50000 :
    diskon=jumbay*10/100

else :
    diskon=0

total_bayar=jumbay-diskon

print("                                       Jumlah Bayar : ",int(jumbay))
print("                                       Diskon       : ",int(diskon))
print("                                       Total Bayar  : ",int(total_bayar))