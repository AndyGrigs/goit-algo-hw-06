import networkx as nx
import matplotlib.pyplot as plt

# Створюємо порожній граф
G = nx.Graph()

# Додаємо вузли (наприклад, станції або зупинки)
G.add_nodes_from([
    ("A", {"pos": (1, 0)}),
    ("B", {"pos": (1, 1)}),
    ("C", {"pos": (3, 1)}),
    ("D", {"pos": (3, 4)}),
    ("E", {"pos": (4, 2)}),
])

# Додаємо ребра (дороги або маршрути між вузлами)
# G.add_edges_from([
#     ("A", "B", {"weight": 5}),
#     ("B", "C", {"weight": 3}),
#     ("C", "D", {"weight": 4}),
#     ("D", "E", {"weight": 2}),
#     ("A", "C", {"weight": 6}),
#     ("B", "D", {"weight": 1}),
#     ("C", "E", {"weight": 7}),
# ])
G.add_edges_from([
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("A", "C"),
    ("B", "D"),
    ("C", "E"),
])



# Отримуємо позиції вузлів для візуалізації
pos = nx.get_node_attributes(G, 'pos')

# Малюємо граф
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')

# Додаємо мітки ваг ребер
# edge_labels = nx.get_edge_attributes(G)
# nx.draw_networkx_edge_labels(G, pos)

plt.title("Транспортна мережа міста")
plt.show()
