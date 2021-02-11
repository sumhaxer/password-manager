from urllib.request import urlopen

with open("main.py", "w") as f:
	data = urlopen("https://raw.githubusercontent.com/sumhaxer/password-manager/main/main.py")
	f.write(data.read().decode())
	f.close()
