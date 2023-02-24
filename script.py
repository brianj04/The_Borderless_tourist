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
print(test_destination_index)

