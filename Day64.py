class Library:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False

    # register
    def register(self, new_username, new_password):
        self.username = new_username
        self.password = new_password
        print("Registration Successful!")

    # login
    def login(self, username, password):
        if username == self.username and password == self.password:
            self.is_logged_in = True
            print("Login Successful!")
        else:
            print("Invalid username and password.")

    # logout
    def logout(self):
        if self.is_logged_in:
            self.is_logged_in = False
            print("Logout Successful!")
        else:
            print("You are not logged in.")

lib = Library("Akshay", "123")

print("\t\tWelcome to KITABI KONA!\t")

while True:
    print("1: Login \t 2: Register \t 3: Logout \t 4: Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Enter the details!")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            lib.login(username, password)
        case 2:
            print("Enter the details!")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            lib.register(username, password)
        case 3:
            lib.logout()
        case 4:
            print("Exiting the program. Goodbye!")
            exit()
        case _:
            print("Invalid choice. Please try again.")