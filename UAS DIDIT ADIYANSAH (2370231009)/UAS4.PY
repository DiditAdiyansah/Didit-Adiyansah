# Program penjualan kasir

# Buat list untuk menyimpan item yang dijual
daftar_item = []

# Buat fungsi untuk menambahkan item ke daftar
def tambah_item(nama, harga):
  daftar_item.append({'nama': nama, 'harga': harga})

# Buat fungsi untuk menghitung total harga
def hitung_total():
  total = 0
  for item in daftar_item:
    total += item['harga']
  return total

# Buat fungsi untuk menampilkan struk
def tampilkan_struk():
  for item in daftar_item:
    print(item['nama'], '\t', item['harga'])
  print('Total \t\t', hitung_total())

# Selanjutnya, kita akan meminta input dari pengguna untuk menambahkan item ke daftar
while True:
  nama = input("Masukkan nama item: ")
  if nama == 'selesai':
    break
  harga = int(input("Masukkan harga item: "))
  tambah_item(nama, harga)

# Setelah semua item ditambahkan, tampilkan struk
tampilkan_struk()

# Selesai!
