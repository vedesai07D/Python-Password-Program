import random
import string


def password():
    print("\t\t\t\tPassword Program")
    print("="*80)
    print("Rules for password: \n1.Minimum Length should be 7 Charecters\n2.Need one Lowecase Alphabet\n3.Need one Uppercase Alphabet\n4.Need one number\n5.Need one Special Charecter(not space)\n")
    print("="*80)
    check = True
    check_pass = 0
    valid = True
    while check:

        pas = str(input("Enter a password: "))
        print("-"*60)

        if " " in pas:                                                 # Spaces condition
            print("Password must not contain spaces")
            continue

        if len(pas)<=6:                                                # Length Condition
            print("-"*60 + "\nEnter Password with 7 or more charecters")

        else:
            for i in pas:                                               # Lowercase loop
                if i.islower():
                    break
            else:
                    print("Enter a Lowercase Charecter in your Password")
                    valid = False

            for i in pas:                                               # Uppercase Loop
                if i.isupper():
                    break
            else:
                print("Enter a Uppercase Charecter in your Password")
                valid = False

            for i in pas:                                               # Integer Loop
                if i.isnumeric():
                    break
            else:
                print("Enter a Integer in your Password")
                valid = False

            for i in pas:                                               # Special Char Loop
                if i.isalpha():
                    continue
                elif i.isnumeric():
                    continue
                else:
                    check_pass = pas

            if check_pass != pas:                                       # Speecial Char Condition
                    print("Enter a Special Charecter in your Password")
            elif valid:
                print("-"*60)
                newpas = str(input("Re-Enter your Password: "))
                print("-"*60)

                if newpas == pas:                                       # Re-Enter Condition
                    print("Yeppe!!, Your Account has been created")
                    check = False
                    return pas
                else:
                    print("Incorrect Password Re-Entered")
                    return 0

        print("="*80)


def encryp(pas):
    chars = string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    cyper = list()

    key = chars.copy()
    random.shuffle(key)

    for letter in pas:
        index = chars.index(letter)
        cyper += key[index]

    return cyper



inp1 = input("Do you wanna Login or Signup?:").lower()

if inp1 != "login" and inp1 != "signup":
    print("Please choose a valid option")

elif inp1 == "signup":
    username = input("Enter Username of your choice: ")

    with open("passwords.txt", "a") as file:           
        # r=read only, w=overwrite, a=continue write
        usr_pas = encryp(password())
        file.write(f"{username}|{usr_pas}\n")

# Its giving error from here (login) fix it.
else:                                                   
    username = input("Enter your Username: ")
    pas = input("Enter your Password: ")
    
    with open("passwords.txt", "r") as file:
        if username in file.read(username) and pas in file.read(pas):
            print("Details..........")
        else:
            print("Invalid creditials")