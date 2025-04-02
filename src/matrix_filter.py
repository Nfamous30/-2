import json
import numpy as np



# 加载weight矩阵
with open('../data/res3/weight_matrix.json', 'r',encoding = 'utf-8') as f1:
    matrix1 = np.array(json.load(f1))
# 加载cn矩阵
with open('../data/res3/cn_matrix.json', 'r',encoding = 'utf-8') as f2:
    matrix2 = np.array(json.load(f2))
# 加载company矩阵
with open('../data/res3/company_matrix.json', 'r',encoding = 'utf-8') as f3:
    matrix3 = np.array(json.load(f3))
# 加载follower矩阵
with open('../data/res3/follower_matrix.json', 'r',encoding = 'utf-8') as f4:
    matrix4 = np.array(json.load(f4))
# 加载tf_idf矩阵
with open('../data/res3/tag_tf_idf_matrix.json', 'r',encoding = 'utf-8') as f5:
    matrix5 = np.array(json.load(f5))

# 归一化处理
def normalize(matrix):
    max_val = np.max(matrix)
    min_val = np.min(matrix)
    if max_val == min_val:
        return matrix
    return (matrix - min_val) / (max_val - min_val)

matrix1_norm = normalize(matrix1)
matrix2_norm = normalize(matrix2)
matrix3_norm = normalize(matrix3)
matrix4_norm = normalize(matrix4)
matrix5_norm = normalize(matrix5)


# 数值相加
result = matrix1_norm + matrix2_norm+matrix3_norm+matrix4_norm+matrix5_norm
with open('../dataset/graph_ori.json','w',encoding='utf-8') as f:
    json.dump(result.tolist(), f)

# 归一化处理并二值化
result_norm = normalize(result)
result_norm[result_norm >= 0.2] = 1
result_norm[result_norm < 0.2] = 0

print(result_norm)

with open('../data/res3/graph_matrix.json','w',encoding='utf-8') as f:
    json.dump(result_norm.tolist(), f)
with open('../dataset/graph.json','w',encoding='utf-8') as f:
    json.dump(result_norm.tolist(), f)
# with open('../data/res/interface_matrix.json','a',encoding='utf-8') as f:
#     json.dump(matrix.tolist(), f)
print(len(result_norm))
# 统计非0元素的个数
nonzero_count = np.count_nonzero(result_norm)
print(nonzero_count)

# # 加载graph矩阵
# with open('../data/dataset/graph.json', 'r',encoding = 'utf-8') as f6:
#     matrix6 = np.array(json.load(f6))
# print(np.count_nonzero(matrix6))

    
