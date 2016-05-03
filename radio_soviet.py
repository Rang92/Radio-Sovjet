from maps import USA


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

    breadthc = []
    depthc = []

    stypes = [20, 22, 28, 32, 37, 39, 41]

    for start in range(0, len(USA().as_list())):
        country = USA()

        oblasts = country.as_list()

        trav_cell_breadth(oblasts[start])

        for oblast in oblasts:
            if oblast.senderType == 0: 
                if len(oblast.neighbours) == 0:
                    oblast.senderType = 1
                else:
                    trav_cell_breadth(oblast)

        for o in oblasts:
            if o.senderType == 0: print  "ERROR"

        # Weergeef de som van de zendertypes om een indicatie geven te van hoe laag de zendertypes zijn gebleven.
        weightc = sum([stypes[e.senderType-1] for e in country.as_list()])
        weight = sum([e.senderType for e in country.as_list()])
        # print 'Start:', oblasts[start].name, weight
        breadthc.append(weightc)
        breadth.append(weight)

    for start in range(0, len(USA().as_list())):
        country = USA()

        oblasts = country.as_list()

        trav_cell_depth(oblasts[start])

        for oblast in oblasts:
            if oblast.senderType == 0: 
                if len(oblast.neighbours) == 0:
                    oblast.senderType = 1
                else:
                    trav_cell_depth(oblast)

        for o in oblasts:
            if o.senderType == 0: print  "ERROR"

        # Weergeef de som van de zendertypes om een indicatie te geven van hoe laag de zendertypes zijn gebleven.
        weightc = sum([stypes[e.senderType-1] for e in country.as_list()])
        weight = sum([e.senderType for e in country.as_list()])
        # print 'Start:', oblasts[start].name, weight
        # print 'Start:', oblasts[start].name, weightc
        depthc.append(weightc)
        depth.append(weight)

    print 'DFS: {}, BFS: {}'.format(min(depth), min(breadth))
    print 'DFS: {}, BFS: {}'.format(min(depthc), min(breadthc))
