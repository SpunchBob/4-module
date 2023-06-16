from requests import get

api_url = "https://swapi.dev/api"

def starships_func():
    response = get(api_url)
    data = response.json()['starships']

    response = get(data)
    starships = response.json()['results']
    starships_speeds = []
    starships_names = []

    for starships_data in starships:
        if starships_data['max_atmosphering_speed'] == "n/a":
            continue
        elif starships_data['max_atmosphering_speed'] == "1000km":
            continue
        else:
            starships_speeds.append(int(starships_data['max_atmosphering_speed']))
        starships_names.append(starships_data['name'])
    
    return (f"Корабль с максимальной скоростью: {starships_names[5]}, его скорость - {max(starships_speeds)} км.")

def planets_func(): 
    response = get(api_url)
    data = response.json()['planets']

    response = get(data)
    planets = response.json()['results']
    planets_diameter = []
    planets_name = []

    for planets_data in planets:
        planets_diameter.append(int(planets_data["diameter"]))
        planets_name.append(planets_data["name"])   

    return (f"Планета с самым большим диаметром: {planets_name[5]}, её диаметр - {max(planets_diameter)} км.")


