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

password()
