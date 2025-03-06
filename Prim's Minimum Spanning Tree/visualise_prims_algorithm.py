import heapq
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import defaultdict

def read_graph():
    """
    Reads the graph from 'edges.txt' and return it as an adjacency list + node set.
    :return:
    """
    with open('edges.txt') as file:
        num_nodes, num_edges = map(int, file.readline().split())

        graph = defaultdict(list)
        edges = []
        nodes = set()

        for line in file:
            node_1, node_2, cost = map(int, line.split())
            graph[node_1].append((cost, node_2))
            graph[node_2].append((cost, node_1))
            edges.append((node_1, node_2, cost))
            nodes.add(node_1)
            nodes.add(node_2)

    return graph, edges, nodes

def prims_mst_visual(graph: dict, edges: list, nodes: set):
    """
    Implements Prim's Algorithm and dynamically visualizes the process.
    """

    start_node = next(iter(nodes))  # Pick any node as start
    visited = set([start_node])
    min_heap = []
    mst_edges = []

    # Add all edges from start_node to the heap
    for cost, neighbor in graph[start_node]:
        heapq.heappush(min_heap, (cost, start_node, neighbor))

    # Create the initial graph visualization
    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    # Set up plot
    fig, ax = plt.subplots(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)  # Positions for nodes

    # === Animation Function ===
    def update(frame):
        if len(visited) == len(nodes):  # Stop when MST is complete
            return

        while min_heap:
            cost, node_1, node_2 = heapq.heappop(min_heap)  # Get the smallest edge

            if node_2 not in visited:
                visited.add(node_2)
                mst_edges.append((node_1, node_2))  # Add edge to MST

                for edge_cost, neighbor in graph[node_2]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (edge_cost, node_2, neighbor))

                break  # Process one edge per frame for animation

        ax.clear()
        ax.set_title(f"Prim's Minimum Spanning Tree (Step {frame+1})")

        # Draw full graph with light gray edges
        nx.draw(G, pos, with_labels=True, font_weight='bold', font_size=8, ax=ax,
                node_color='lightblue', edge_color='gray')

        # Draw MST edges in red
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red', width=2, ax=ax)

            # Save the last frame as an image
        if frame == len(nodes) - 2:
            plt.savefig("prims_mst_visual.png", dpi=300)
            print(f"Imagine saved to prims_mst_visual.png")

    ani = animation.FuncAnimation(fig, update, frames=len(nodes) - 1, repeat=False, interval=1000)
    plt.show()

if __name__ == '__main__':
    graph, edges, nodes = read_graph()
    prims_mst_visual(graph, edges, nodes)

