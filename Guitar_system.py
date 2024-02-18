class Guitar():
    def __init__(self, price, brand, model, type, color, magnetic_sort, serial_number):
        self.price = price
        self.brand = brand
        self.model = model
        self.type  = type
        self.color = color
        self.magnetic_sort = magnetic_sort
        self.serial_number = serial_number

    def show_info(self):
        print(f"""
            Guitar İnfo:
                Brand: {self.brand}
                Model: {self.model}
                Type: {self.type}
                Color: {self.color}
                Magnetic: {self.magnetic_sort}
                Price: {self.price}
                Serial Number: {self.serial_number}
        """)

    def update(self):
        new_price = int(input("New Price: "))
        new_brand = input("New brand: ")
        new_model = input("New Model: ")
        new_type = input("New Type: ")
        new_color = input("New Color: ")
        new_magnetic = input("New magnetic sorting: ")
        new_serial_number = input("New Serial Number: ")
        if new_price:
            self.price = new_price
        elif new_brand:
            self.brand = new_brand
        elif new_model:
            self.model = new_model
        elif new_type:
            self.type = new_type
        elif new_color:
            self.color = new_color
        elif new_magnetic:
            self.magnetic_sort = new_magnetic
        elif new_serial_number:
            self.serial_number = new_serial_number


class Amplifier():
    def __init__(self, price, brand, model, watt, serial_number):
        self.price = price
        self.brand = brand
        self.model = model
        self.watt = watt
        self.serial_number = serial_number

    def show_info(self):
        print(f"""
            Amphi İnfo:
                Brand: {self.brand}
                Model: {self.model}
                Watt: {self.watt}
                Price: {self.price}
                Serial Number: {self.serial_number}
        """)

    def update(self):
        new_price = int(input("New Price: "))
        new_brand = input("New brand: ")
        new_model = input("New Model: ")
        new_watt = input("New Watt: ")
        new_serial_number = input("New Serial Number: ")
        if new_price:
            self.price = new_price
        elif new_brand:
            self.brand = new_brand
        elif new_model:
            self.model = new_model
        elif new_watt:
            self.watt = new_watt
        elif new_serial_number:
            self.serial_number = new_serial_number



class JackCable():
    def __init__(self, price, brand, model, length, serial_number):
        self.price = price
        self.brand = brand
        self.model = model
        self.length = length
        self.serial_number = serial_number

    def show_info(self):
        print(f"""
            Jack Cable İnfo:
                Brand: {self.brand}
                Model: {self.model}
                Length: {self.length}
                Price: {self.price}
                Serial Number: {self.serial_number}
        """)

    def update(self):
        new_price = int(input("New Price: "))
        new_brand = input("New brand: ")
        new_model = input("New Model: ")
        new_length = input("New Length: ")
        new_serial_number = input("New Serial Number: ")
        if new_price:
            self.price = new_price
        elif new_brand:
            self.brand = new_brand
        elif new_model:
            self.model = new_model
        elif new_length:
            self.length = new_length
        elif new_serial_number:
            self.serial_number = new_serial_number

class User():
    def __init__(self, name, surname, username, password):
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.cart = []
        self.apply_cart = False
        self.is_login = False



    def show_user_info(self):
        print(f"{self.username}'s info:")
        print(f"""
            Name: {self.name}
            Surname: {self.surname}
            Username: {self.username}
            Password: ***** (You have to be an admin too see user's password)
        """)

    def update_user(self):
        password_ = input("Please write your password to change your info: ")
        if password_ == self.password:
            new_name = input("Please write new name: ")
            new_surname = input("Please write new surname: ")
            new_username = input("Please write new username: ")
            new_password = input("Please write new password: ")
            if new_name:
                self.name = new_name
            elif new_surname:
                self.surname = new_surname
            elif new_username:
                self.username = new_username
            elif new_password:
                self.password = new_password
        else:
            print("Password is uncorrect.")

    def dev_show_info_user(self):
        print(f"""
            Name: {self.name}
            Surname: {self.surname}
            Username: {self.username}
            Password: {self.password} (Don't share anyone)
        """)

class MusicStore():
    def __init__(self):
        self.users = []
        self.guitars = []
        self.amps = []
        self.jacks = []
        self.admin_mode = False
        self.admin_name = "Arda"
        self.admin_password = "1234"

    def add_guitar(self):
        print("Please write info of the guitar: ")
        brand = input("Brand: ")
        model = input("Model: ")
        type_ = input("Type: ")
        color = input("Color: ")
        magnetic = input("Magnetic Sorting: ")
        serial_number = input("Serial Number: ")
        price = int(input("Price: "))
        guitar = Guitar(price, brand, model, type_, color, magnetic, serial_number)
        self.guitars.append(guitar)
        print(f"{guitar.brand} {guitar.model} successfully added the system.")


    def add_amphi(self):
        print("Please write info of the amplifier")
        brand = input("Brand: ")
        model = input("Model: ")
        watt = input("Watt: ")
        serial_number = input("Serial Number: ")
        price = int(input("Price: "))
        amp = Amplifier(price, brand, model, watt, serial_number)
        self.amps.append(amp)
        print(f"{amp.brand} {amp.model} successfully added the system.")

    def add_jack(self):
        print("Please write info of the Jack Cable")
        brand = input("Brand: ")
        model = input("Model: ")
        length = input("Length: ")
        serial_number = input("Serial Number: ")
        price = int(input("Price: "))
        cable = JackCable(price, brand, model, length, serial_number)
        self.jacks.append(cable)
        print(f"{cable.brand} {cable.model} successfully added the system.")

    def add_user(self):
        print("Please write the info of the user: ")
        name = input("Name: ")
        surname = input("Surname: ")
        username = input("Username: ")
        password = input("Password: ")
        password2 = input("Verify Password: ")
        if password2 == password:
            user = User(name, surname, username, password)
            self.users.append(user)
            print(f"{user.name} {user.surname} added the user's successfully")

    def show_all_guitars(self):
        if len(self.guitars) == 0:
            print("There is no guitars in the system.")
        else:
            print("Guitars:")
            for guitar in self.guitars:
                print(f"{guitar.brand}-{guitar.model}")

    def show_all_amps(self):
        if len(self.amps) == 0:
            print("There is no amplifier's in the system.")
        else:
            print("Amplifiers:")
            for amplifier in self.amps:
                print(f"{amplifier.brand}-{amplifier.model}")


    def show_all_cable(self):
        if len(self.jacks) == 0:
            print("There is no Jack Cables in the system.")
        else:
            print("Cables:")
            for jackcable in self.jacks:
                print(f"{jackcable.brand}-{jackcable.model}")

    def show_all_users(self):
        if len(self.users) == 0:
            print("There is no users in the system.")
        else:
            for user in self.users:
                print(f"{user.name} {user.surname}  ({user.username})")

    def search_guitar(self):
        search_g = input("Please write the model of guitar: ")
        for guitar in self.guitars:
            if search_g == guitar.model:
                guitar.show_info()


    def search_amphi(self):
        search_a = input("Please write the model of amplifier: ")
        for amplifier in self.amps:
            if search_a == amplifier.model:
                amplifier.show_info()


    def search_cable(self):
        search_c = input("Please write the model of jack cable: ")
        for jackcable in self.jacks:
            if search_c == jackcable.model:
                jackcable.show_info()


    def search_user(self):
        search_u = input("Please write the username of the user: ")
        for user in self.users:
            if search_u == user.username:
                if self.admin_mode:
                    user.dev_show_info_user()
                else:
                    user.show_user_info()


    def delete_guitar(self):
        delete_g = input("Please write the Serial Number of guitar: ")
        for guitar in self.guitars:
            if delete_g == guitar.serial_number:
                print(f"{guitar.brand} {guitar.model} successfully removed")
                self.guitars.remove(guitar)


    def delete_amp(self):
        delete_a = input("Please write serial of the amplifier: ")
        for amplifier in self.amps:
            if delete_a == amplifier.serial_number:
                print(f"{amplifier.brand} {amplifier.model} successfully deleted")
                self.amps.remove(amplifier)


    def delete_cable(self):
        delete_c = input("Please write Serial Number of the cable: ")
        for jackcable in self.jacks:
            if delete_c == jackcable.serial_number:
                print(f"{jackcable.brand} {jackcable.model} succcessfully deleted")
                self.jacks.remove(jackcable)


    def update_guitar(self):
        search_g = input("Please write Serial Number of guitar: ")
        for guitar in self.guitars:
            if search_g == guitar.serial_number:
                print("İf you cold leave it blank it will be the same")
                guitar.update()


    def update_amp(self):
        search_a = input("Please write Serial Number of amplifier: ")
        for amplifier in self.amps:
            if search_a == amplifier.serial_number:
                print("İf you cold leave it blank it will be the same")
                amplifier.update()


    def update_jack(self):
        search_c = input("Please write Serial Number of jack cable: ")
        for jackcable in self.jacks:
            if search_c == jackcable.model:
                print("İf you cold leave it blank it will be the same")
                jackcable.update()

    def update_user(self):
        search_u = input("Please write your username: ")
        for user in self.users:
            if search_u == user.username:
                print("İf you cold leave it blank it will be the same")
                user.update_user()

    def login_admin(self):
        password = input("Password: ")
        name = input("Name: ")
        if self.admin_name == name and self.admin_password == password:
            self.admin_mode = True

    def login_user(self):
        username = input("Username: ")
        Password = input("Password: ")
        if username is not True and Password is not True:
            print("Please type somthing.")
        else:
            for user in self.users:
                if username == user.username and Password == user.password:
                    print(f"{user.username} succsessfully logged in.")
                    user.is_login = True
                else:
                    print("Username or password incorrect.")


    def add_cart(self):
        for user in self.users:
            if user.is_login:
                cart = input("Please write product model to buy: ")
                for guitar in self.guitars:
                    if cart == guitar.model:
                        print(f"{guitar.brand} {guitar.model} successfully added the cart")
                        user.cart.append(guitar)
                        print("Your cart: ")
                        for guitar in user.cart:
                            print(f"\n{guitar.brand}-{guitar.model}")
                    else:
                        print(f"{cart} not found.")
                for jackcable in self.jacks:
                    if cart == jackcable.model:
                        print(f"{jackcable.brand} {jackcable.model} successfully added the cart")
                        user.cart.append(jackcable)
                        print("Your cart:")
                        for jackcable in user.cart:
                            print(f"\n{jackcable.brand}-{jackcable.model}")
                for amplifier in self.amps:
                    if cart == amplifier.model:
                        print(f"{amplifier.brand} {amplifier.model} successfully added the cart")
                        user.cart.append(amplifier)
                        print("Your cart:")
                        for amplifier in user.cart:
                            print(f"\n{amplifier.brand}-{amplifier.model}")
            else:
                print("Please login first.")

    def apply_cart(self):
        total = 0
        for user in self.users:
            if len(user.cart) == 0:
                print("You have to add soomething to the cart.")
            else:
                if user.is_login:
                    for item in user.cart:
                        total += item.price
                        print("İNFO: AFTER THAT YOU WİLL BE LOGOUT THE SYSTEM")
                        ans = input(f"You have to pay {total}TL to buy the cart do want to apply(y/n): ")
                        if ans == "y":
                            user.is_login = False
                            print("You successfully boughth products.")
                            user.cart.clear()
                else:
                    print("You have to login.")
















music_store = MusicStore()

try:
    while True :
        print("*"*20, "Music Store", "*"*20)
        print("""
            Transactions:
                1. Add Guitar
                2. Add Amplifier
                3. Add Jackcable
                4. Show All Guitars
                5. Show All Amplifiers
                6. Show All Jackcables
                7. Search Guitar
                8. Search Amplifier
                9. Search Jackcable
                10. Delete Guitar
                11. Delete Amplifier
                12. Delete Jackcable 
                13. Update Guitar
                14. Update Amplifier
                15. Update Jackcable
                16. Sign User
                17. Login
                18. Show All Users
                19. Became Admin
                20. Search User
                21. Update User
                22. Add To Cart
                23. Apply Cart
                24. Quit (q-Q)
                
                
                
                    
        """)
        proc = input("Please write process number (1-16): ")
        if proc == "1":
            music_store.add_guitar()
        elif proc == "2":
            music_store.add_amphi()
        elif proc == "3":
            music_store.add_jack()
        elif proc == "4":
            music_store.show_all_guitars()
        elif proc == "5":
            music_store.show_all_amps()
        elif proc == "6":
            music_store.show_all_cable()
        elif proc == "7":
            music_store.search_guitar()
        elif proc == "8":
            music_store.search_amphi()
        elif proc == "9":
            music_store.search_cable()
        elif proc == "10":
            music_store.delete_guitar()
        elif proc == "11":
            music_store.delete_amp()
        elif proc == "12":
            music_store.delete_cable()
        elif proc == "13":
            music_store.update_guitar()
        elif proc == "14":
            music_store.update_amp()
        elif proc == "15":
            music_store.update_jack()
        elif proc == "16":
            music_store.add_user()
        elif proc == "17":
            music_store.login_user()
        elif proc == "18":
            music_store.show_all_users()
        elif proc == "19":
            music_store.login_admin()
        elif proc == "20":
            music_store.search_user()
        elif proc == "21":
            music_store.update_user()
        elif proc == "22":
            music_store.add_cart()
        elif proc == "23":
            music_store.apply_cart()
        elif proc == "24" or proc == "q" or proc == "Q":
            print("Exiting the system.")
            break
        else:
            print("You write something wrong")
except ValueError:
    print("Please write a integer value to price")
    print("Please restart system...")




















