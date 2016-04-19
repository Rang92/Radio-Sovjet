from maps import Ukraine


def lowest_sendertype(cell):
    # Haal alle gebruikte zendertypes uit een lijst met de beschikbare zendertypes
    # Dus als zenders 1 en 2 zijn gebruikt, dan wordt (1, 2, 3, 4, 5) -> (3, 4, 5)
    # Om dit te doen moet van elke oblast het zendertype worden bepaald (lambda n: n.senderType)
    return set(range(1, 8)) - set(map(lambda n: n.senderType, cell.neighbours))


def trav_cell_breadth(cell):
    nodes = [c for c in cell.neighbours if c.senderType == 0]

    for c in nodes:
        c.senderType = lowest_sendertype(c).pop()

    for c in nodes:
        trav_cell_breadth(c)


def trav_cell_depth(cell):
    cell.senderType = lowest_sendertype(cell).pop()

    neighs = [c for c in cell.neighbours if c.senderType == 0]

    while len(neighs) > 0:
        trav_cell_depth(neighs.pop())


if __name__ == '__main__':
    breadth = []
    depth = []

    for start in range(0, len(Ukraine().as_list())):
        country = Ukraine()

        oblasts = country.as_list()

        trav_cell_breadth(oblasts[start])

        # Weergeef de som van de zendertypes om een indicatie te geven van hoe laag de zendertypes zijn gebleven.
        weight = reduce(lambda x, y: x + y, [e.senderType for e in country.as_list()])
        # print 'Start:', oblasts[start].name, weight
        breadth.append(weight)

    for start in range(0, len(Ukraine().as_list())):
        country = Ukraine()

        oblasts = country.as_list()

        trav_cell_depth(oblasts[start])

        # Weergeef de som van de zendertypes om een indicatie te geven van hoe laag de zendertypes zijn gebleven.
        weight = reduce(lambda x, y: x + y, [e.senderType for e in country.as_list()])
        # print 'Start:', oblasts[start].name, weight
        depth.append(weight)

    print 'DFS: {}, BFS: {}'.format(min(depth), min(breadth))
