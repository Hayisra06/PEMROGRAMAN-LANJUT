#Class Utama
class merek:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
    def Daftar_merek(self):
        print ("Daftar_merek : ", self.A, self.B, self.C, self.D)

#Subclass 1
class yamaha (merek):
    def __init__(self, A, B, C, D ):
        merek.__init__(self, A, B, C, D)
        self.Y = "Motor Yamaha"
    def Mtr(self):
        print("Jenis kendaraan adalah :", self.Y)

#Subclass 2
class suzuki (merek):
    def __init__(self, A, B, C, D ):
        merek.__init__(self, A, B, C, D)
        self.S = "Motor Suzuki"
    def Mtr(self):
        print("Jenis kendaraan adalah :", self.S)

#Subclass 3
class honda (merek):
    def __init__(self, A, B, C, D ):
        merek.__init__(self, A, B, C, D)
        self.H = "Motor Honda"
    def Mtr(self):
        print("Jenis kendaraan adalah :", self.H)

def main():

    #Biodata
    print(20 * "^")
    print("Nama   : Hayisra ")
    print("Kelas  : 1829141008 ")
    print(20 * "^","\n")

    #Pendeklarasian Objek dan memanggil objek dari kelas turunan
    Kendaraan1 = yamaha("Jupiter MX |","Nmax |","Xride |","Mio sporty |")
    Kendaraan1.Daftar_merek()
    Kendaraan1.Mtr()

    print(50*"_","\n")

    Kendaraan2 = suzuki("Thuder |", "Spin 125 |", "Satria F150 |", "Next II |")
    Kendaraan2.Daftar_merek()
    Kendaraan2.Mtr()

    print(50 * "_", "\n")

    Kendaraan2 = honda("Beat |", "Sonic 150 |", "Supra 125 |", "Vario |")
    Kendaraan2.Daftar_merek()
    Kendaraan2.Mtr()

if __name__ == "__main__":
        main()
