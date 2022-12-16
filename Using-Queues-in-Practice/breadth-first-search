import networkx as nx
from graph import City, load_graph
from graph import (
    City,
    load_graph,
    breadth_first_traverse,
    breadth_first_search as bfs,
)

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")


def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))

for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")


def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
print(city.name)

for city in breadth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)
