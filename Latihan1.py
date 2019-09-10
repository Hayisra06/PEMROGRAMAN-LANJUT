class Keliling_Lingkaran(object):
	def __init__(self, pi, r):
		self.pi = pi
		self.jari2 = r

	def hitungKeliling(self) :
		return 2 * self.pi * self.jari2
	def cetakData(self):
		print ('PHI \t:', self.pi, 'cm')
		print ('Jari-jari \t :', self.jari2, 'am')
		
	def cetakKeliling(self) :
		print ('Keliling Lingkaran \t :', self.hitungKeliling(),'cm')

class Luas_Lingkaran(object):
	def __init__(self, pi1, r1):
		self.pi = pi1
		self.jari2 = r1

	def hitungLuas(self) :
		return  self.pi * self.jari2 * self.jari2

		print ('PHI \t:', self.pi)
		print ('Jari-jari \t :', self.jari2)

	def cetakData(self):
		print ('PHI \t:', self.pi, 'cm')
		print ('Jari-jari \t :', self.jari2, 'cm')
		
	def cetakLuas(self) :
		print ('Luas Lingkaran \t :', self.hitungLuas(),'cm')

def main ():
	print ('\nHASIL METODE CLASS KE-1 (KELILING)')
	print ('-----------------------------------------------------------------')
	Lingkaran1 = Keliling_Lingkaran(22/7, 7)

	print ('\nKeliling Lingkaran 1')
	Lingkaran1.cetakData()
	Lingkaran1.cetakKeliling()


	Lingkaran2 = Keliling_Lingkaran(22/7, 14)

	print ("\nKeliling Lingkaran 2")
	Lingkaran2.cetakData()
	Lingkaran2.cetakKeliling()


	print ('\nHASIL METODE CLASS KE-2 (LUAS)')
	print ('-----------------------------------------------------------------')
	Lingkaran1 = Luas_Lingkaran(22/7, 21)

	print ("\nLuas Lingkaran 1")
	Lingkaran1.cetakData()
	Lingkaran1.cetakLuas()

	Lingkaran2 = Luas_Lingkaran(22/7, 28)

	print ("\nLuas Lingkaran 2")
	Lingkaran2.cetakData()
	Lingkaran2.cetakLuas()


if __name__=="__main__":
	main()

