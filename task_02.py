import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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
G.add_edges_from([
    ("A", "B", {"weight": 5}),
    ("B", "C", {"weight": 3}),
    ("C", "D", {"weight": 4}),
    ("D", "E", {"weight": 2}),
    ("A", "C", {"weight": 6}),
    ("B", "D", {"weight": 1}),
    ("C", "E", {"weight": 7}),
])

# Функція для пошуку в глибину (DFS)
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if result is not None:
                return result
    return None

# Функція для пошуку в ширину (BFS)
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        elif node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# Виконуємо DFS та BFS
start_node = 'A'
goal_node = 'E'

dfs_path = dfs(G, start_node, goal_node)
bfs_path = bfs(G, start_node, goal_node)

print(f"Шлях від {start_node} до {goal_node} за допомогою DFS: {dfs_path}")
print(f"Шлях від {start_node} до {goal_node} за допомогою BFS: {bfs_path}")

# Візуалізація графу та шляхів
pos = nx.get_node_attributes(G, 'pos')

plt.figure(figsize=(10, 5))

# Малюємо граф
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')

# Малюємо шлях DFS
if dfs_path:
    edge_list_dfs = list(zip(dfs_path, dfs_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edge_list_dfs, edge_color='red', width=2, label='DFS шлях')

# Малюємо шлях BFS
if bfs_path:
    edge_list_bfs = list(zip(bfs_path, bfs_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edge_list_bfs, edge_color='green', width=2, style='dashed', label='BFS шлях')

plt.legend(['Граф', 'DFS шлях', 'BFS шлях'])
plt.title("Порівняння шляхів DFS та BFS")
plt.show()
