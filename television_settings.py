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

#define the parameters of the constructor


#create a method that turns on the television

#create a method that turns off the television

#create a method that allows that user to change the volume settings

#create a method that alllows that user to change the channel settings
