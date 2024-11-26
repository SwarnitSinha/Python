import time
import sys
from tqdm import tqdm

class Laptop:

        listOfCompatibleOs : dict = {'windows', 'linux', 'mac'}

        def __init__(self, brand: str, size: str, processor: str,owner: str = None, os: str = 'Windows' ) -> None:
                self.brand = brand
                self.size = size
                self.processor = processor
                self.owner = owner if owner else brand
                self.os = os
                self.password = None

        # Getter for 'owner'
        @property
        def owner(self) -> str:
                return self._owner

    # Setter for 'owner'
        @owner.setter
        def owner(self, value: str):
                self._owner = value
                print(f"Owner has been updated to {value}")

        @owner.setter
        def owner(self, value: str):
                self._owner = value

        def getInfo(self) -> None:
                print("")
                print("\tLaptop specification! : ")
                print("\tThis laptop belongs to ", self.owner)
                print(f"\t{self.brand} {self.size} {self.processor}")
                print(f"\tIt has operating System : {self.os}")
                print("")

        def updateSystem(self) -> None:
                print("System is updating... Don't switch off the laptop")
        
        def installOperatingSystem(self, newOs  : str) -> bool :
                if newOs.lower() in Laptop.listOfCompatibleOs : 
                        """ CODE for changing terminal using sys library
                        symbol : str = '/'
                        cur = 0
                        time_to_wait = 8; #for 8 sec the process will; continue
                        while(cur < time_to_wait):
                                # sys.stdout.write(f"\rChanging the Operating System... {symbol}")
                                # sys.stdout.flush()
                                if symbol == '/' : symbol = '\\'
                                else: symbol = '/'
                                time.sleep(0.5)
                                cur += 1
                        """
                        print("Changing the Operating System...")
                        for _ in tqdm(range(100), desc="Installing", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}%"):
                                time.sleep(0.08)  # Simulate the installation process
                        
                        self.os = newOs;
                        print(f"\n\t\tOperating System changed! Enjoy your {newOs}")
                        return True
                else:
                        print(f"Error: {newOs} is not compatible for this device.")
                        return False

listOfLaptops = ['Lenovo', 'HP', "ASUS", "Mac Book", "Dell"]

def showLaptopCollection() -> None:
    print("Our Laptops:")
    for i in range(len(listOfLaptops)):  # Use range() for iterating over indices
        print(f"\t{i+1}. {listOfLaptops[i]}")  # Use indexing to access elements
    return

purchasedLaptop = []

def purchaseLaptop() -> None:
        print("MAKE PURCHASE")
        brandName : str = input("Which brand you prefer?")
        screenSize : str = input("Which screen size?")
        processor : str = input("Which processor you prefer?")

        laptop : Laptop = Laptop(brandName, screenSize,processor)
        purchasedLaptop.append(laptop)
        print("\n\nCongratulations on your new Laptop!!! BINGO!\n\n")
        print("\n\nSetup your new Laptop\n\n")
        setupLaptop(laptop)
        return

def setupLaptop(laptop : Laptop) -> None:
        while(True):
                print("Select Menu: \n\t 1. Get Information of Your Current Laptop.\n\t 2. Change your Operating System.")
                menucount = 4
                if(laptop.password is not None) :
                        print(f"\t 3. Change Password.")
                else:
                        print("\t 3. Create Account.")
                print(f"\t 4. Setup Done.")
                try:
                        optionSelected = int(input("Enter Option: "))
                except ValueError :
                        print("Enter valid number!")
                if optionSelected == 1 :
                        laptop.getInfo()
                elif optionSelected == 2 :
                        newOs : str = input("Which operating system you want: ")
                        laptop.installOperatingSystem(newOs)
                elif optionSelected == 3 :
                        if (laptop.password is None):
                                userName : str = input("Username: ")
                                password : str = input("Password: ")
                                laptop.owner = userName
                                laptop.password =password
                                # processing()
                                print("\tYour Account has been Created!")
                        else:
                                oldPassword = input("Enter old Password: ")
                                if(oldPassword == laptop.password):
                                        newPassword = input("Enter new Password: ")
                                        laptop.password = newPassword
                                        symbol : str = '/'
                                        cur = 0
                                        time_to_wait = 3; #for 3 sec the process will; continue
                                        while(cur < time_to_wait):
                                                sys.stdout.write(f"\rChanging Password... {symbol}")
                                                sys.stdout.flush()
                                                if symbol == '/' : symbol = '\\'
                                                else: symbol = '/'
                                                time.sleep(0.5)
                                                cur += 1
                                        
                                        print("\tYour password has been updated.")
                                else:
                                        print("\tYou entered wrong password!")
                else:
                        print("You have completed the SETUP.")
                        break

def customerExit() -> None:
        print("Thank you for visiting! Have a good day.")

def startApplication() -> None :
        print("Welcome to Laptop Shop")

        while True: 
                print("1. Check our Laptop Collection.")
                if len(purchasedLaptop) > 0:
                        print("2. See details of Purchased Laptop.")
                else:
                        print("2. Purchase a laptop")
                print("3. Checkout.")
                optionSelected = input("ENTER A OPTION: ")
                if(optionSelected == '1'):
                        showLaptopCollection()
                elif(optionSelected == '2'):
                        #purchase
                        if len(purchasedLaptop) > 0:
                                purchasedLaptop[0].getInfo()
                        else:
                                purchaseLaptop()
                else:
                        customerExit()
                        break



                
startApplication()