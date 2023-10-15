print("="*20)
print("LOGIN")
print("="*20)
nama = input("masukan nama: ")
nim = int(input("masukan nim: "))
prodi = input("masukan prodi/kelas: ")
print(f"hallo {nama}, {nim}, {prodi} Selamat datang di program kami !!")

print("="*20)
print("PROGRAM NILAI TUKAR MATA UANG RUPIAH")
print("="*20)


def idr_to_USD(jumlah_idr):
    USD_in_idr = 15000
    hasil_USD = jumlah_idr / USD_in_idr
    return hasil_USD

def idr_to_YEN(jumlah_idr):
    YEN_in_idr = 100
    hasil_YEN = jumlah_idr / YEN_in_idr
    return hasil_YEN

def idr_to_RINGGIT(jumlah_idr): 
    RINGGIT_in_idr = 3000
    hasil_RINGGIT = jumlah_idr / RINGGIT_in_idr
    return hasil_RINGGIT 

jumlah_idr = float(input("Masukan jumlah uang Anda dalam rupiah: "))

print("Pilih jenis mata uang yang ingin Anda konversi: ")
print("1. USD")
print("2. YEN")
print("3. RINGGIT")
pilihan = int(input("Masukan pilihan (1/2/3): "))


if pilihan == 1:
    hasil_USD = idr_to_USD(jumlah_idr)
    print(f"Hasil konversi ke USD: {hasil_USD} USD")
elif pilihan == 2:
    hasil_YEN = idr_to_YEN(jumlah_idr)
    print(f"Hasi konversi ke YEN: {hasil_YEN} JPY")
elif pilihan == 3:
    hasil_RINGGIT = idr_to_RINGGIT(jumlah_idr)
    print(f"Hasil konversi ke RINGGIT: {hasil_RINGGIT} MYR")  
else:
    print("Pilihan tidak valid. Silahkan pilih 1, 2, 3.")




print(f"Terima Kasih telah menggunakan program kami. Hope it help <3")

    























