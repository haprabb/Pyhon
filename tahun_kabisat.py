
#menginput tahun
Tahun = int(input("Masukkan tahun : "))
#menggunakan int karena memasukkan angka

#menghitung tahun apakah kabisat atau bukan
if Tahun % 400 == 0:
    print("{} Merupakan tahun kabisat".format(Tahun))

elif Tahun % 100 == 0:
    print("{} Bukan tahun Kabisat".format(Tahun))

elif Tahun % 4 == 0:
    print("{} Bukan tahun kabisat".format(Tahun))

else:
    print("{} Bukan tahun Kabisat".format(Tahun))
 

