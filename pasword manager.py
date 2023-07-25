import os

def add_password(website, username, password):
    with open("passwords.txt", "a") as f:
        f.write(f"{website} | {username} | {password}\n")
        print(f"Password for {website} added successfully!")

def get_password(website):
    with open("passwords.txt", "r") as f:
        for line in f:
            if website in line:
                return line.split("|")[2].strip()
        return "Password not found."

def delete_password(website):
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
    with open("passwords.txt", "w") as f:
        for line in lines:
            if website not in line:
                f.write(line)
    print(f"Password for {website} deleted successfully!")

def display_passwords():
    with open("passwords.txt", "r") as f:
        for line in f:
            print(line.strip())

def main():
    choice=1
    while 1:
        print("Welcome to Password Manager!")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Delete Password")
        print("4. Display Passwords")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(website, username, password)
        elif choice == "2":
            website = input("Enter website: ")
            password = get_password(website)
            print(f"Password for {website}: {password}")
        elif choice == "3":
            website = input("Enter website: ")
            delete_password(website)
        elif choice == "4":
            display_passwords()
        elif choice == "5":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
