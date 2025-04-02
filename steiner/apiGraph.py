# -*- coding: utf-8 -*-
"""
该文件定义了aGraph类，包含了生成steiner树时所需的一些图的方法

"""

class apiGraph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.dimension = len(self.matrix)
        
    def neighbors(self, u):
        neighbors = []
        # edges = []
        for i in range(self.dimension):
            if self.matrix[u][i] > 0:
                neighbors.append(i)
                # edges.append(self.matrix[u][i])
                
        return neighbors
    def edges(self, u):
        edges = []
        # edges = []
        for i in range(self.dimension):
            if self.matrix[u][i] > 0:
                edges.append(self.matrix[u][i])
                
        return edges
    
    

