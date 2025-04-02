import numpy as np
import json


# 
# with open('../data/res/company_matrix.json', 'r',encoding = 'utf-8') as f:
#     matrix1 = np.array(json.load(f))

# with open('../data/res/cn_matrix.json', 'r',encoding = 'utf-8') as f:
#     matrix2 = np.array(json.load(f))
# # 定义新矩阵
# n = len(matrix1)
# new_matrix = np.zeros((n, n))

# # 计算新矩阵的值
# for i in range(n):
#     for j in range(n):
#         if matrix2[i][j] < 1:
#             new_matrix[i][j] = matrix1[i][j]
#         else:
#             new_matrix[i][j] = matrix1[i][j] * matrix2[i][j]


# with open('../data/res/new_company_matrix.json','w',encoding='utf-8') as f:
#     json.dump(new_matrix.tolist(), f)

with open('../data/res/follower_matrix.json', 'r',encoding = 'utf-8') as f:
    matrix1 = np.array(json.load(f))

with open('../data/res/cn_matrix.json', 'r',encoding = 'utf-8') as f:
    matrix2 = np.array(json.load(f))
# 定义新矩阵
n = len(matrix1)
new_matrix = np.zeros((n, n))

# 计算新矩阵的值
for i in range(n):
    for j in range(n):
        if matrix2[i][j] < 1:
            new_matrix[i][j] = matrix1[i][j]
        else:
            new_matrix[i][j] = matrix1[i][j] * matrix2[i][j]
nonzero_indices = np.nonzero(new_matrix)  # 获取非零元素的下标
new_matrix[nonzero_indices] = np.sqrt(new_matrix[nonzero_indices])
# 对所有元素保留小数点后3位
new_matrix = np.round(new_matrix, decimals=3)
with open('../data/res2/new_follower_matrix.json','w',encoding='utf-8') as f:
    json.dump(new_matrix.tolist(), f)
