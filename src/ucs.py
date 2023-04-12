import heapq
import os
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    cost: int
    node: Any=field(compare=False)
    path: Any=field(compare=False)

def ucs(matrix, start, goal, nodes):
    visited = set()
    queue = [PrioritizedItem(0, start, [])]
    while queue:
        item = heapq.heappop(queue)
        cost, node, path = item.cost, item.node, item.path
        if node not in visited:
            visited.add(node)
            path = path + [nodes[node]]
            if node == goal:
                return (cost, path)
            for neighbor in range(len(matrix[node])):
                if matrix[node][neighbor] != 0 and neighbor not in visited:
                    costNow = cost + matrix[node][neighbor]
                    heapq.heappush(queue, PrioritizedItem(costNow, neighbor, path))

    return (float("inf"), [])


