from plant import Plant
import csv
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt
import statistics


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

    def summarize_attribute(self, attribute):
        values = []

        for plant in self._plant_list:
            values.append(getattr(plant, attribute))

        count = len(values)
        mean = statistics.mean(values)
        median = statistics.median(values)
        stdev = statistics.pstdev(values)   # population standard deviation
        minimum = min(values)
        maximum = max(values)

        return count, mean, median, stdev, minimum, maximum

    def average_by_health_status(self, attribute):
        groups = {}

        for plant in self._plant_list:
            status = plant.plant_health_status
            value = getattr(plant, attribute)

            if status not in groups:
                groups[status] = []
            groups[status].append(value)

        results = {}
        for status in groups:
            values = groups[status]
            avg = sum(values) / len(values)
            results[status] = avg

        return results



    
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

    def correlation_graph(self, attr1, attr2):
        x_values = []
        y_values = []

        for plant in self._plant_list:
            x_values.append(getattr(plant, attr1))
            y_values.append(getattr(plant, attr2))

        mean_x = statistics.mean(x_values)
        mean_y = statistics.mean(y_values)

        num = 0
        denom_x = 0
        denom_y = 0

        for i in range(len(x_values)):
            dx = x_values[i] - mean_x
            dy = y_values[i] - mean_y
            num += dx * dy
            denom_x += dx * dx
            denom_y += dy * dy

        r = num / ((denom_x * denom_y) ** 0.5)

        plt.figure()
        plt.scatter(x_values, y_values, marker="o")

        x_label = attr1.replace("_", " ").title()
        y_label = attr2.replace("_", " ").title()

        plt.title(f"{y_label} vs {x_label} (r = {r:.3f})")
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.tight_layout()
        plt.savefig("plot.png", dpi=150, bbox_inches="tight")

        print("Saved correlation plot to plot.png")
        print(f"Correlation between {x_label} and {y_label}: {r}")





