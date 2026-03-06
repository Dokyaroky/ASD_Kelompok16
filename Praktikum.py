file = "MenuCafe.txt"
stock_dict = {}

def baca_file(nama_file):
    data = {}
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip()
                if not baris:
                    continue
                try:
                    nama, jenis, harga, stok = baris.split(",")
                    data[nama.lower()] = {
                        "Nama": nama,
                        "Jenis": jenis,
                        "Harga": int(harga),
                        "Stok": int(stok)
                    }
                except ValueError:
                    print(f"Format salah pada baris: {baris}")
    except FileNotFoundError:
        print("File tidak ditemukan, akan dibuat baru.")
    return data


def simpan_file(nama_file, stock_dict):
    with open(nama_file, "w", encoding="utf-8") as f:
        for key in stock_dict:
            data = stock_dict[key]
            nama = data["Nama"]
            jenis = data["Jenis"]
            harga = data["Harga"]
            stok = data["Stok"]
            f.write(f"{nama},{jenis},{harga},{stok}\n")

def tampilkan_semua(stock_dict):
    if not stock_dict:
        print("Menu sedang kosong")
        return
    print("\nMenu Cafe")
    print("=" * 62)
    print((f"{'Nama Makanan' : <31} | {'Jenis' : <10} | {'Harga' : <8} | {'Stok' : <10}"))
    print("=" * 62)
    for i, (key, data) in enumerate(stock_dict.items(), start=1):
        print(f"{str(i)+'.' : <5} {data['Nama'] : <25} | {data['Jenis'] : <10} | {data['Harga'] : <8} | {data['Stok'] : <10}")