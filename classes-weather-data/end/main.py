import json

class WeatherData:
    def __init__(self, hours, temperature, wind_direction, wind_speed):
        self.hours = hours
        self.temperature = temperature
        self.wind_direction = wind_direction
        self.wind_speed = wind_speed

    def display(self, location):
        print(f'In {location} at {self.hours} hours,')
        print(f'\t temperature will be {self.temperature}')
        self.display_wind()
  
    def display_wind(self):
        print(f'\t wind speed will be {self.wind_speed}')
        print(f'\t wind coming from the {self.wind_direction}')
   

def data_from_dictionary(all_data):
    objects = []
    for data in all_data['dataseries']:
        hours = data['timepoint']
        temperature = data['temp2m']
        wind_dir = data['wind10m']['direction']
        wind_speed = data['wind10m']['speed']

        new_object = WeatherData(hours, temperature, wind_dir, wind_speed)
        objects.append(new_object)
    return objects

def main():
    with open('api_output.json', 'r') as f:
        all_data = json.load(f)

    location = 'Nairobi'
    all_weather_data = data_from_dictionary(all_data)
    for weather_data in all_weather_data:
        weather_data.display(location)

main()

