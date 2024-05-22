#author__thea_uy
#date_may_05_2024
#Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two objects from Class TV 

#import module
import random

#create a class named TV
class TV():

    #parameter constructor where in:
    #status defines the current state of the television (on/off)
    #volume refers to the volume of the television
    #channel_list has a channel from 1 to 120
    #current_channel has no current channel

    def __init__(self, status = "OFF", volume = 0, channel_list = list(range(1,121)), current_channel = None):

        self.status = status
        self.volume = volume
        self.channel_list = channel_list
        self.current_channel = current_channel

#create a method that turns on the television
    def turn_on(self):
        if self.status == "ON":
            print("TV is already turned on.")
        else:
            self.status = "ON"
            print("TV will turn on.")

#create a method that turns off the television
    def turn_off(self):
        if self.status == "OFF":
            print("TV is already turned off.")
        else:
            self.status = "OFF"
            print("TV will turn off.")
    

#create a method that allows that user to change the volume settings
    def volume_settings(self):
        while True:
            try:
                volume = input("Volume 1-7 \nVolume down '<' \nVolume up '>' \nExit 'e' \nChoose:")
                for answer in range(len(volume)):
                    volume = ord(volume[answer]) #convert the input volume to the decimal equivalent of ascii
                    volume = int(volume) #convert to integer

                if volume == 101: #"101" decimal equivalent of character "e" in ascii
                    break #exits the loop for volume settings

                if volume == 60: #"60" decimal equivalent of character "<"in ascii. 
                    if self.volume <=1: #minimum volume 
                        print("Min Volume: 1") 
                    else:
                        self.volume -=1 #reduce volume given that the volume is not less than or equal to one
                        print("Current Volume:",self.volume)

                if volume == 62: #"62" decimal equivalent of character ">" in ascii
                    if self.volume >=7: #maximum volume 
                        print("Max volume: 7")
                    else:
                        self.volume +=1
                        print("Current Volume:",self.volume) #raise the volume given that the volume is not greater than or equal to seven
                
                if 1<=volume<=7: #is the user chose a specific volume
                    self.volume = volume
                    print("Current volume: ",self.volume)
                
            except ValueError:
                print("Unknown Command")
                continue
            
        

#create a method that allows the user to change the channel settings
    def channel_settings(self):
        while True:
            try:
                channel = input("Channel 1-120 \nChannel up '>' \nChannel down '< \nRandom Channel 'r' \nExit 'e' \nChoose: ")
                for answer in range(len(channel)):
                    channel = ord(channel[answer]) #convert the channel input into the decimal equivalent of ascii
                    channel = int(channel) #convert to integer
                
                if channel == 101:
                    break

                if channel == 60:
                    if self.current_channel == 1:
                        print("There are no more channel lower than this.")
                    else:
                        self.current_channel -= 1 
                        print("Current Channel: ", self.current_channel)
                
                if channel == 62:
                    if self.current_channel >=120:
                        print("There are no more channel beyond this.")
                    else:
                        self.current_channel +=1
                        print("Current channel: ", self.current_channel)
                
                if 1<=channel<121:
                    self.current_channel = channel -1
                
                if channel == 114:
                    random_number = random.randint(0, len(self.channel_list) -1)
                    self.current_channel = self.channel_list[random_number]
                    print("Current Channel: ",self.current_channel)
            except ValueError:
                print("Unknown Command")

    #Create a method that allows that user to change channel list settings
    def channel_list_settings(self):
        while True:
            try:
                channel_list = str(input("Change Channel Name 'c' \nAdd Channel 'a' \nChoose"))
                channel_list = channel_list.lower()

                if channel_list == "c":
                    channel_name = input("Enter a channel name: ")
                    channel_number = int(input("Enter the channel number: "))
                    self.channel_list[channel_number - 1] = channel_name
                    print(f"Channel name was successfully changed \nChannel number:{channel_number} \nChannel Name: {channel_name}")
                    break
                
                elif channel_list == "a":
                    add_channel_name = input("Enter a channel name: ")
                    self.channel_list.append(add_channel_name)
                    break
            
            except ValueError:
                print("Unknonw Command")
    
    #Create a method that will return the length of channel list
    def __len__(self):
        return len(self.channel_list)
    
    #Create a method that will return all information
    def __len__(self):
    	return "---All the information---\nTV Current Status: {}\nTV Current Volume: {}\nTV Channel List: {}\nTV Current Channel: {}".format(self.status, self.volume, self.channel_list, self.current_channel)

                
    


