class Plant:
    def __init__(self, timestamp="none", plant_id="none", soil_moisture=0, ambient_temperature=0, soil_temperature=0, humidity=0, light_intensity=0, soil_ph=0, nitrogen_level=0, phosphorus_level=0):
        self._timestamp = timestamp
        self._plant_id = plant_id
        self._soil_moisture = soil_moisture
        self._ambient_temperature = ambient_temperature
        self._soil_temperature = soil_temperature
        self._humidity = humidity
        self._light_intensity = light_intensity
        self._soil_ph = soil_ph
        self._nitrogen_level = nitrogen_level
        self._phosphorus_level = phosphorus_level

    # getters
    @property
    def timestamp(self):
        return self._timestamp

    @property
    def plant_id(self):
        return self._plant_id

    @property
    def soil_moisture(self):
        return self._soil_moisture

    @property
    def ambient_temperature(self):
         return self._ambient_temperature

    @property
    def soil_temperature(self):
        return self._soil_temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def light_intensity(self):
        return self._light_intensity
  
    @property
    def soil_ph(self):
        return self._soil_ph

    @property
    def nitrogen_level(self):
        return self._nitrogen_level

    @property
    def phosphorus_level(self):
        return self._phosphorus_level

    def __str__(self):
        return f"Plant info: Timestamp: {self.timestamp}, Plant ID: {self.plant_id}, Soil Moisture: {self.soil_moisture}%, Ambient Temperature: {self.ambient_temperature}°C, Soil Temperature: {self.soil_temperature}°C, Humidity: {self.humidity}% Light Intensity: {self.light_intensity}, Soil pH: {self.soil_ph}, Nitrogen Level: {self.nitrogen_level}%, Phosphorus Level: {self.phosphorus_level}%"
