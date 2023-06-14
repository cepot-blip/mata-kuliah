#   Project rogram Penjualan Sate

def FormatRupiah (angka):
    if type (angka) != type (1):
        angka = int (angka)
    hasil = 'Rp. ' + format (angka, ',.2f')
    return hasil
