from plant import Plant
from system import PlantIRS

class Interface():
    @staticmethod
    def start():
        system = PlantIRS()
        system.load_data()
        print("***********************************************************")
        print("*Welcome to the Plant Data Retrieval System*")
        print("***********************************************************")
        
        input = -1
        while input != 0:
            input = input(("What would you like to do?\n[1] Print all Plants\n[2] Find the average of an Attribute\n[3] Make a Graph of an Attribute\n[0] Exit Program"))

            if input = 1:
                system.print_plants()
            elif input == 2:
                input2 = 0
                input2 = input(("What attribute would you like to find the average of?\n[0]"))