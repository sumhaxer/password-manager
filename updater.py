from urllib.request import urlopen

def main():

	with open("main.py", "w") as f:
		print("downloading...")
		data = urlopen("https://raw.githubusercontent.com/sumhaxer/password-manager/main/main.py")
		print("writing")
		f.write(data.read().decode())
		f.close()
		print("done!")

if __name__ == "__main__":
	main()
