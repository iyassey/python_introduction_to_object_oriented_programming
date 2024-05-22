#author__thea_uy
#date_may_05_2024
#Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two objects from Class TV 

#import module
import random
import time

#create a class named TV
class TV():

    #parameter constructor where in:
    #status defines the current state of the television (on/off)
    #volume refers to the volume of the television
    #channel_list has a channel from 1 to 120
    #current_channel has no current channel

    def __init__(self, status = "OFF", volume = 0, channel_list = list(range(1,121)), current_channel = 1):

        self.status = status
        self.volume = volume
        self.channel_list = channel_list
        self.current_channel = current_channel

#create a method that turns on the television
    def turn_on(self):
        if self.status == "ON":
            print("TV is already turned on. \n")
        else:
            self.status = "ON"
            print("TV will turn on. \n")

#create a method that turns off the television
    def turn_off(self):
        if self.status == "OFF":
            print("TV is already turned off. \n")
        else:
            self.status = "OFF"
            print("TV will turn off. \n")
    

#create a method that allows that user to change the volume settings
    def volume_settings(self):
        while True:
            try:
                volume = input("Volume 1-7 \nVolume down '<' \nVolume up '>' \nExit 'e' \nChoose: ")
                for answer in range(len(volume)):
                    volume = ord(volume[answer]) #convert the input volume to the decimal equivalent of ascii
                    volume = int(volume) #convert to integer

                if volume == 101: #"101" decimal equivalent of character "e" in ascii
                    break #exits the loop for volume settings

                if volume == 60: #"60" decimal equivalent of character "<"in ascii. 
                    if self.volume <=1: #minimum volume 
                        print("Min Volume: 1 \n") 
                    else:
                        self.volume -=1 #reduce volume given that the volume is not less than or equal to one
                        print("Volume Level: ",self.volume, "\n")

                if volume == 62: #"62" decimal equivalent of character ">" in ascii
                    if self.volume >=7: #maximum volume 
                        print("Max volume: 7 \n")
                    else:
                        self.volume +=1
                        print("Volume Level:",self.volume ,"\n") #raise the volume given that the volume is not greater than or equal to seven
            except:
                print("Unknown Command \n")
                continue

    
    def choose_volume_number(self):
        while True:
            try:
                volume_level = int(input("Enter volume level: 1-7 \nEnter 10 to exit: "))
                if 1<=volume_level<=7:
                    self.volume = volume_level
                    print("Volume Level: ", self.volume, "\n")
                elif volume_level == 10:
                    print("\n")
                    break
            except:
                print("Invalid Input \n")
                continue
                
#create a method that allows the user to change the channel settings
    def channel_settings(self):
        while True:
            try:
                channel = input("Channel 1-120 \nChannel up '>' \nChannel down '< \nRandom Channel 'r' \nExit 'e' \nChoose: ")
                for answer in range(len(channel)):
                    channel = ord(channel[answer]) #convert the channel input into the decimal equivalent of ascii
                    channel = int(channel)

                if channel == 101: #101 is the decimal equivalent of str 'e' in ascii
                    break

                if channel == 60: #60 is the decimal equivalent of str '<' in ascii
                    if self.current_channel == 1:
                        print("There are no more channel lower than this. \n")
                    else:
                        self.current_channel -= 1 
                        print("Current Channel: ",self.current_channel,"\n")
                
                if channel == 62: #62 is the decimal equivalent of str '>' in ascii 
                    if self.current_channel >=120:
                        print("There are no more channel beyond this.\n")
                    else:
                        self.current_channel +=1
                        print("Current channel: ", self.current_channel,"\n")
                
                if channel == 114: #114 is the decimal equivalent of 'r'
                    random_number = random.randint(0, len(self.channel_list) -1)
                    self.current_channel = self.channel_list[random_number]
                    print("Current Channel: ",self.current_channel, "\n")
            except:
                print("Unknown Command \n")
    
    #Create a method  that allows the user to choose a channel number
    def choose_channel_number(self):
        while True:
            try:
                get_length_of_channel_list = len(self.channel_list)
                channel_number = int(input(f"Enter channel number 1-{get_length_of_channel_list}: \nEnter 0 to exit: \nChoose: "))
                if 1<=channel_number<=get_length_of_channel_list:
                    self.current_channel = channel_number
                    print("Current Channel: ",self.channel_list[self.current_channel-1],"\n")
                elif channel_number == 0:
                    print("\n")
                    break
            except:
                print("\n")
                continue

    #Create a method that allows that user to change channel list settings
    def channel_list_settings(self):
        while True:
            try:
                channel_list = str(input("Change Channel Name 'c' \nAdd Channel 'a' \nShow Channel List 'l' \nExit 'e' \nChoose: "))
                channel_list = channel_list.lower()

                if channel_list == "c":
                    channel_name = input("Enter a channel name: ")
                    channel_number = int(input("Enter the channel number: "))
                    self.channel_list[channel_number - 1] = channel_name
                    print(f"Channel name was successfully changed \nChannel number:{channel_number} \nChannel Name: {channel_name} \n")
                
                elif channel_list == "a":
                    add_channel_name = input("Enter a channel name: ")
                    self.channel_list.append(add_channel_name)
                    print(f"Channel {add_channel_name} was successfully added in the channel list \n")
                
                elif channel_list == "l":
                    print(self.channel_list)
                
                elif channel_list == "e":
                    break
            
            except:
                print("Unknonw Command \n")
    
    def tv_information_1(self):
        print(f"""
        --------------TV1 INFORMATION--------------
        Current Status:{self.status}
        Volume Level:{self.volume}
        Current Channel:{self.current_channel}
        """)
    
    def tv_information_2(self):
        print(f"""
        --------------TV2 INFORMATION--------------
        Current Status:{self.status}
        Volume Level:{self.volume}
        Current Channel:{self.current_channel}
        """)
    
    #Create a method that will return the length of channel list
    def __len__(self):
        return len(self.channel_list)
    
    #Create a method that will return all information
    def __str__(self):
    	return "---All the information---\nTV Current Status: {}\nTV Current Volume: {}\nTV Channel List: {}\nTV Current Channel: {}".format(self.status, self.volume, self.channel_list, self.current_channel)




