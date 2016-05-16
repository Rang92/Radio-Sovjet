from data_structures import Tree
from maps import USA, Ukraine, China

def lowest_sendertype(cell):
    # Haal alle gebruikte zendertypes uit een lijst met de beschikbare zendertypes
    # Dus als zenders 1 en 2 zijn gebruikt, dan wordt (1, 2, 3, 4, 5) -> (3, 4, 5)
    # Om dit te doen moet van elke oblast het zendertype worden bepaald (lambda n: n.senderType)
    return set(range(1, 5)) - set(map(lambda n: n.senderType, cell.neighbours))


def to_tree(node, tree):
    tree.append(node)
    node.inTree = True

    neighs = [c for c in node.neighbours if not c.inTree]

    while len(neighs) > 0:
        to_tree(neighs.pop(), tree)
        neighs = [c for c in node.neighbours if not c.inTree]


def tree_sum(leaf):
    if leaf.next.this is not None:
        return leaf.this.senderType + tree_sum(leaf.next)
    else:
        return 0


def print_tree(leaf, nestinglevel = 1):
    global nesting

    print '-' * nesting, leaf.this.name, leaf.this.senderType
    nesting += 1

    if leaf.next.this is not None:
        print_tree(leaf.next, nestinglevel + 1)


def trav_cell_depth(tree):
    cell = tree.this

    pos = lowest_sendertype(cell) - cell.prev

    if len(pos) == 0:
        if tree.parent is None:
            raise Exception('Wut')

        tree.parent.this.prev.add(tree.parent.this.senderType)
        trav_cell_depth(tree.parent)

    cell.senderType = pos.pop()

    if tree.next.this is not None:
        trav_cell_depth(tree.next)


def tree_dist(leaf, dist):
    dist[leaf.this.senderType] += 1

    if leaf.next.this is not None:
        tree_dist(leaf.next, dist)

    return dist


if __name__ == '__main__':
    # stypes = [20, 22, 28, 32, 37, 39, 41]

    res = []
    sums = []

    for c in [USA, Ukraine, China]:
        for i in range(len(c().as_list())):
            oblast = c().as_list()[i]

            tree = Tree()
            ttree = tree
            l = []
            to_tree(oblast, l)

            for x in l:
                ttree.this = x
                ttree.next = Tree()
                ttree.next.parent = ttree

                ttree = ttree.next

            try:
                trav_cell_depth(tree)
            except:
                continue

            res.append(tree)
            ttree = tree

            print tree_dist(ttree, {1: 0, 2: 0, 3: 0, 4: 0})

            nesting = 1
        print '-----------'
