from heapq import heappush, heappop
import ucs
from math import radians, cos, sqrt

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    cost: int
    node: Any=field(compare=False)
    path: Any=field(compare=False)

rBumi = 6371000

def heuristic(matrix, goal, nodes):
    h = [0] * len(matrix)
    for node in range(len(matrix)):
        cost, path = ucs(matrix, node, goal, nodes)
        h[node] = cost
    return h


def haversine(matrix, graph, gnode):
    h = [0] * len(matrix)
    g_lat = radians(graph.nodes[gnode]['y'])
    g_lon = radians(graph.nodes[gnode]['x'])
    for i in graph.nodes():
        lat1 = radians(graph.nodes[i]['y'])
        lon1 = radians(graph.nodes[i]['x'])
        x = (lon1 -g_lon) * cos(0.5 * (lat1 + g_lat))
        y = lat1 - g_lat
        hav= rBumi * sqrt(x * x + y * y)
        h[i] = hav
    return h

def astar(matrix, start, goal, nodes, heuristic):
    iteration = 0
    visited = set()
    queue = [PrioritizedItem(0, start, [])]
    while queue:
        item = heappop(queue)
        cost, node, path = item.cost, item.node, item.path
        if node not in visited:
            visited.add(node)
            path = path + [nodes[node]]
            if node == goal:
                return (cost, path)
            if (node != start):
                cost -= heuristic[node]
            for neighbor in range(len(matrix[node])):
                if matrix[node][neighbor] != 0 and neighbor not in visited:
                    costNow = cost + matrix[node][neighbor] + heuristic[neighbor]
                    heappush(queue, PrioritizedItem(costNow, neighbor, path))
    return (float("inf"), [])
