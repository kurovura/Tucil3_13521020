import numpy as np
import matplotlib.pyplot as plt

matrix = []

def txtToGraph () :
    filename = input("nama file (harus .txt ya) : ")
    with open(filename, 'r') as f:
        next(f)  #skip baris pertama yang menginterpretasikan kota
        for line in f:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
    return matrix

def showGraph () :
    plt.imshow(txtToGraph(), cmap='hot', interpolation='nearest')
    plt.show()

# txtToGraph()
showGraph()

