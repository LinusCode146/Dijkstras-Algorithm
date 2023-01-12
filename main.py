from pprint import pprint
from create_graph import create_graph




def dijkstra(start: str,
             struct: dict[str: dict[str: int or float]],
             max_value = int
             ) -> dict[str: dict[str: int or float]]:


    table = {key : {'dist': max_value, 'prev': None} for key in struct.keys()}
    table[start]['dist'] = 0
    visited = []
    unvisited = list(struct.keys())
    current_node = start

    for _ in range(len(list(struct.keys())) - 1):
        #* fill table and find shortest path for each individuell connnection point
        key = current_node
        item = struct[key]
        for dest, dist in item.items():
            if dest in unvisited and dist + table[key]['dist'] < table[dest]['dist']:

                table[dest]['dist'] = dist + table[key]['dist']
                table[dest]['prev'] = key  
        unvisited.remove(key)
        visited.append(key)

        #*Get next node
        nodes = {key: table[key]['dist'] for key in unvisited}
        min_value = min(list(nodes.values()))
        minimum_key = [key for key in nodes if nodes[key]==min_value][0]
        current_node = minimum_key

    return table


def get_distance(start, destination, graph, max_value=10000, path_construction = False):
    dic = dijkstra(start, graph, max_value)
    if not path_construction:
        return dic[destination]['dist']

    current = destination
    path = [destination]
    while current != start:
        current = dic[current]['prev']
        path.insert(0, current)
    return {
        'distance': dic[destination]['dist'],
        'path': path,
    }


if __name__ == '__main__':

    #TODO: create a graph with create_graph() method here and name it "struct"
    struct = create_graph(['a', 'b', 'c', 5, 6], ['b', 'a', 'c','d', 5, 2, 5], ['c', 'a', 'b','d', 6, 2, 5], ['d', 'b', 'c', 5, 5])
    
    start = 'a' #TODO: decide your start point here
    destination = 'd'#TODO: and your endpoint here
    path_construction = True
    information = get_distance(start, destination, struct, path_construction = path_construction) #! If you dont want to have the reconstructed path, said the 'way' parameter to false
    match information:
        case int():
            information = information - 1 + 1
            pprint(information)
        case dict():
                distance = information['distance']
                path = information['path']
                pprint(distance)
                pprint(' - '.join(path))
        case _:
            print("Something has caused an error")



    
    

