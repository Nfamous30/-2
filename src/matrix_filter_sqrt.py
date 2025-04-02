import numpy as np
import json

# # 加载组合次数矩阵
# with open('../data/res/new_company_matrix.json', 'r',encoding = 'utf-8') as f:
#     matrix = np.array(json.load(f))

# # 将矩阵中非零元素开方
# nonzero_indices = np.nonzero(matrix)  # 获取非零元素的下标
# matrix[nonzero_indices] = np.sqrt(matrix[nonzero_indices])
# # 对所有元素保留小数点后3位
# matrix = np.round(matrix, decimals=3)

# with open('../data/res2/new_company_matrix.json','a',encoding='utf-8') as f:
#     json.dump(matrix.tolist(), f)

# 加载组合次数矩阵
with open('../data/res/follower_matrix.json', 'r',encoding = 'utf-8') as f:
    matrix = np.array(json.load(f))

# 将矩阵中非零元素开方
nonzero_indices = np.nonzero(matrix)  # 获取非零元素的下标
matrix[nonzero_indices] = np.sqrt(matrix[nonzero_indices])
# 对所有元素保留小数点后3位
matrix = np.round(matrix, decimals=3)

with open('../data/res2/follower_matrix.json','a',encoding='utf-8') as f:
    json.dump(matrix.tolist(), f)
