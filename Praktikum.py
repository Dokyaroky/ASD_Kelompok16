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


def urutkan_menu(stock_dict):
    urutan = input("Urutkan berdasarkan (nama/jenis/harga/stok): ").strip().lower()
    if urutan not in ["nama", "jenis", "harga", "stok"]:
        print("Pilihan urutan tidak valid.")
        return
    sorted_menu = sorted(stock_dict.items(), key=lambda x: x[1][urutan.capitalize()])
    for i, (nama, data) in enumerate(sorted_menu, start=1):
        print(f"{i}. {data['Nama']} | Jenis : {data['Jenis']} | Harga : {data['Harga']} | Stok : {data['Stok']}")


def simpan_data():
    simpan_file(file, stock_dict)


def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    menu = baca_file(file)

    while True:
        print("\n=== MENU CAFE ===")
        print("1. Tampilkan semua menu")
        print("2. Cari menu")
        print("3. Tambah menu")
        print("4. Urutkan menu")
        print("5. Ubah stok menu")
        print("6. Hapus menu")
        print("7. Ubah harga menu")
        print("8. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Silahkan pilih: ").strip()

        if pilihan == "1":
            tampilkan_semua(menu)
        elif pilihan == "2":
            cari_menu(menu)
        elif pilihan == "3":
            tambah_menu(menu)
        elif pilihan == "4":
            urutkan_menu(menu)
        elif pilihan == "5":
            ubah_stok(menu)
        elif pilihan == "6":
            hapus_menu(menu)
        elif pilihan == "7":
            ubah_harga(menu)
        elif pilihan == "8":
            simpan_file(file, menu)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid.")


if _name_ == "_main_":
    main()