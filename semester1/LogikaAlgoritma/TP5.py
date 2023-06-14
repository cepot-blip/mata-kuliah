print("=====================================")
print("\t ---- Bintang 5 ----")
print("=====================================")
m=6 # DEKLARASI VARIABLE M UNTUK MENAMPUNG NILAI 6
for n in range(0,m): #  PERULANGAN DENGAN RANGE 0-6
    for o in range(0,m): #  PERULANGAN DENGAN RANGE 0-6
                print("",end=" ") #  OUTPUT SPASI
    for k in range(0,n): #  PERULANGAN DENGAN RANGE 0-N
                print("*",end=" ")   #  OUTPUT BINTANG
    m=m-1 #  DEKRIMEN VARIABLE M
    print() #  OUTPUT ENTER

print("=====================================")
print("\t  ---- $ Dolar 10 ----")
print("=====================================")

m=11 # DEKLARASI VARIABLE M UNTUK MENAMPUNG NILAI 11
for n in range(0,m): #  PERULANGAN DENGAN RANGE 0-11
    for o in range(0,m): #  PERULANGAN DENGAN RANGE 0-11
        print("",end=" ") #  OUTPUT SPASI
    for k in range(0,n): #  PERULANGAN DENGAN RANGE 0-N
        print("$",end=" ")   #  OUTPUT DOLAR 
    m=m-1 #  DEKRIMEN VARIABLE M
    print() #  OUTPUT ENTER