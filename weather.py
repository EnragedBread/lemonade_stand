import random

def make_weather(day):
    weather_chance = random.random()

    if weather_chance < 0.6:
        weather = 'Sunny'
        weather_factor = 1.0
    elif weather_chance < 0.8:
        weather = 'Cloudy'
        rain_chance = random.randint(30, 70)
        weather += f', With a {rain_chance}% chance of rain'
        weather_factor = 1 - (rain_chance / 100)
    elif day >= 3:
        weather = 'Hot and Dry'
        weather_factor = 2.0
    else:
        weather = 'Sunny'
        weather_factor = 1.0
   
    return (weather, weather_factor)

def random_events(weather, glasses_sold, glasses):
    # TODO add day limit
    random_event = "" 
    if weather.startswith('Cloudy'):
        storm_chance = random.random()
        if storm_chance < 0.25:
            random_event = "A Thunderstorm wiped out your lemonade stand! No sales for today."
            glasses_sold = 0

    if weather == 'Sunny':
        street_closed = random.random()
        if street_closed < 0.25:
            random_event = "Street crews are working on your street today, no traffic!"
            crews_thirsty = random.random()
            if crews_thirsty < 0.50:
                random_event += "\n Thirsty workers bought all of your lemonade!"
                glasses_sold = glasses

            else:
                random_event += "\n only a few people bought your lemonade today!"
                glasses_sold = round(glasses_sold / 10)
    
    return (random_event, glasses_sold)