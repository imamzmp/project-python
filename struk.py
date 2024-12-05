class Kasir:
    def __init__(self):
        self.items = {}  
        self.customer_name = ""

    def tambah_barang(self, nama, harga):
        self.items[nama] = harga

    def tampilkan_barang(self):
        print("\nDaftar Barang:")
        for nama, harga in self.items.items():
            print(f"{nama}: Rp {harga}")
        print()

    def input_pelanggan(self):
        self.customer_name = input("Masukkan nama pelanggan: ")

    def transaksi(self):
        self.tampilkan_barang()
        belanjaan = {}
        while True:
            barang = input("Masukkan nama barang (atau ketik 'selesai' untuk selesai): ")
            if barang.lower() == "selesai":
                break
            if barang not in self.items:
                print("Barang tidak ditemukan, silakan pilih dari daftar.")
                continue
            jumlah = int(input(f"Masukkan jumlah untuk {barang}: "))
            belanjaan[barang] = jumlah
        
        total = sum(self.items[barang] * jumlah for barang, jumlah in belanjaan.items())
        print(f"\nTotal harga yang harus dibayar: Rp {total}")

        pembayaran = int(input("Masukkan jumlah uang yang dibayarkan: "))
        if pembayaran >= total:
            kembalian = pembayaran - total
            print("----------STRUK PEMBAYARAAN----------")
            print("\n=== BAKSO BERKAH ===")
            print("jl.ahmad yani no.21 Pemalang")
            print(f"Nama Pelanggan: {self.customer_name}")
            for barang, jumlah in belanjaan.items():
                print(f"{barang} x{jumlah} = Rp {self.items[barang] * jumlah}")
            print(f"Total: Rp {total}")
            print(f"Pembayaran: Rp {pembayaran}")
            print(f"Kembalian: Rp {kembalian}")
        else:
            print("Uang yang dibayarkan tidak cukup.")

def main():
    kasir = Kasir()
    kasir.tambah_barang("Bakso Rudal", 20000)
    kasir.tambah_barang("Bakso Mercon", 15000)
    kasir.tambah_barang("Bakso Ranjau", 23000)
    kasir.tambah_barang("(Bakso Spesial Mix)", 35000)
    kasir.tambah_barang("Es Teh", 5000)
    kasir.tambah_barang("Air Mineral", 3000)
    
    print("=== BAKSO BERKAH ===")
    print("jl.ahmad yani no.21 Pemalang")
    kasir.input_pelanggan()
    kasir.transaksi()

if __name__ == "__main__":
    main()
