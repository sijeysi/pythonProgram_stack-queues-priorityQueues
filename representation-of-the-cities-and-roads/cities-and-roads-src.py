
import networkx as nx
from graph import City, load_graph

print(nx.nx_agraph.read_dot("roadmap.dot"))


graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["london"])


nodes, graph = load_graph("roadmap.dot", City.from_dicts(attrs))
print(nodes["london"])


for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)


for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)


def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))


def by_distance(weights):
    return float(weights["distance"])


for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")