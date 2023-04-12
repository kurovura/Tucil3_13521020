import ucs
import graph
import astar

nodes, mat = graph.inputFile()
snode, gnode = graph.inputNode(nodes)
print ("Hasil dengan ucs")

ucsp, ucsc = ucs.ucs(mat,snode, gnode, nodes)
graph.showgraph(mat,nodes,ucsp)
print("path = ", ucsp)
print("cost = ", ucsc)
