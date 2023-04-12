import networkx as nx
import os
import matplotlib.pyplot as plt

def inputFile():
    while True:
        fname = input("Masukkan nama file : ")
        file = os.path.join('..\\test', fname)
        
        try:
            with open(file, 'r') as f:
                line = f.readline()
                nodes = [str(x) for x in line.strip().split()]
                n_nodes = len(nodes)
                if n_nodes < 8:
                    raise ValueError("unvalid total node")
                
                matrix = []
                for i in range(n_nodes):
                    line = f.readline()
                    row = line.strip().split()
                    if len(row) != n_nodes:
                        raise ValueError("matrix unvalid.")
                    try:
                        row = [int(elmt) for elmt in row]
                        for elmt in row :
                            if elmt < 0 :
                                raise ValueError("bobot tidak valid")
                        matrix.append(row)
                    except ValueError:
                        raise ValueError("unvalid matrix")
                return nodes, matrix
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")
            continue


def inputNode(nodes: list):
    print("\n")
    print("Daftar nodes :")
    for i in range(len(nodes)):
        print(f"{i+1} {nodes[i]}")
    while True:
        try:
            inputNode = int(input("start node: "))
            if inputNode < 1 or inputNode > len(nodes):
                print("Masukkan node start valid")
                continue
            snode = inputNode - 1
            break
        except ValueError:
            print("Masukkan node dalam angka")
    print("\n")
    print("Daftar nodes :")
    for i in range(len(nodes)):
        if i < snode:
            print(f"{i+1} {nodes[i]}")
        elif i > snode:
            print(f"{i} {nodes[i]}")
    while True:
        try:
            inputNode = int(input("node goal : "))
            if inputNode < 1 or inputNode > len(nodes) - 1:
                print("masukkan node goal yang valid")
                continue
            if inputNode - 1 < snode:
                gnode = inputNode - 1
            else:
                gnode = inputNode
            break
        except ValueError:
            print("Masukkan node dalam angka")
    return snode, gnode


def showgraph(graph, nodes, path):
   
    if len(nodes) == 0:
        print("[]")
    else:
        labels = {k: v for k, v in enumerate(nodes)}
        G = nx.Graph()
        for i in range(len(graph)):
            for j in range(i+1, len(graph[i])):
                if graph[i][j] != 0:
                    G.add_edge(labels[i], labels[j], weight=graph[i][j])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_weight='bold')
        if isinstance(path, float):
            path = [path]  
        edge_colors = ['b' if (path[i], path[i+1]) in nx.edges(G) else 'k' for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], edge_color='y', width=5)
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
        plt.show()
