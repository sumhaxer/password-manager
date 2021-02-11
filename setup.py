def main():
	with open("passwords.txt", "w") as f:
		f.close()
	
	with open("key.pass", "w") as f:
		data = ".\n"
		f.write(data)
		f.close()
if __name__ == "__main__":
	main()
