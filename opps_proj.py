from colorama import Fore, Style
import colorama

class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.login = False
        self.menu()

    def menu(self):
        user_input = input(colorama.Fore.GREEN + colorama.Style.BRIGHT + """
            Welcome to chatbook😊, How would you like to proceed?""" + colorama.Fore.BLUE + colorama.Style.BRIGHT + """
            1. Press 1 to Sign Up """ + colorama.Fore.YELLOW + colorama.Style.BRIGHT + """
            2. Press 2 to Login """ + colorama.Fore.GREEN + colorama.Style.BRIGHT + """
            3. Press 3 to write a post """ + colorama.Fore.CYAN + colorama.Style.BRIGHT + """
            4. Press 4 to send a message to a friend """ + colorama.Fore.RED + colorama.Style.BRIGHT + """
            5. Press any other key to exit \n""" + colorama.Fore.GREEN + colorama.Style.BRIGHT + """->
        """)

        if user_input == "1":
            self.sign_up()
        
        elif user_input == "2":
            self.sign_in()

        elif user_input == "3":
            self.write_post()

        elif user_input == "4":
            self.send_message()

        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Exiting the program...")
            exit()
    
    def sign_up(self):
        email = input(colorama.Fore.BLUE + colorama.Style.BRIGHT + "Enter your email: ")
        pwd = input(colorama.Fore.BLUE + colorama.Style.BRIGHT + "Enter your password: ")
        self.username = email
        self.password = pwd
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "Sign up successful!")
        print("\n")
        self.menu()

    def sign_in(self):
        if self.username == "" and self.password == "":
                print(colorama.Fore.RED + colorama.Style.BRIGHT + "Please sign up first from menu by pressing 1!")
        else:
            uname = input(colorama.Fore.BLUE + colorama.Style.BRIGHT + "username: ")
            pwd = input(colorama.Fore.BLUE + colorama.Style.BRIGHT + "password: ")
            if self.username == uname and self.password == pwd:
                print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "Login successful!")
                self.login = True
                self.menu()
            else:
                print(colorama.Fore.RED + colorama.Style.BRIGHT + "Invalid username or password!")
                    
        print("\n")
        self.menu()

    def write_post(self):
        if self.login == True:
            txt = input(colorama.Fore.BLUE + colorama.Style.BRIGHT + "Enter your post: ")
            print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "Post successful!")
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Please login first from menu by pressing 2!")
        
        print("\n")
        self.menu()

    def send_message(self):
        if self.login == True:
            txt = input(colorama.Fore.BLUE + colorama.Style.BRIGHT + "Enter your message: ")
            frnd = input(colorama.Fore.BLUE + colorama.Style.BRIGHT + "Enter your friend's username: ")
            print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"Message sent to {frnd}!")
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT + "Please login first from menu by pressing 2!")
        
        print("\n")
        self.menu()

obj = chatbook()