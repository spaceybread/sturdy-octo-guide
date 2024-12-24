import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(node_map, board):
    graph = nx.Graph()
    edge_list = list()
    
    for x in node_map.keys():
        nodes = node_map[x]
        
        for y in nodes:
            if (x, y) not in edge_list and (y, x) not in edge_list:
                edge_list.append((x, y))
    
    graph.add_edges_from(edge_list)
    all_y_values = [node[1] for node in graph.nodes()]
    max_y = max(all_y_values)
    pos = {node: (node[0], max_y - node[1]) for node in graph.nodes()}
    
    node_values = {node: board[node[0]][node[1]] for node in graph.nodes()}
    unique_values = list(set(node_values.values()))
    color_map = {value: i for i, value in enumerate(unique_values)}
    node_colors = [color_map[node_values[node]] for node in graph.nodes()]
    
    nx.draw_networkx(graph, pos, node_size=300, with_labels=True, node_color=node_colors)
    plt.show()

def print_puzzle(board, n):
    for i in range(n**2):
        for j in range(n**2):
            print(board[i][j], end=" ")
        print()

def get_neighbors(x, y, n):
    out = []
    
    for i in range(n**2):
        out.append((i, y))
        out.append((x, i))
    
    for i in range((x // n) * n, (x // n + 1) * n):
        for j in range((y // n) * n, (y // n + 1) * n):
            out.append((i, j))
    out = set(out)
    out.remove((x, y))
    return sorted(list(out))
    
    
def make_graph(board, n):
    out = {}
    for i in range(n**2):
        for j in range(n**2):
            out[(i, j)] = get_neighbors(i, j, n)
            print(i, j, out[(i, j)])
    return out

def get_predim(board, n):
    out = set()
    for i in range(n**2):
        for j in range(n**2):
            if board[i][j] != 0:
                out.add((i, j))
    return out
    
def idx_to_coord(idx, n):
    x = idx // (n**2)
    y = idx % (n**2)
    
    return x, y

def color(board, n, idx, predim):
    if idx == (n**4): return True
    x, y = idx_to_coord(idx, n)
    for clr in range(1, n**2 + 1):
        if can_color(board, n, x, y, clr, predim):
            board[x][y] = clr
            if color(board, n, idx + 1, predim): return True
        if (x, y) not in predim:
            board[x][y] = 0

def can_color(board, n, x, y, color, predim):
    if (x, y) in predim:
        if board[x][y] == color: return True
        else: return False
    
    neighbors = get_neighbors(x, y, n)
    
    for node in neighbors:
        if board[node[0]][node[1]] == color: return False
    return True

puzzle3x3 = [
[0, 0, 0, 4, 0, 0, 0, 0, 0],
[7, 2, 3, 0, 0, 9, 4, 0, 0],
[0, 0, 1, 0, 0, 0, 9, 0, 0],
[2, 0, 0, 8, 0, 3, 0, 5, 4],
[0, 0, 0, 2, 6, 0, 0, 0, 0],
[0, 0, 0, 0, 5, 0, 0, 0, 9],
[3, 0, 0, 0, 0, 0, 0, 0, 0],
[8, 7, 0, 0, 0, 6, 0, 0, 0],
[5, 0, 0, 3, 0, 8, 0, 7, 2]]

puzzle2x2 = [
[0, 1, 4, 0],
[0, 3, 0, 2],
[0, 0, 3, 0],
[0, 0, 0, 0]]

# init
puzzle = puzzle3x3
N = int(len(puzzle)**0.5)

print_puzzle(puzzle, N)
node_map = make_graph(puzzle, N)


predim = get_predim(puzzle, N)
color(puzzle, N, 0, predim)
print_puzzle(puzzle, N)

visualize_graph(node_map, puzzle)
