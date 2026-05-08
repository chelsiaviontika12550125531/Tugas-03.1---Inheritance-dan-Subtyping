# =========================================
# SISTEM MANAJEMEN SUMBER DAYA MANUSIA (HRD)
# Menggunakan:
# - Inheritance
# - Encapsulation
# - super()
# - Method Overriding
# - Subtyping / Polymorphism
# =========================================


# =========================
# CLASS INDUK
# =========================
class Pegawai:

    # Constructor
    def __init__(self, nama_pegawai, id_pegawai, gaji_pokok):

        self.nama_pegawai = nama_pegawai
        self.id_pegawai = id_pegawai

        # Encapsulation (private attribute)
        self.__gaji_pokok = gaji_pokok


    # Getter
    def get_gaji_pokok(self):
        return self.__gaji_pokok


    # Method menghitung gaji
    def hitung_gaji(self):
        return self.__gaji_pokok


    # Method menampilkan informasi pegawai
    def tampil_info(self):

        print("=" * 45)
        print("        DATA PEGAWAI")
        print("=" * 45)

        print(f"Nama Pegawai : {self.nama_pegawai}")
        print(f"ID Pegawai   : {self.id_pegawai}")
        print(f"Jabatan      : Pegawai Biasa")
        print(f"Gaji Total   : Rp {self.hitung_gaji():,}")

        print("=" * 45)


# =========================
# SUBCLASS MANAGER
# =========================
class Manager(Pegawai):

    def __init__(self,
                 nama_pegawai,
                 id_pegawai,
                 gaji_pokok,
                 bonus_jabatan,
                 divisi):

        # Mengambil constructor parent
        super().__init__(nama_pegawai,
                         id_pegawai,
                         gaji_pokok)

        self.bonus_jabatan = bonus_jabatan
        self.divisi = divisi


    # Override method
    def hitung_gaji(self):
        return self.get_gaji_pokok() + self.bonus_jabatan


    # Method khusus manager
    def kelola_tim(self):

        print(f"\n{self.nama_pegawai} sedang mengelola divisi {self.divisi}")


    # Override tampil_info
    def tampil_info(self):

        print("=" * 45)
        print("          DATA MANAGER")
        print("=" * 45)

        print(f"Nama Pegawai : {self.nama_pegawai}")
        print(f"ID Pegawai   : {self.id_pegawai}")
        print(f"Jabatan      : Manager")
        print(f"Divisi       : {self.divisi}")
        print(f"Bonus        : Rp {self.bonus_jabatan:,}")
        print(f"Gaji Total   : Rp {self.hitung_gaji():,}")

        print("=" * 45)


# =========================
# SUBCLASS PROGRAMMER
# =========================
class Programmer(Pegawai):

    def __init__(self,
                 nama_pegawai,
                 id_pegawai,
                 gaji_pokok,
                 bahasa_pemrograman,
                 uang_lembur):

        # Mengambil constructor parent
        super().__init__(nama_pegawai,
                         id_pegawai,
                         gaji_pokok)

        self.bahasa_pemrograman = bahasa_pemrograman
        self.uang_lembur = uang_lembur


    # Override method
    def hitung_gaji(self):
        return self.get_gaji_pokok() + self.uang_lembur


    # Method khusus programmer
    def coding(self):

        print(f"\n{self.nama_pegawai} sedang membuat aplikasi menggunakan {self.bahasa_pemrograman}")


    # Override tampil_info
    def tampil_info(self):

        print("=" * 45)
        print("        DATA PROGRAMMER")
        print("=" * 45)

        print(f"Nama Pegawai : {self.nama_pegawai}")
        print(f"ID Pegawai   : {self.id_pegawai}")
        print(f"Jabatan      : Programmer")
        print(f"Skill Utama  : {self.bahasa_pemrograman}")
        print(f"Uang Lembur  : Rp {self.uang_lembur:,}")
        print(f"Gaji Total   : Rp {self.hitung_gaji():,}")

        print("=" * 45)


# =========================
# FUNGSI SUBTYPING
# =========================
def tampilkan_data_pegawai(pegawai):

    # Semua subclass bisa diperlakukan
    # sebagai object Pegawai
    pegawai.tampil_info()



# =========================
# MEMBUAT OBJECT
# =========================

# Pegawai biasa
pegawai1 = Pegawai(
    "Siti Nurhaliza",
    "PG001",
    5000000
)

# Manager
manager1 = Manager(
    "Andi Saputra",
    "MN001",
    8000000,
    2500000,
    "Human Resource Development"
)

# Programmer
programmer1 = Programmer(
    "Budi Santoso",
    "PR001",
    7000000,
    "Python",
    1500000
)



# =========================
# MENJALANKAN PROGRAM
# =========================

print("\nSISTEM MANAJEMEN HRD PERUSAHAAN\n")


# Subtyping berjalan di sini
tampilkan_data_pegawai(pegawai1)
tampilkan_data_pegawai(manager1)
tampilkan_data_pegawai(programmer1)


# Method khusus subclass
manager1.kelola_tim()
programmer1.coding()