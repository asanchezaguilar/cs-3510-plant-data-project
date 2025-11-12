class Plant:
    def __init__(self, timestamp="none", plant_id="none", soil_moisture=0, ambient_temperature=0, soil_temperature=0, humidity=0, light_intensity=0, soil_ph=0, nitrogen_level=0, phosphorus_level=0, potassium_level=0, chlorophyll_content=0, electrochemical_signal=0, plant_health_status="none", unique_id = 0):
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
        self._potassium_level = potassium_level
        self._chlorophyll_content = chlorophyll_content
        self._electrochemical_signal = electrochemical_signal
        self._plant_health_status = plant_health_status
        self._unique_id = unique_id

    # getters
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if timestamp:
            self._timestamp = timestamp

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, plant_id):
        if plant_id:
            self._plant_id = plant_id

    @property
    def soil_moisture(self):
        return self._soil_moisture

    @soil_moisture.setter
    def soil_moisture(self, soil_moisture):
        if soil_moisture:
            self._soil_moisture = soil_moisture

    @property
    def ambient_temperature(self):
         return self._ambient_temperature

    @ambient_temperature.setter
    def ambient_temperature(self, ambient_temperature):
        if ambient_temperature:
            self._ambient_temperature = ambient_temperature

    @property
    def soil_temperature(self):
        return self._soil_temperature
    
    @soil_temperature.setter
    def soil_temperature(self, soil_temperature):
        if soil_temperature:
            self._soil_temperature = soil_temperature

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        if humidity:
            self._humidity = humidity

    @property
    def light_intensity(self):
        return self._light_intensity

    @light_intensity.setter
    def light_intensity(self):
        if light_intensity:
            self._light_intensity = light_intensity
  
    @property
    def soil_ph(self):
        return self._soil_ph

    @soil_ph.setter
    def soil_ph(self, soil_ph):
        if soil_ph:
            self._soil_ph = soil_ph

    @property
    def nitrogen_level(self):
        return self._nitrogen_level

    @nitrogen_level.setter
    def nitrogen_level(self, nitrogen_level):
        if nitrogen_level:
            self._nitrogen_level = nitrogen_level

    @property
    def phosphorus_level(self):
        return self._phosphorus_level

    @phosphorus_level.setter
    def phosphorus_level(self, phosphorus_level):
        if phosphorus_level:
            self._phosphorus_level = phosphorus_level

    @property
    def potassium_level(self):
        return self._potassium_level

    @potassium_level.setter
    def potassium_level(self, potassium_level):
        if potassium_level:
            self._potassium_level = potassium_level
        
    @property
    def chlorophyll_content(self):
        return self._chlorophyll_content
    
    @chlorophyll_content.setter
    def chlorophyll_content(self, chlorophyll_content):
        if chlorophyll_content:
            self._chlorophyll_content = chlorophyll_content
    
    @property
    def electrochemical_signal(self):
        return self._electrochemical_signal

    @electrochemical_signal.setter
    def electrochemical_signal(self, electrochemical_signal):
        if electrochemical_signal:
            self._electrochemical_signal = electrochemical_signal
    
    @property
    def plant_health_status(self):
        return self._plant_health_status

    @plant_health_status.setter
    def plant_health_status(self, plant_health_status):
        if plant_health_status:
            self._plant_health_status = plant_health_status

    def __str__(self):
        return f"Plant info: Timestamp: {self.timestamp}, Plant ID: {self.plant_id}, Soil Moisture: {self.soil_moisture}%, Ambient Temperature: {self.ambient_temperature}°C, Soil Temperature: {self.soil_temperature}°C, Humidity: {self.humidity}% Light Intensity: {self.light_intensity}, Soil pH: {self.soil_ph}, Nitrogen Level: {self.nitrogen_level}%, Phosphorus Level: {self.phosphorus_level}%, Potassium Level: {self.potassium_level}%, Chlorophyll Content: {self.chlorophyll_content}, Electrochemical Signal: {self.electrochemical_signal}, Plant Health Status: {self.plant_health_status}"
