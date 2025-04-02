import json
import numpy as np



with open('../data/res/weight_matrix.json', 'r',encoding = 'utf-8') as f:
    data = json.load(f)
# with open('../data/new/interface_matrix.json', 'r',encoding = 'utf-8') as f:
#     data = json.load(f)

# 将json解析后转换为list格式
matrix_list = []
for row in data:
    matrix_list.append(list(row))

matrix = np.array(matrix_list)

# 将非零元素取倒数并保留3位小数
nonzero_mask = matrix != 0  # 找出非零元素的位置
reciprocal_matrix = np.zeros_like(matrix, dtype=float)  # 初始化一个浮点数类型的矩阵
reciprocal_matrix[nonzero_mask] = 1 / matrix[nonzero_mask]  # 将非零元素取倒数
reciprocal_matrix = np.around(reciprocal_matrix, decimals=3)  # 保留3位小数

print(reciprocal_matrix[0])

with open('../data/res2/weight_matrix.json','a',encoding='utf-8') as f:
    json.dump(reciprocal_matrix.tolist(), f)
# with open('../data/res/interface_matrix.json','a',encoding='utf-8') as f:
#     json.dump(matrix.tolist(), f)
print(len(reciprocal_matrix))

    