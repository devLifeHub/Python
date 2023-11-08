import requests
import json

ship_url = "https://swapi.dev/api/starships/10/"

response = requests.get(ship_url)

if response.status_code == 200:
    ship_data = response.json()

    pilots_info = []
    for pilot_url in ship_data["pilots"]:
        pilot_response = requests.get(pilot_url)
        if pilot_response.status_code == 200:
            pilot_data = pilot_response.json()
            homeworld_response = requests.get(pilot_data['homeworld'])
            homeworld_data = homeworld_response.json()
            pilot_info = {
                "name": pilot_data["name"],
                "height": pilot_data["height"],
                "mass": pilot_data["mass"],
                "homeworld": homeworld_data["name"],
                "homeworld_url": pilot_data["homeworld"]
            }
            pilots_info.append(pilot_info)

    result = {
        "name": ship_data["name"],
        "max_atmosphering_speed": ship_data["max_atmosphering_speed"],
        "starship_class": ship_data["starship_class"],
        "pilots": pilots_info
    }

    print(json.dumps(result, indent=4))

    with open('millennium_falcon.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4)
else:
    print("Не удалось получить информацию о корабле Millennium Falcon.")
