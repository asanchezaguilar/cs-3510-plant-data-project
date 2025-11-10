from plant import Plant
import csv
class PlantIRS():
    def __init__(self):
        self._plant_list = []

    def load_data(self):
        with open("plant_health_data.csv") as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                if row[0] == "Timestamp":
                    pass
                else:
                    plant = Plant()
                    plant.timestamp = row[0]
                    plant.plant_id = row[1]
                    plant.soil_moisture = row[2]
                    plant.ambient_temperature = row[3]
                    plant.soil_temperature = row[4]
                    plant.humidity = row[5]
                    plant.light_intensity = row[6]
                    plant.soil_ph = row[7]
                    plant.nitrogen_level = row[8]
                    plant.phosphorus_level = row[9]
                    plant.potassium_level = row[10]
                    plant.chlorophyll_content = row[11]
                    plant.electrochemical_signal = row[12]
                    plant.plant_health_status = row[13]
                    self._plant_list.append(plant)
    
    def add_plant(self, plant):
        self._plant_list.append(plant)

    def average(self):
        pass
    
    def print_plants(self):
        for plant in self._plant_list:
            print(plant)

    # def graphs...
