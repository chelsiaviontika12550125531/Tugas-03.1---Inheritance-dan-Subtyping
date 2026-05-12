class Pegawai:
    def __init__(self, nama_pegawai, id_pegawai, gaji_pokok):
        self.nama_pegawai = nama_pegawai
        self.id_pegawai = id_pegawai
        self.__gaji_pokok = gaji_pokok

    # Getter
    def get_gaji_pokok(self):
        return self.__gaji_pokok

    # Method menghitung gaji
    def hitung_gaji(self):
        return self.__gaji_pokok

    # Method menampilkan informasi pegawai
    def tampil_info(self):
        print("=" * 50)
        print("           DATA PEGAWAI")
        print("=" * 50)
        print(f"Nama Pegawai : {self.nama_pegawai}")
        print(f"ID Pegawai   : {self.id_pegawai}")
        print(f"Jabatan      : Pegawai Biasa")
        print(f"Gaji Pokok   : Rp {self.get_gaji_pokok():,}")
        print(f"Gaji Total   : Rp {self.hitung_gaji():,}")
        print("=" * 50)


class Manager(Pegawai):
    def __init__(self, nama_pegawai, id_pegawai, gaji_pokok, persentase_bonus, divisi):
        super().__init__(nama_pegawai, id_pegawai, gaji_pokok)
        self.persentase_bonus = persentase_bonus
        self.divisi = divisi

    # Method hitung bonus
    def hitung_bonus(self):
        bonus = self.get_gaji_pokok() * self.persentase_bonus / 100
        return bonus

    # Override method
    def hitung_gaji(self):
        return self.get_gaji_pokok() + self.hitung_bonus()

    # Method khusus manager
    def kelola_tim(self):
        print(f"\n{self.nama_pegawai} sedang mengelola divisi {self.divisi}")

    # Override tampil_info
    def tampil_info(self):
        print("=" * 50)
        print("            DATA MANAGER")
        print("=" * 50)
        print(f"Nama Pegawai : {self.nama_pegawai}")
        print(f"ID Pegawai   : {self.id_pegawai}")
        print(f"Jabatan      : Manager")
        print(f"Divisi       : {self.divisi}")
        print(f"Gaji Pokok   : Rp {self.get_gaji_pokok():,}")
        print(f"Bonus        : {self.persentase_bonus}%")
        print(f"Total Bonus  : Rp {self.hitung_bonus():,.0f}")
        print(f"Gaji Total   : Rp {self.hitung_gaji():,.0f}")
        print("=" * 50)


class Programmer(Pegawai):
    def __init__(self, nama_pegawai, id_pegawai, gaji_pokok, bahasa_pemrograman, jam_lembur, tarif_lembur):
        super().__init__(nama_pegawai, id_pegawai, gaji_pokok)
        self.bahasa_pemrograman = bahasa_pemrograman
        self.jam_lembur = jam_lembur
        self.tarif_lembur = tarif_lembur

    # Method hitung lembur
    def hitung_uang_lembur(self):
        return self.jam_lembur * self.tarif_lembur

    # Override method
    def hitung_gaji(self):
        return self.get_gaji_pokok() + self.hitung_uang_lembur()

    # Method khusus programmer
    def coding(self):
        print(f"\n{self.nama_pegawai} sedang membuat aplikasi menggunakan {self.bahasa_pemrograman}")

    # Override tampil_info
    def tampil_info(self):
        print("=" * 50)
        print("           DATA PROGRAMMER")
        print("=" * 50)
        print(f"Nama Pegawai : {self.nama_pegawai}")
        print(f"ID Pegawai   : {self.id_pegawai}")
        print(f"Jabatan      : Programmer")
        print(f"Skill Utama  : {self.bahasa_pemrograman}")
        print(f"Gaji Pokok   : Rp {self.get_gaji_pokok():,}")
        print(f"Jam Lembur   : {self.jam_lembur} Jam")
        print(f"Tarif/Jam    : Rp {self.tarif_lembur:,}")
        print(f"Total Lembur : Rp {self.hitung_uang_lembur():,}")
        print(f"Gaji Total   : Rp {self.hitung_gaji():,}")
        print("=" * 50)

def tampilkan_data_pegawai(pegawai):
    pegawai.tampil_info()

#objek pada kodingan
pegawai1 = Pegawai("Siti Nurhaliza", "PG001", 5000000)
manager1 = Manager("Andi Saputra", "MN001", 8000000, 10, "Human Resource Development")
programmer1 = Programmer("Budi Santoso", "PR001", 7000000, "Python", 20, 75000)

print("\nSISTEM MANAJEMEN HRD PERUSAHAAN\n")
tampilkan_data_pegawai(pegawai1)
tampilkan_data_pegawai(manager1)
tampilkan_data_pegawai(programmer1)

manager1.kelola_tim()
programmer1.coding()