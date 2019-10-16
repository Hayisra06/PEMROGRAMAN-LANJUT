import kerucut
def main():
	r = 50
	s = 20
	t = 30
	
	print("Hitunglah Volume kerucut")
	print("r = ", r)
	print("s = ", s)

	volume = kerucut.volume(r,s)

	print("Volume dari r=",r, "dan s=",s, volume)

	print(100*"=")

	luasSelimut = kerucut.luasSelimut(r,s)

	print("Luas Selimut dari r=",r, "dan s=",s, luasSelimut)

	print(100*"=")


	luasPermukaan = kerucut.luasPermukaan(r,t)

	print("Luas Permukaan dari r=",r, "dan t=",t, luasPermukaan)

	print(100*"=")

	

if __name__=="__main__":
	main()
