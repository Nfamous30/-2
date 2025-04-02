import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import json

# 加载组合次数矩阵
with open('../data/res/weight_matrix.json', 'r',encoding = 'utf-8') as f:
    matrix = np.array(json.load(f))

# # 定义矩阵
# matrix = np.array([[0, 2, 1, 0],
#                    [2, 0, 1, 0],
#                    [1, 1, 0, 1],
#                    [0, 0, 1, 0]])

# 构建图对象
G = nx.from_numpy_array(matrix)

# 计算节点对之间的共同邻居数量，并保存到矩阵中
cn_matrix = np.zeros_like(matrix)
for i in range(matrix.shape[0]):
    for j in range(i + 1, matrix.shape[1]):
        cn = len(list(nx.common_neighbors(G, i, j)))
        cn_matrix[i][j] = cn_matrix[j][i] = cn

print(cn_matrix[0])

# 计算节点对之间的资源分配指数，并保存到矩阵中
ra_matrix = np.zeros_like(matrix)
for i in range(matrix.shape[0]):
    for j in range(i + 1, matrix.shape[1]):
        ra = nx.resource_allocation_index(G, [(i, j)])
        for u, v, p in ra:
            ra_matrix[i][j] = ra_matrix[j][i] = p

print(ra_matrix[0])
