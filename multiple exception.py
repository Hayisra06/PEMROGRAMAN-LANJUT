def main():
	print("PROGRAM PEMBAGIAN BILANGAN")

	try:
		a = float(input("Masukan a: "))
		b = float(input("Masukan b: "))

		hasil = a / b

	except ZeroDivisionError:
		print("\nERROR: Nilai b tidak boleh 0")

	except ValueError:
		print("\nERROR : a dan b harus berupa angka")

	except KeyboardInterrupt:
		print("\nERROR: Jangan tekan Ctrl+C!")
	else:
		print("\na : ",a)
		print("b : ",b)
		print("a/b= ", hasil)

if __name__ == "__main__":
	main()
