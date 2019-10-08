import sys
def main():
	print ("PROGRAM PEMBAGIAN BILANGAN")

	a =  float(input("Masukan a: "))
	b =  float(input("Masukan b: "))

	try:
		hasil = a/b
	except ZeroDivisionError:
		print ("\nERROR : Nilai b tidak boleh 0")


		print("\na : ", a)
		print("b : ", b)
		print("a / b = ", hasil)
if __name__ == "__main__":
	main()
