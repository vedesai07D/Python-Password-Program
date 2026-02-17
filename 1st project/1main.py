import newpass
import encryption
import skull
import save_file
skull

inp1 = input("Do you wanna Login or Signup?:").lower()

if inp1 != "login" and inp1 != "signup":
    print("Please choose a valid option")

elif inp1 == "signup":
    username = input("Enter Username of your choice: ")

    #usr_pas = encryption.encryp(newpass.password())    # For not encrp. and getting correct login Comment this line and
    save_file.save(username, newpass.password())                    # write "newpass.password()" insted of "use_pas"

# Its giving error from here (login) fix it.
else:
    username = input("Enter your Username: ")
    pas = input("Enter your Password: ")

    save_file.opn(username,pas)