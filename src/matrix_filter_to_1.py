import numpy as np
import json

# 加载组合次数矩阵
with open('../data/res/weight_matrix.json', 'r',encoding = 'utf-8') as f:
    matrix = np.array(json.load(f))
# 使用numpy的log函数进行Log归一化
log_norm_matrix = np.log(matrix + 1)
# 对所有元素保留小数点后3位
log_norm_matrix = np.round(log_norm_matrix, decimals=3)

with open('../data/res3/weight_matrix.json','a',encoding='utf-8') as f:
    json.dump(log_norm_matrix.tolist(), f)

# 加载cn矩阵
with open('../data/res/cn_matrix.json', 'r',encoding = 'utf-8') as f:
    matrix = np.array(json.load(f))
# 使用numpy的log10函数进行Log归一化
log_norm_matrix = np.log(matrix + 1)
# 对所有元素保留小数点后3位
log_norm_matrix = np.round(log_norm_matrix, decimals=3)

with open('../data/res3/cn_matrix.json','a',encoding='utf-8') as f:
    json.dump(log_norm_matrix.tolist(), f)

# # 加载interface矩阵
# with open('../data/res/interface_matrix.json', 'r',encoding = 'utf-8') as f:
#     matrix = np.array(json.load(f))
# # 使用numpy的log10函数进行Log归一化
# log_norm_matrix = np.log10(matrix + 1)
# # 对所有元素保留小数点后3位
# log_norm_matrix = np.round(log_norm_matrix, decimals=3)

# with open('../data/res1/interface_matrix.json','a',encoding='utf-8') as f:
#     json.dump(log_norm_matrix.tolist(), f)

# # 加载tf_idf矩阵
# with open('../data/res/tag_tf_idf_matrix.json', 'r',encoding = 'utf-8') as f:
#     matrix = np.array(json.load(f))
# # 使用numpy的log10函数进行Log归一化
# log_norm_matrix = np.log10(matrix + 1)
# # 对所有元素保留小数点后3位
# log_norm_matrix = np.round(log_norm_matrix, decimals=3)

# with open('../data/res1/tf_idf_matrix.json','a',encoding='utf-8') as f:
#     json.dump(log_norm_matrix.tolist(), f)

# 加载follower矩阵
with open('../data/res2/new_follower_matrix.json', 'r',encoding = 'utf-8') as f:
    matrix = np.array(json.load(f))
# 使用numpy的log10函数进行Log归一化
log_norm_matrix = np.log(matrix + 1)
# 对所有元素保留小数点后3位
log_norm_matrix = np.round(log_norm_matrix, decimals=3)

with open('../data/res3/follower_matrix.json','a',encoding='utf-8') as f:
    json.dump(log_norm_matrix.tolist(), f)

# 加载company矩阵
with open('../data/res2/new_company_matrix.json', 'r',encoding = 'utf-8') as f:
    matrix = np.array(json.load(f))
# 使用numpy的log函数进行Log归一化
log_norm_matrix = np.log(matrix + 1)
# 对所有元素保留小数点后3位
log_norm_matrix = np.round(log_norm_matrix, decimals=3)

with open('../data/res3/company_matrix.json','a',encoding='utf-8') as f:
    json.dump(log_norm_matrix.tolist(), f)