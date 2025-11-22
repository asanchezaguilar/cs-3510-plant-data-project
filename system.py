from plant import Plant
import csv
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt


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
                    plant_id = int(row[1])
                    soil_moisture = float(row[2])
                    ambient_temperature = float(row[3])
                    soil_temperature = float(row[4])
                    humidity = float(row[5])
                    light_intensity = float(row[6])
                    soil_ph = float(row[7])
                    nitrogen_level = float(row[8])
                    phosphorus_level = float(row[9])
                    potassium_level = float(row[10])
                    chlorophyll_content = float(row[11])
                    electrochemical_signal = float(row[12])
                    plant_health_status = row[13]
                    plant = Plant(timestamp, plant_id, soil_moisture, ambient_temperature, soil_temperature, humidity, light_intensity, soil_ph, nitrogen_level, phosphorus_level, potassium_level, chlorophyll_content, electrochemical_signal, plant_health_status, unique_id)
                    self._plant_list.append(plant)
                    unique_id += 1
    
    def add_plant(self, plant):
        self._plant_list.append(plant)

    def average(self, attribute):
        plant_count = 0
        attribute_value_count = 0
        for plant in self._plant_list:
            plant_count += 1
            attribute_value_count += getattr(plant, attribute)
        return attribute_value_count/plant_count

    
    def print_plants(self):
        for plant in self._plant_list:
            print(plant)

    def attribute_over_time(self, attribute, plant_id):
        attribute_list = []
        time_stamp_list = []
        for plant in self._plant_list:
            if plant.plant_id == plant_id:
                attribute_list.append(getattr(plant, attribute))
                time_stamp_list.append(plant.timestamp)

        if not attribute_list:
            print(f"No data found for Plant ID {plant_id}")
            return

        # sorts by timestamp if needed
        try:
            time_stamp_list, attribute_list = zip(*sorted(zip(time_stamp_list, attribute_list)))
        except Exception:
            pass

        plt.figure()
        plt.plot(time_stamp_list, attribute_list, marker="o")
        plt.title(f"{attribute.capitalize()} over time (Plant {plant_id})")
        plt.xlabel("Timestamp")
        plt.ylabel(attribute.capitalize())
        plt.tight_layout()
        plt.savefig("plot.png", dpi=150, bbox_inches="tight")
        print("Saved plot to plot.png")




