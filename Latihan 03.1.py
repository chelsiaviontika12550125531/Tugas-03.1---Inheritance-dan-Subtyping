class Pegawai:
    def __init__(self, nama_pegawai, id_pegawai, gaji_pokok=5000000):
        self.nama_pegawai = nama_pegawai
        self.id_pegawai = id_pegawai
        self.__gaji_pokok = gaji_pokok

    # Getter
    def get_gaji_pokok(self):
        return self.__gaji_pokok

    # Method menghitung gaji
    def hitung_gaji(self):
        return self.__gaji_pokok


class Manager(Pegawai):
    def __init__(self, nama_pegawai, id_pegawai, bonus, divisi):
        super().__init__(nama_pegawai, id_pegawai)
        self.bonus = bonus
        self.divisi = divisi

    # Method hitung bonus
    def hitung_bonus(self):
        return self.get_gaji_pokok() * self.bonus / 100

    # Override method
    def hitung_gaji(self):
        return self.get_gaji_pokok() + self.hitung_bonus()

    # Method khusus manager
    def kelola_tim(self):
        print(f"{self.nama_pegawai} sedang mengelola divisi {self.divisi}")


class Programmer(Pegawai):
    def __init__(self, nama_pegawai, id_pegawai, bahasa_pemrograman, jam_lembur, tarif_lembur):
        super().__init__(nama_pegawai, id_pegawai)
        self.bahasa_pemrograman = bahasa_pemrograman
        self.jam_lembur = jam_lembur
        self.tarif_lembur = tarif_lembur

    # Method hitung uang lembur
    def hitung_uang_lembur(self):
        return self.jam_lembur * self.tarif_lembur

    # Override method
    def hitung_gaji(self):
        return self.get_gaji_pokok() + self.hitung_uang_lembur()

    # Method khusus programmer
    def coding(self):
        print(f"{self.nama_pegawai} sedang coding menggunakan {self.bahasa_pemrograman}")


# ==========================
# PROGRAM UTAMA
# ==========================

daftar_pegawai = []

# List divisi perusahaan
divisi_perusahaan = [
    "Human Resource Development",
    "Keuangan",
    "Pemasaran",
    "Teknologi Informasi",
    "Operasional"
]

# List bonus manager
list_bonus = [5, 10, 15, 20]

# List bahasa pemrograman
list_bahasa = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "PHP"
]

while True:
    print("\n" + "=" * 75)
    print("                    SISTEM MANAJEMEN HRD")
    print("=" * 75)
    print("1. Tambah Pegawai")
    print("2. Tambah Manager")
    print("3. Tambah Programmer")
    print("4. Tampilkan Semua Data")
    print("5. Keluar")
    print("=" * 75)

    pilihan = input("Masukkan pilihan menu : ")

  
    # TAMBAH PEGAWAI

    if pilihan == "1":

        print("\n--- INPUT PEGAWAI ---")

        nama = input("Nama Pegawai : ")
        id_pegawai = input("ID Pegawai   : ")

        pegawai = Pegawai(nama, id_pegawai)

        daftar_pegawai.append(pegawai)

        print("\nPegawai berhasil ditambahkan!")


    # TAMBAH MANAGER

    elif pilihan == "2":

        print("\n--- INPUT MANAGER ---")

        nama = input("Nama Manager : ")
        id_pegawai = input("ID Manager   : ")

        # Pilihan bonus
        print("\nPilih Bonus Manager")
        for i in range(len(list_bonus)):
            print(f"{i+1}. {list_bonus[i]}%")

        pilih_bonus = int(input("Masukkan pilihan bonus : "))
        bonus = list_bonus[pilih_bonus - 1]

        # Pilihan divisi
        print("\nPilih Divisi")
        for i in range(len(divisi_perusahaan)):
            print(f"{i+1}. {divisi_perusahaan[i]}")

        pilih_divisi = int(input("Masukkan nomor divisi : "))
        divisi = divisi_perusahaan[pilih_divisi - 1]

        manager = Manager(nama, id_pegawai, bonus, divisi)

        daftar_pegawai.append(manager)

        print("\nManager berhasil ditambahkan!")


    # TAMBAH PROGRAMMER

    elif pilihan == "3":

        print("\n--- INPUT PROGRAMMER ---")

        nama = input("Nama Programmer : ")
        id_pegawai = input("ID Programmer   : ")

        # Pilihan bahasa pemrograman
        print("\nPilih Bahasa Pemrograman")
        for i in range(len(list_bahasa)):
            print(f"{i+1}. {list_bahasa[i]}")

        pilih_bahasa = int(input("Masukkan pilihan bahasa : "))
        bahasa = list_bahasa[pilih_bahasa - 1]

        jam = int(input("Jam Lembur   : "))
        tarif = int(input("Tarif Lembur : "))

        programmer = Programmer(
            nama,
            id_pegawai,
            bahasa,
            jam,
            tarif
        )

        daftar_pegawai.append(programmer)

        print("\nProgrammer berhasil ditambahkan!")

    # TAMPILKAN SEMUA DATA
    elif pilihan == "4":

        if len(daftar_pegawai) == 0:

            print("\nBelum ada data pegawai!")

        else:

            print("\n" + "=" * 145)
            print("                                      DATA SELURUH PEGAWAI")
            print("=" * 145)

            # Header tabel
            print(f"{'ID':<10} "
                  f"{'NAMA':<20} "
                  f"{'JABATAN':<15} "
                  f"{'DIVISI / SKILL':<30} "
                  f"{'BONUS / LEMBUR':<25} "
                  f"{'GAJI POKOK':<18} "
                  f"{'GAJI TOTAL':<18}")

            print("-" * 145)

            # Isi tabel
            for pegawai in daftar_pegawai:

                # Jika Manager
                if isinstance(pegawai, Manager):

                    bonus_info = f"{pegawai.bonus}% / Rp {pegawai.hitung_bonus():,.0f}"

                    print(f"{pegawai.id_pegawai:<10} "
                          f"{pegawai.nama_pegawai:<20} "
                          f"{'Manager':<15} "
                          f"{pegawai.divisi:<30} "
                          f"{bonus_info:<25} "
                          f"{f'Rp {pegawai.get_gaji_pokok():,}':<18} "
                          f"{f'Rp {pegawai.hitung_gaji():,.0f}':<18}")

                # Jika Programmer
                elif isinstance(pegawai, Programmer):

                    lembur_info = f"{pegawai.jam_lembur} Jam"

                    print(f"{pegawai.id_pegawai:<10} "
                          f"{pegawai.nama_pegawai:<20} "
                          f"{'Programmer':<15} "
                          f"{pegawai.bahasa_pemrograman:<30} "
                          f"{lembur_info:<25} "
                          f"{f'Rp {pegawai.get_gaji_pokok():,}':<18} "
                          f"{f'Rp {pegawai.hitung_gaji():,}':<18}")

                # Jika Pegawai biasa
                else:

                    print(f"{pegawai.id_pegawai:<10} "
                          f"{pegawai.nama_pegawai:<20} "
                          f"{'Pegawai':<15} "
                          f"{'-':<30} "
                          f"{'-':<25} "
                          f"{f'Rp {pegawai.get_gaji_pokok():,}':<18} "
                          f"{f'Rp {pegawai.hitung_gaji():,}':<18}")
            print("=" * 145)

    # KELUAR PROGRAM
    elif pilihan == "5":

        print("\nProgram selesai. Terima kasih!")
        break

    # JIKA INPUT SALAH
    else:

        print("\nPilihan tidak tersedia!")
