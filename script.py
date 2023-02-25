destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_desination_index(Destination):
    destinations_Index = destinations.index(Destination)
    return destinations_Index


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_desination_index(traveler_destination)
    return traveler_destination_index
test_destination_index = get_traveler_location(test_traveler)

attractions = [[] for destinatio in destinations]
def add_attraction(destination, attraction):
    destination_index = get_desination_index(destination)
    attractions_for_destinations = attractions[destination_index]
    attractions[destination_index].append(attraction)
    return attractions_for_destinations
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)

def find_attractions(destination, interests):
    destination_index = get_desination_index(destination)
    attractions_in_city = destination_index[1]
    attractions_with_interest = []
    possible_attraction = [[] for x in attractions_in_city]
    for item in possible_attraction:
        attraction_tags = item[1]
        for attraction in attraction_tags:
            for interest in interests:
                if interest in attraction_tags:
                    