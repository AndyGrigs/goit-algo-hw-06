import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф з першого завдання
G = nx.Graph()

# Додаємо вузли з їх позиціями
G.add_nodes_from([
    ("A", {"pos": (0, 0)}),
    ("B", {"pos": (1, 2)}),
    ("C", {"pos": (2, 0)}),
    ("D", {"pos": (3, 2)}),
    ("E", {"pos": (4, 0)}),
])

# Додаємо ребра з вагами
G.add_weighted_edges_from([
    ("A", "B", 5),
    ("B", "C", 3),
    ("C", "D", 4),
    ("D", "E", 2),
    ("A", "C", 6),
    ("B", "D", 1),
    ("C", "E", 7),
])

# Використовуємо алгоритм Дейкстри для знаходження найкоротших шляхів між усіма парами вершин
# Отримуємо словник найкоротших шляхів та їх довжин
all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))
all_shortest_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

# Виводимо найкоротші шляхи та їх довжини
for source in G.nodes():
    for target in G.nodes():
        if source != target:
            path = all_shortest_paths[source][target]
            length = all_shortest_lengths[source][target]
            print(f"Найкоротший шлях від {source} до {target}: {path}, довжина: {length}")

# Візуалізація графу та найкоротших шляхів від вузла 'A' до інших
pos = nx.get_node_attributes(G, 'pos')

plt.figure(figsize=(10, 7))

# Малюємо граф
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')

# Додаємо мітки ваг ребер
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Виділяємо найкоротші шляхи від 'A' до інших вузлів
colors = ['red', 'green', 'blue', 'purple']
targets = ['B', 'C', 'D', 'E']

for idx, target in enumerate(targets):
    path = all_shortest_paths['A'][target]
    edge_list = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color=colors[idx], width=2, label=f'Шлях до {target}')

plt.legend()
plt.title("Найкоротші шляхи від 'A' до інших вузлів за алгоритмом Дейкстри")
plt.show()
