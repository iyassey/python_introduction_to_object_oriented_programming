#author__thea_uy
#date_may_05_2024
#Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two objects from Class TV 


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
                    volume = ord(volume[answer]) #convert the input volume to the decimanal equivalent of ascii
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
            
        

#create a method that alllows that user to change the channel settings
