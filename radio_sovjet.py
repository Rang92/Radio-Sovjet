from maps import Ukraine


def lowest_sendertype(cell):
    # Haal alle gebruikte zendertypes uit een lijst met de beschikbare zendertypes
    # Dus als zenders 1 en 2 zijn gebruikt, dan wordt (1, 2, 3, 4, 5) -> (3, 4, 5)
    # Om dit te doen moet van elke oblast het zendertype worden bepaald (lambda n: n.senderType)
    return set(range(1, 8)) - set(map(lambda n: n.senderType, cell.neighbours))


if __name__ == '__main__':
    country = Ukraine()

    for elem in country.as_list():
        # Stel bij elk Oblast het laagst mogelijke zendertype in
        elem.senderType = lowest_sendertype(elem).pop()

    for elem in country.as_list():
        # Weergeef de naam van de Oblast en het zendertype
        print elem.name, elem.senderType

    # Weergeef de som van de zendertypes om een indicatie te geven van hoe laag de zendertypes zijn gebleven.
    print reduce(lambda x, y: x + y, [e.senderType for e in country.as_list()])