def create_graph(*nodes):
    struct = dict()
    for node in nodes:
        start = node.pop(0)
        connnections = list(filter(lambda x: str(x) == x, node))
        distances = list(filter(lambda x: str(x) != x, node))
        con_dict = dict()
        for con, dist in zip(connnections, distances):
            con_dict[con] = dist
        struct[start] = con_dict
    return struct

