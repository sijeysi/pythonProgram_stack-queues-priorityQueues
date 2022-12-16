# Shortest Path Using Breadth-First Traversal
import networkx as nx
from graph import City, load_graph

print("\n8th testing: Using networkx to reveal all the shortest paths between two cities")
nodes, graph = load_graph("roadmap.dot", City.from_dict)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))


def by_latitude(city):
    return -city.latitude

print(" → ".join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude))
    )
    