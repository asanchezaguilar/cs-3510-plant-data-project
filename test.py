import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

phd = pd.read_csv("plant_health_data.csv")

stress = phd['Electrochemical_Signal'].tolist()
moisture = phd['Soil_Moisture'].tolist()
light = phd['Light_Intensity'].tolist()
humidity = phd['Humidity'].tolist()
nitrogen = phd['Nitrogen_Level'].tolist()
atemp = phd['Ambient_Temperature'].tolist()
stemp = phd['Soil_Temperature'].tolist()
stress2 = phd['Plant_Health_Status'].tolist()

for i in range(len(stress2)):
    if stress2[i] == 'Healthy':
        stress2[i] = 0
    elif stress2[i] == 'Moderate Stress':
        stress2[i] = 1
    elif stress2[i] == 'High Stress':
        stress2[i] = 2

def add_best_fit_line(x, y):
    m, b = np.polyfit(x, y, 1)
    x_line = [min(x), max(x)]
    y_line = [m * x_line[0] + b, m * x_line[1] + b]
    plt.plot(x_line, y_line, color="red")

def make_and_save_plot(x, y, xlabel, ylabel, title, filename):
    plt.figure()
    plt.scatter(x, y)
    add_best_fit_line(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"Saved: {filename}")

# Create all plots
make_and_save_plot(atemp, stress2,
                   "Ambient Temperature (°C)", "Plant Stress",
                   "Plant Stress vs Ambient Temperature",
                   "ambient_temp_stress.png")

make_and_save_plot(nitrogen, stress2,
                   "Nitrogen Level (mg/kg)", "Plant Stress",
                   "Plant Stress vs Nitrogen Level",
                   "nitrogen_stress.png")

make_and_save_plot(light, stress2,
                   "Light Intensity (Lux)", "Plant Stress",
                   "Plant Stress vs Light Intensity",
                   "light_stress.png")

make_and_save_plot(moisture, stress2,
                   "Soil Moisture (%)", "Plant Stress",
                   "Plant Stress vs Soil Moisture",
                   "moisture_stress.png")
