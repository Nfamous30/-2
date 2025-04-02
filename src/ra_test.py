import numpy as np
from scipy.optimize import linear_sum_assignment
import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
# 加载组合次数矩阵
with open('../data/res/weight_matrix.json', 'r',encoding = 'utf-8') as f:
    weight_matrix = np.array(json.load(f))
def resource_allocation(M):
    n = M.shape[0] # 矩阵大小为 n x n
    cost_matrix = -M # 将边权重取负，转换为最小权重匹配问题
    row_ind, col_ind = linear_sum_assignment(cost_matrix) # 执行资源分配算法
    S = np.zeros((n,n)) # 初始化相似度矩阵
    for i, j in zip(row_ind, col_ind):
        S[i,j] = 1 # 填充相似度矩阵，匹配节点相似度为1
    return S

# 示例
S = resource_allocation(weight_matrix) # 计算相似度矩阵
print(S[0])
# # 将共同邻居矩阵存储到本地
with open('../data/res/ra_matrix.json', 'w',encoding = 'utf-8') as f:
    json.dump(S.tolist(), f)
