from maps import USA
from maps import Ukraine
from maps import China

# maak een lijst om bij te houden welk zendertype hoevaak gebruikt is
hist = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

def lowest_sendertype(cell):
    # Haal alle gebruikte zendertypes uit een lijst met de beschikbare zendertypes
    # Dus als zenders 1 en 2 zijn gebruikt, dan wordt (1, 2, 3, 4, 5) -> (3, 4, 5)
    # Om dit te doen moet van elke oblast het zendertype worden bepaald (lambda n: n.senderType)

    available_senderTypes = list(set(range(1, 7)) - set(map(lambda n: n.senderType, cell.neighbours)))

    # sorteer de beschikbare zendertypes op gebruiktheid (minst gebruikt - meest gebruikt
    sortedlist= sorted(available_senderTypes, key=lambda x: hist[x]) 

    # error checking
    print hist
    print sortedlist

    # return gesorteerde lijst
    return sortedlist

def trav_cell_depth(cell):
    cell.senderType = lowest_sendertype(cell)[0]

    hist[cell.senderType]+=1

    neighs = [c for c in cell.neighbours if c.senderType == 0]

    while len(neighs) > 0:
        trav_cell_depth(neighs.pop())
        neighs = [c for c in cell.neighbours if c.senderType == 0]

if __name__ == '__main__':
    breadth = []
    depth = []

    breadthc = []
    depthc = []

    stypes = [20, 22, 28, 32, 37, 39, 41]

    # Depth First Search (= efficienter dan Breadth First Search)
    country = USA()
    oblasts = country.as_list()
    trav_cell_depth(country.Minnesota)

    # Weergeef de som van de zendertypes om een indicatie te geven van hoe laag de zendertypes zijn gebleven.
    weightc = sum([stypes[e.senderType-1] for e in country.as_list()])
    weight = sum([e.senderType for e in country.as_list()])
    # print 'Start:', oblasts[start].name, weight
    # print 'Start:', oblasts[start].name, weightc

    depthc.append(weightc)
    depth.append(weight)

    # print resultaat
    print hist

    print 'DFS: {}'.format(min(depth))
    print 'DFS costs: {}'.format(min(depthc))
