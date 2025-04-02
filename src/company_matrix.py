# 计算同公司的矩阵
# API Provider
import json
import pandas as pd

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


with open('../data/new/api_data_new.json', 'r',encoding = 'utf-8') as f:
    data = json.load(f)


# 将json数据转换为DataFrame
df = pd.DataFrame(data)

# 创建二维矩阵
n = len(df)
adj_matrix = [[0] * n for _ in range(n)]

# 填充矩阵
providers = df['API Provider'].unique()
for provider in providers:
    provider_df = df[df['API Provider'] == provider]
    provider_indices = provider_df.index.tolist()
    for i in provider_indices:
        for j in provider_indices:
            adj_matrix[i][j] += len(provider_indices)

# 将主对角线上的元素置为0
for i in range(n):
    adj_matrix[i][i] = 0
print(adj_matrix[0])
matrix_list = adj_matrix
count=0
for line in matrix_list:
    for num in line:
        if num>0.2:
            count+=1

print(count)
with open('../data/res/company_matrix.json','a',encoding='utf-8') as f:
    json.dump(matrix_list, f)
print(len(matrix_list))

