
all_forecasts = {
    "9.02N,7.31E" : [
        { "day" : 1,
        "temperature": 23,
        "wind_speed": 1.37 },
        { "day" : 2,
        "temperature": 20,
        "wind_speed": 0.25 },
        { "day" : 3,
        "temperature": 21,
        "wind_speed": 0.83 }
    ], 
    "1.3S,36.85E":
    [
        { "day" : 1,
        "temperature": 20,
        "wind_speed": 0.73 },
        { "day" : 2,
        "temperature": 18,
        "wind_speed": 0.96 },
        { "day" : 3,
        "temperature": 19,
        "wind_speed": 1.29 }
    ],
    "5.63N,0.39W":
    [
        { "day" : 1,
        "temperature": 15,
        "wind_speed": 1.31 },
        { "day" : 2,
        "temperature": 13,
        "wind_speed": 0.24 },
        { "day" : 3,
        "temperature": 16,
        "wind_speed": 0.83 }
    ]
}

map_city_to_coords = {
    'Abuja': '9.02N,7.31E',
    'Nairobi': '1.3S,36.85E'
}

def show_weather():
    city_name = input('Please enter a city name:')
    if city_name not in map_city_to_coords:
        print('We do not have coordinates for that city.')
    else:
        coords = map_city_to_coords[city_name]
        print(all_forecasts[coords])


show_weather()

# This is the initial program. The walkthrough shows how to modify this code.
# At the end of the walkthrough, this code will read and write to a json file.
#
# You can see the completed code after the walkthrough by going here,
# https://github.com/kibo-programming-2-jan-23/walkthroughs/tree/main/show-weather-from-file/end

