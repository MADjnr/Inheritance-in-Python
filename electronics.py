### Three classes
## Electronics
    ## Computer
    ##TV
            #Desktop and Laptop

##include attributes and method
'''
class Electronics:


    def __init__(self, model, year_of_production):
        self.model = model
        self.year_of_production = year_of_production

##Define several methods


class Computer(Electronics):

    def __init__(self, model, year_of_production, name_of_computer):
    Electronics.__init__(self, model, year_of_production)
    self.name_of_computer = name_of_computer
'''


class ElectronicDevice:

    def __init__(self, voltage, weight, height, color):
        self.voltage = voltage
        self.weight = weight
        self.height = height
        self.color = color

class TV(ElectronicDevice):

    def __init__(self, voltage, weight, height, color, max_num_channels ):
        ElectronicDevice.__init__(self, voltage, weight, height, color)
        self.max_num_channels = max_num_channels

class Computer(ElectronicDevice):


    def __init__(self, voltage, weight, height, color, memory, hard_drive):
        ElectronicDevice.__init__(self, voltage, weight, height, color)
        self.memory = memory
        self.hard_drive = hard_drive

class Desktop(Computer):

    def __init__(self, voltage, weight, height, color, memory, hard_drive , monitor_size):
        Computer.__init__(self, voltage, weight, height, color, memory, hard_drive )
        self.monitor_size = monitor_size

class Laptop(Computer):

    def __init__(self, voltage, weight, height, color, memory, hard_drive , has_mouse_pad):
        Computer.__init__(self, voltage, weight, height, color, memory, hard_drive )
        self.has_mouse_pad = has_mouse_pad