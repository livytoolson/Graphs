from graph import Graph         # this import won't work because graph is in a different folder

def earliest_ancestor(ancestors, starting_node):
    lineage = Graph()

    for parents in ancestors:

        if parents[0] not in lineage:
            lineage.add_vertex(parents[0])

        if len(parents) > 1:

            if parents[1] not in lineage:
                lineage.add_vertex(parents[1])

    paths = lineage.dft_recursive(starting_node)                                   # find all the paths that leads to our node - starting node is the first node in each path, possible ancestor is the last node in that path
    max_length_path = max([len(path) for path in paths]) if len(paths) > 0 else 0  # length of the longest path in paths - inside square brackets is a list of all the lengths, max length path will only be returned if the length of paths is greater than 0

    possible = []                              # keeps track of possible ancestors

    for path in paths:

        if len(path) == max_length_path:
            possible.append(path)

    if len(possible) == 1:
        return possible[0][-1]                  # possible[0] returns the first path in possible, possible[-1] - returns last vert which is the ancestor

    elif len(possible) > 1:                     # if length of possible paths is greater than 1
        current_ancestor = possible[0][-1]      # possible[0] = first possible path, possible[0][-1] = ancestor at first path ([-1] because possible ancestor is the last vert)

        for path in possible:                   # possible is list of a list of oaths

            if path[-1] < current_ancestor:     # if the ancestor < our current ancestor
                current_ancestor = path[-1]     # reassign current ancestor to new possible ancestor in new path - we want to return ancestor with smallest numeric value

        return current_ancestor

    return -1                                   # input individual has no parents
