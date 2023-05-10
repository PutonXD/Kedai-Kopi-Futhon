class Diskon:
    def __init__(self, harga, jumlah):
        self.harga = harga
        self.jumlah = jumlah

    def hitung_diskon(self):
        if self.jumlah >= 5:
            diskon = int(self.harga * 0.2)
        elif self.jumlah >= 3:
            diskon = int(self.harga * 0.1)
        elif self.jumlah >= 2:
            diskon = int(self.harga * 0.05)
        elif self.harga >= 50000:
            diskon = int(self.harga * 0.1)
        else:
            diskon = 0
        return diskon

pilihan = "y"
while pilihan.lower() == "y":
    print("""
    ==============================
    
    Ananda Coffee
    List Menu Minuman Kopi
 
    ==============================
    A. ES Kopi Susu : Rp 11.000
    B. ES Kopi Coklat : Rp 12.000
    C. ES Kopi Hitam : Rp 11.000
    D. Ice Americano : Rp 14.000
    ==============================
    """)
    pesan = input("Masukkan abjad menu kopi: ").lower()
    jumlah_pesan = int(input("Masukkan jumlah pesanan: "))
    if pesan == "a":
        list_nama = "ES Kopi Susu"
        harga = 11000 * jumlah_pesan
        ppn = int(harga * 0.1)
        diskon = Diskon(harga, jumlah_pesan).hitung_diskon()
        total_harga = int(harga - diskon + ppn)
    elif pesan == "b":
        list_nama = "ES Kopi Coklat"
        harga = 12000 * jumlah_pesan
        ppn = int(harga * 0.1)
        diskon = Diskon(harga, jumlah_pesan).hitung_diskon()
        total_harga = int(harga - diskon + ppn)
    elif pesan == "c":
        list_nama = "ES Kopi Hitam"
        harga = 11000 * jumlah_pesan
        ppn = int(harga * 0.1)
        diskon = Diskon(harga, jumlah_pesan).hitung_diskon()
        total_harga = int(harga - diskon + ppn)
    elif pesan == "d":
        list_nama = "Ice Americano"
        harga = 14000 * jumlah_pesan
        ppn = int(harga * 0.1)
        diskon = Diskon(harga, jumlah_pesan).hitung_diskon()
        total_harga = int(harga - diskon + ppn)
    else:
        list_nama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        total_harga = "-"
        pilihan = input("Menu tidak tersedia, silakan masukkan abjad menu yang tersedia. Silakan ulangi kembali Y/N: ")
 
    print("--------------------------")
    print("Ananda Coffee")
    print("--------------------------")
    print("Menu :", list_nama)
    print("Jumlah Pesan :", jumlah_pesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", total_harga)
    print("--------------------------")
    pilihan = input("Apakah Anda ingin order kembali? Y/N: ").lower()
