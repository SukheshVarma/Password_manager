def encrypt(text):
    encrypted=''
    for letter in text:
        encrypted+=chr(ord(letter)+3)
    return encrypted

def decrypt(text):
    decrypted=''
    for letter in text:
        decrypted+=chr(ord(letter)-3)
    return decrypted
def add_entry():
    website=input("Enter website name")
    username=input("Enter username")
    password=input("Enter the password")
    encrypted_password=encrypt(password)

    with open ("data.txt","a") as file:
        file.write(website + "|" + username + "|" + encrypted_password + "\n")
    print("PASSWORD SAVED SUCCESSFULLY!")

def view():
    try:
     with open ("data.txt","r") as file:
        print("\n--- Saved Passwords ---")
        for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    website=parts[0]
                    username=parts[1]
                    encrypted_password=parts[2]
                    decrypted_password = decrypt(encrypted_password)

                    print(" Website:", website)
                    print(" Username:", username)
                    print(" Password:", decrypted_password)
                    print("----------------------")
    except FileNotFoundError:
        print("No saved passwords found.")
def main():
    MASTER_PASSWORD = "admin123"
    entered_password = input("Enter master password to access the manager: ")

    if entered_password != MASTER_PASSWORD:
        print("Incorrect master password. Access denied.")
        return

    while True:
        print("\n===== Password Manager Menu =====")
        print("1. Add New Password")
        print("2. View Saved Passwords")
        print("3. Update passsword")
        print("4.EXIT")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view()
        elif choice == "4":
            print("Exiting Password Manager. Goodbye!")
            break
        elif choice =="3":
            update()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
def update():
    sd = input("Enter the username for which you want to change the password: ")
    new_password = input("Enter new password: ")

    lines = []
    updated = False

    with open("data.txt", "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) < 3:
                lines.append(line)
                continue

            if sd == parts[1]:
                encrypted_new_password = encrypt(new_password)
                parts[2] = encrypted_new_password
                updated = True
                print(f"Password updated for user {sd}")

            lines.append("|".join(parts) + "\n")

    if not updated:
        print("Username not found.")
        return

    with open("data.txt", "w") as file:
        file.writelines(lines)

main()
        