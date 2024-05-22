#this file is contains the main method for python file television_settings

#import modules
from television_settings import *


#Create the object "tv1" and "tv2"
tv1 = TV()
tv2 = TV()

#Create a method that will allow the user to change the television settings
#Create a method that will allow the user to change the settings of tv 1

def change_settings_tv1():
    print("""
        --------------TV1 SYSTEM--------------
        1. ON
        2. OFF
        3. Change Volume Level by 1
        4. Choose Volume Number
        5. Change Channel by 1
        6. Change Channel Number
        7. Channel Settings
        8. TV Info
        9. Exit TV1 Settings 
        10. Shut down
    """)
    while True:
        try:
            tv_command = input("Enter your command: ")

            if tv_command == "10":
                tv1.tv_information_1()
                print("Thank you for using my program")
                exit()

            elif tv_command == "9":
                print("Exiting tv1 settings")
                break

            elif tv_command == "1":
                tv1.turn_on()
            
            elif tv_command == "2":
                tv1.turn_off()
            
            elif tv_command == "3":
                tv1.volume_settings()
            
            elif tv_command == "4":
                tv1.choose_volume_number()
            
            elif tv_command == "5":
                tv1.channel_settings()

            elif tv_command == "6":
                tv1.choose_channel_number()
            
            elif tv_command == "7":
                tv1.channel_list_settings()
            
            elif tv_command == "8":
                tv1.tv_information_1()
            
            else:
                print("Invalid Command \n")
                continue
        except ValueError:
            continue

#Create a method that will allow the user to change the settings of tv 2

def change_settings_tv2():
    print("""
        --------------TV2 SYSTEM--------------
        1. ON
        2. OFF
        3. Change Volume Level by 1
        4. Choose Volume Number
        5. Change Channel by 1
        6. Change Channel Number
        7. Channel Settings
        8. TV Info
        9. Exit TV1 Settings 
        10. Shut down
    """)
    while True:
        try:
            tv_command = input("Enter your command: ")

            if tv_command == "10":
                tv2.tv_information_2()
                print("Thank you for using my program")
                exit()

            elif tv_command == "9":
                print("Exiting tv2 settings")
                break

            elif tv_command == "1":
                tv2.turn_on()
            
            elif tv_command == "2":
                tv2.turn_off()
            
            elif tv_command == "3":
                tv2.volume_settings()
            
            elif tv_command == "4":
                tv2.choose_volume_number()
            
            elif tv_command == "5":
                tv2.channel_settings()

            elif tv_command == "6":
                tv2.choose_channel_number()
            
            elif tv_command == "7":
                tv2.channel_list_settings()
            
            elif tv_command == "8":
                tv2.tv_information_2()
            
            else:
                print("Invalid Command \n")
                continue
        except ValueError:
            continue
	
#Create the main method
def main():
    print("""
        --------------TV--------------
        1. TV1
        2. TV2
        3. TV1 Information
        4. TV2 Information
        5. Exit
    """)

    while True:
        try:
            answer = int(input("Choose: "))
            if answer == 1:
                television_settings = change_settings_tv1()

            elif answer == 2:
                television_settings = change_settings_tv2()

            elif answer == 3:
                television_settings = tv1.tv_information_1()

            elif answer == 4:
                television_settings = tv2.tv_information_2()

            elif answer == 5:
                print("Thank you for using my program!")
                exit()
            else:
                continue
        except ValueError:
            print("Unknown Command")

main()