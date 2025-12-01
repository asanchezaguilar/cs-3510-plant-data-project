import pandas as pd
from matplotlib import pyplot as plt

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
    if (stress2[i]=='Healthy'):
        stress2[i] = 0
    elif (stress2[i]=='Moderate Stress'):
        stress2[i] = 1
    elif (stress2[i]=='High Stress'):
        stress2[i] = 2
        
plt.scatter(atemp,stress2)
plt.xlabel('Ambient Temperature (°C)')
plt.ylabel('Plant Health')
plt.show()

plt.scatter(nitrogen,stress2)
plt.xlabel('Nitrogen Level (mg/kg)')
plt.ylabel('Plant Health')
plt.show()

plt.scatter(light,stress2)
plt.xlabel('Light Intensity (Lux)')
plt.ylabel('Plant Health')
plt.show()

plt.scatter(moisture,stress2)
plt.xlabel('Soil Moisture (%)')
plt.ylabel('Plant Health')
plt.show()