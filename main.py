from plant import Plant
from system import PlantIRS
from interface import Interface

system = PlantIRS()
system.load_data()
interface = Interface()
interface.start()