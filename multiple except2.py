def main():
	print("PROGRAM PEMBAGIAN BILANGAN")

	try:
		a = float(input("Masukan a: "))
		b = float(input("Masukan b: "))

		hasil = a / b

	except(ZeroDivisionError, ValueError, KeyboardInterrupt):
		print("\nERROR: Anda telah melakukan Kesalahan")

	else: 
		print("\na : ",a)
		print("b : ",b)
		print("a/b= ", hasil)

if __name__ == "__main__":
	main()
