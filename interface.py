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