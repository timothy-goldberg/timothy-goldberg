import itertools


def base_quads(tipe):
    """"
    This returns a list of the quads in 2-dim of the requested type (=tipe).
    Lowercase letters restrict to half the possible values, for building
    odd-dimensional Quads games.
    """
    if tipe == 'A':
        return [[0, 0, 0, 0],
                [1, 1, 1, 1],
                [2, 2, 2, 2],
                [3, 3, 3, 3]]
    elif tipe == 'H':
        return [[0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1],
                [0, 0, 2, 2], [0, 2, 0, 2], [0, 2, 2, 0], [2, 2, 0, 0], [2, 0, 2, 0], [2, 0, 0, 2],
                [0, 0, 3, 3], [0, 3, 0, 3], [0, 3, 3, 0], [3, 3, 0, 0], [3, 0, 3, 0], [3, 0, 0, 3],
                [1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 2, 1, 1], [2, 1, 2, 1], [2, 1, 1, 2],
                [1, 1, 3, 3], [1, 3, 1, 3], [1, 3, 3, 1], [3, 3, 1, 1], [3, 1, 3, 1], [3, 1, 1, 3],
                [2, 2, 3, 3], [2, 3, 2, 3], [2, 3, 3, 2], [3, 3, 2, 2], [3, 2, 3, 2], [3, 2, 2, 3]]
    elif tipe == 'D':
        return [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1],
                [2, 0, 1, 3], [2, 0, 3, 1], [2, 1, 0, 3], [2, 1, 3, 0], [2, 3, 0, 1], [2, 3, 1, 0],
                [3, 0, 1, 2], [3, 0, 2, 1], [3, 1, 0, 2], [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1, 0]]
    elif tipe == 'a':
        return [[0, 0, 0, 0],
                [1, 1, 1, 1]]
    elif tipe == 'h':
        return [[0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]
    return True


def has_duplicates(l):
    """
    This checks if the list has duplicates.
    I think "and not seen.append(x)" is a trick to update the list "seen".
    I stole the code from somewhere so I'm not sure.
    """
    seen = []
    unique_list = [x for x in l if x not in seen and not seen.append(x)]
    return len(l) != len(unique_list)


def quad_count_dim4(tipe):
    """
    This constructs and returns the count for the number of quads of each type
    in 4-dimensional Quads, Quad-16.
    """
    quad_list = []
    for A in base_quads(tipe[0]):
        for B in base_quads(tipe[1]):
            prequad = [A, B]
            quad = [[slot[i] for slot in prequad] for i in range(len(prequad[0]))]
            quad.sort()
            if not (has_duplicates(quad)) and not (quad in quad_list):
                quad_list.append(quad)
    return len(quad_list)


def quad_count_gen(tipe):
    """
    This constructs all quads of the given type, with lowercase letters representing
    half-attributes, and returns the count.
    """
    quad_list = []
    universe = [base_quads(letter) for letter in tipe]
    for x in itertools.product(*universe):
        prequad = list(x)
        quad = [[slot[i] for slot in prequad] for i in range(len(prequad[0]))]
        quad.sort()
        if not (has_duplicates(quad)) and not (quad in quad_list):
            quad_list.append(quad)
    return len(quad_list)


# quad_count_gen('DDD')


def main():
    counts = {}
    for x in 'ADH':
        for y in 'ADH':
            tipe = x + y
            counts[tipe] = quad_count_gen(tipe)
    return counts


thing = main()

for x in thing:
    print(x, thing[x])


