from urllib.request import urlopen

def main():

	with open("main.py", "w") as f:
		data = urlopen("https://raw.githubusercontent.com/sumhaxer/password-manager/main/main.py")
		f.write(data.read().decode())
		f.close()

if __name__ == "__main__":
	main()
