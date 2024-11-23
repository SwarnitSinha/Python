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
                print("Laptop specification! : ")
                print("This laptop belongs to ", self.owner)
                print(f"{self.brand} {self.size} {self.processor}")
                print(f"It has operating System : {self.os}")

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
                
def startApplication() -> None :
        print("Welcome to Laptop Shop")
        print("Purchase a laptop")
        brandName : str = input("Which brand you prefer?")
        screenSize : str = input("Which screen size?")
        processor : str = input("Which processor you prefer?")

        laptop : Laptop = Laptop(brandName, screenSize,processor)
        print("\n\nCongratulations on your new Laptop!!! BINGO!\n\n")

        exit: bool = False
        while(exit == False):
                print("Select Menu: \n\t 1. Get Information of Your Current Laptop.\n\t 2. Change your Operating System.\n\t 3. Create Account.")
                menucount = 4
                if(laptop.password is not None) :
                        print(f"\t {menucount}. Change Password.")
                        menucount+=1
                print(f"\t {menucount}. EXIT")
                try:
                        optionSelected = int(input("\t"))
                except ValueError :
                        print("Enter valid number!")
                if optionSelected == 1 :
                        laptop.getInfo()
                elif optionSelected == 2 :
                        newOs : str = input("Which operating system you want: ")
                        laptop.installOperatingSystem(newOs)
                elif optionSelected == 3 :
                        userName : str = input("Username: ")
                        password : str = input("Password: ")
                        laptop.owner = userName
                        laptop.password =password
                elif optionSelected==4 and menucount==5:
                        oldPassword = input("Enter old Password: ")
                        if(oldPassword == laptop.password):
                                newPassword = input("Enter new Password: ")
                                laptop.password = newPassword
                                print("Your password has been updated.")
                        else:
                                print("You entered wrong password!")
                else:
                        print("Thank you for visiting! Have a good day.")
                        exit = True;



                
startApplication()