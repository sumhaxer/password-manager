try:
    import os
    from cryptography.fernet import Fernet
    import hashlib
    from colorama import Fore, Style, init
    import base64

except ImportError:
    print("I require some libraries you don't have installed!") # this will only execute if you are running the .py file
    ask = input("Do you want to install them [Y/N]? ")

    if ask.lower() == "y":
        """
		install missing packages
		"""
        os.system("pip install cryptography")
        os.system("pip install colorama")
        os.system("clear"); main()
    else:
        exit()

init() # initialize the colorama library

_version = 1.0

help_page =f"""

====== Commands ======

help     definition: shows this
clear    definition: clears the console
logout   definition: logs out of the account and you have to reenter the password
list     definition: prints out the stored passwords
add      definition: add a password. for more help see below in the examples
remove   defitition: removes a password. for more help see below in the examples
restart  definition: restarts the console
wipe     definition: wipes all the stored passwords
update   definition: updates the password manager
export   definition: export all stored passwords to a file. WARNING: passwords will not be encrypted!


====== Examples ======

{Fore.RED}>>> {Style.RESET_ALL}add test123
password added!

{Fore.RED}>>> {Style.RESET_ALL}add 123abc
password added!

{Fore.RED}>>> {Style.RESET_ALL}list
test123
123abc

{Fore.RED}>>> {Style.RESET_ALL}remove test123
password removed!

{Fore.RED}>>> {Style.RESET_ALL}list
123abc

{Fore.RED}>>> {Style.RESET_ALL}

====== Aliases ======

Only some commands have aliases

the command 'list' can also be called 'ls'
the command 'clear' can also be called 'cls'


======================

"""

def encrypt(text):
    """

    encrypts plain text to unreadable text by utilizing the
    sha512 hashing algorithm.

    """
    return hashlib.sha512(text.encode("utf-8")).hexdigest()

def main():
    """
	defining program entry
    """
    f = open("key.pass", "r")

    if f.read() == ".\n":
        """

        if its the users first time using this program, it will ask them to create a master password,
        the program will create a key out of the master password.
    
        """
        print("Looks like its your first time using this password manager.")
        print("To get started, why don't you go ahead and create a password?")
        password = input("Password: ")
        x = open("key.pass", "w")
        x.write(str(encrypt(password)))
        x.close()
        os.system("clear")
        main()

	else:
		print("Version:", _version) # print version
		print("To continue you have to login!") # ask the user to login
		password = input("Password: ")
		key = hashlib.sha512(password.encode("utf-8")).hexdigest() # generate key from password
		key = base64.urlsafe_b64encode(key.encode("utf-8"))
		os.system("clear")
		f = open("key.pass", "r")

        if encrypt(password) == f.read():
            f.close()

            while True:
                shell = input(f"{Fore.RED}>>> {Style.RESET_ALL}")

                if shell == "list" or shell == "ls":
                    try:
                        passwrd = open("passwords.txt", "r")
                        for line in passwrd.readlines():
                            data = Fernet(key).decrypt(line.encode("utf-8"))
                            print(data.decode())
                        print()
                        passwrd.close()
                        del data

                    except:
                        print("unable to read and decrypt stored passwords!\nHave you changed your master password?\nRead the read me file!")

                elif "add" in shell:
                    with open("passwords.txt", "ab") as i:
                        i.write(Fernet(key).encrypt(shell[4:].encode("utf-8"))+"\n".encode("utf-8"))
                        i.close()
                    print("password added!\n")

                elif shell == "clear" or shell == "cls":
                    os.system("clear")

                elif shell == "help":
                    print(help_page)

                elif shell == "logout":
                    print("Logging out!")
                    os.system("clear")
                    main()

                elif shell == "wipe":
                    ask = input("Are you sure you want to wipe all stored passwords? [Y/N] ")

                    if ask.lower() == "y":
                        print("Enter your master password to confirm its really you!")
                        auth = input("Password: ")

                        if auth == password:
                            with open("passwords.txt","w") as f:
                                f.write("")
                                f.close()
                                print()

                        else:
                            print("Password is not correct!\nCanceling operation!\n")

                    else:
                        print("Operation canceled by user!\n")

                elif shell == "update": print("updating..."); os.system("python3 updater.py"); print("update finished!")

                elif "remove" in shell:
                    print("Command not implemented yet!\n")

                elif shell == "":
                    pass

                elif shell == "restart":
                    os.system("clear")
                    main()

                elif shell == "export":
                    data = []
                    with open("exported passwords.txt", "wb") as ex:
                        f = open("passwords.txt", "rb")
                        for line in f.readlines():
                            data.append(line)

                        f.close()
                        for line in data:
                            ex.write(Fernet(key).decrypt(line))
                            ex.write("\n".encode("utf-8"))

                        ex.close()
                        del data

                else:
                    print("Unknown command!\n")
        else:
            print("Authentication Failure!")
            f.close()
            input()
            os.system("clear")
            main()

if __name__ == "__main__":
	"""
	don't run program when its imported, only when its run by user
	"""
	main()
