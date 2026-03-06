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


def cari_menu(stock_dict):
    nama = input("\nMasukkan nama menu: ").strip().lower()
    if nama in stock_dict:
        data = stock_dict[nama]
        print("Menu ditemukan!")
        print(f"Menu : {data['Nama']} | Jenis : {data['Jenis']} | Harga : {data['Harga']} | Stok : {data['Stok']}")
    else:
        print("Menu tidak ditemukan!")

def tambah_menu(stock_dict):
    nama = input("Masukkan nama menu baru: ").strip()
    key = nama.lower()
    if key in stock_dict:
        print("Nama menu sudah digunakan.")
        return
    jenis = input("Masukkan jenis menu: ").strip()
    try:
        harga = int(input("Masukkan harga menu: "))
        stok = int(input("Masukkan stok menu: "))
    except ValueError:
        print("Harga dan stok harus angka.")
        return
    stock_dict[key] = {
        "Nama": nama,
        "Jenis": jenis,
        "Harga": harga,
        "Stok": stok
    }
    simpan_file(file, stock_dict)
    print(f"Menu '{nama}' berhasil ditambahkan.")


def ubah_harga(stock_dict):
    nama = input("Masukkan nama menu yang ingin diubah harganya: ").strip().lower()
    if nama not in stock_dict:
        print("Menu tidak ditemukan.")
        return
    try:
        harga_baru = int(input("Masukkan harga baru: "))
    except ValueError:
        print("Harga harus angka.")
        return
    nama_menu = stock_dict[nama]["Nama"]
    stock_dict[nama]["Harga"] = harga_baru
    simpan_file(file, stock_dict)
    print(f"Harga menu '{nama_menu}' berhasil diubah menjadi {harga_baru}.")


def ubah_stok(stock_dict):
    nama = input("Masukkan nama menu yang ingin diubah stoknya: ").strip().lower()
    if nama not in stock_dict:
        print("Menu tidak ditemukan.")
        return
    try:
        stok_baru = int(input("Masukkan stok baru: "))
    except ValueError:
        print("Stok harus angka.")
        return
    nama_menu = stock_dict[nama]["Nama"]
    stock_dict[nama]["Stok"] = stok_baru
    simpan_file(file, stock_dict)
    print(f"Stok menu '{nama_menu}' berhasil diubah menjadi {stok_baru}.")


def hapus_menu(stock_dict):
    nama = input("Masukkan nama menu yang ingin dihapus: ").strip().lower()
    if nama in stock_dict:
        nama_menu = stock_dict[nama]["Nama"]
        del stock_dict[nama]
        simpan_file(file, stock_dict)
        print(f"Menu '{nama_menu}' berhasil dihapus.")
    else:
        print("Menu tidak ditemukan.")


