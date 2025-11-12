from plant import Plant
import csv
class PlantIRS():
    def __init__(self):
        self._plant_list = []

    def load_data(self):
        with open("plant_health_data.csv") as csv_file:
            reader = csv.reader(csv_file)
            unique_id = 1
            for row in reader:
                if row[0] == "Timestamp":
                    pass
                else:
                    plant = Plant()
                    timestamp = row[0]
                    plant_id = row[1]
                    soil_moisture = row[2]
                    ambient_temperature = row[3]
                    soil_temperature = row[4]
                    humidity = row[5]
                    light_intensity = row[6]
                    soil_ph = row[7]
                    nitrogen_level = row[8]
                    phosphorus_level = row[9]
                    potassium_level = row[10]
                    chlorophyll_content = row[11]
                    electrochemical_signal = row[12]
                    plant_health_status = row[13]
                    plant = Plant(timestamp, plant_id, soil_moisture, ambient_temperature, soil_temperature, humidity, light_intensity, soil_ph, nitrogen_level, phosphorus_level, potassium_level, chlorophyll_content, electrochemical_signal, plant_health_status, unique_id)
                    self._plant_list.append(plant)
                    unique_id += 1
    
    def add_plant(self, plant):
        self._plant_list.append(plant)

    def average(self):
        pass
    
    def print_plants(self):
        for plant in self._plant_list:
            print(plant)

    # def graphs...
