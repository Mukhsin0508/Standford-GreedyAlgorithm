import heapq
from collections import defaultdict


def minimum_spanning_tree():
    """
    Code up Prim's Minimum Spanning Tree Algorithm (O(mn) naive version)
    :return: overall cost of a minimum spanning tree --- an integer, which may or may not be negative ---
    """
    with open('edges.txt', 'r') as file:
        #  === Read first line -> number of nodes and edges ===
        nums_nodes, nums_edges = map(int, file.readline().split())

        # === Graph as adjacency list ===
        graph = defaultdict(list)

        # === Read all edges and store them in graph ===
        for line in file:
            node_1, node_2, cost = map(int, line.split())
            graph[node_1].append((cost, node_2)) # === Store (cost, neighbor)
            graph[node_2].append((cost, node_1)) # === Since the graph is undirected.

    print(f"Graph successfully loaded: ", dict(graph)) # === Debugging check ===

    # ===== 2. Implement Prim's Algorithm =====

    # === Starting from any node (e.g., node 1)
    start_node = 1
    min_cost = 0
    visited = set() # === To track which nodes are in MST

    # === Min-heap (priority queue) to get the smallest edge quickly ===
    min_heap = []

    # === Add all edges of the starting node to the heap ===
    visited.add(start_node)
    for cost, neighbor in graph[start_node]:
        heapq.heappush(min_heap, (cost, start_node, neighbor))
    print("Starting MST...")

    while len(visited) < nums_nodes:
        # === Get the smallest edge (cost, node_1, node_2)
        cost, node_1, node_2 = heapq.heappop(min_heap)

        if node_2 in visited:
            continue # === Skip if the node is already in the MST

        # === Add node to MST ===
        visited.add(node_2)
        min_cost += cost # === Add edge cost ===

        # === Add all edges from the new node ===
        for edge_cost, neighbor in graph[node_2]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_cost, node_2, neighbor))

    print(f"Minimum cost: {min_cost}")

if __name__ == '__main__':
    minimum_spanning_tree()
