travel_log = [
    {
      "country": "France",
      "visits": 12,
      "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    {
      "country": "Germany",
      "total_visits": 5,
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
]



def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)


add_new_country("Italy", "2", ["Venice", "Rome"])

print(travel_log)