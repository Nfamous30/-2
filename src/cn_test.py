import numpy as np
import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 加载组合次数矩阵
with open('../data/res/weight_matrix.json', 'r',encoding = 'utf-8') as f:
    weight_matrix = np.array(json.load(f))

def common_neighbors(M):
    n = M.shape[0] # 矩阵大小为 n x n
    S = np.zeros((n,n)) # 初始化相似度矩阵
    for i in range(n):
        for j in range(i+1, n): # 只需计算上三角矩阵，下三角可以直接对称得到
            common = np.sum(np.logical_and(M[i], M[j])) # 计算共同邻居数量
            S[i,j] = S[j,i] = common # 填充相似度矩阵
    return S

# # 示例
# M = np.array([[0, 2, 1], [2, 0, 3], [1, 3, 0]]) # 一个3x3的示例矩阵
S = common_neighbors(weight_matrix) # 计算相似度矩阵
print(S[0])
# # 将共同邻居矩阵存储到本地
with open('../data/res/cn_matrix.json', 'w',encoding = 'utf-8') as f:
    json.dump(S.tolist(), f)
