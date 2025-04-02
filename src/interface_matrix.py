import json


import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


with open('../data/new/api_data_new.json', 'r',encoding = 'utf-8') as f:
    content = f.read()

data = json.loads(content)

# 将所有文本放入一个列表中
docs = []
for api in data:
    docs.append(api['Desc'])

# 计算TF-IDF矩阵
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(docs)

# 计算相似度矩阵
similarity_matrix = cosine_similarity(tfidf_matrix)

# 输出相似度矩阵
print(similarity_matrix[0])
matrix_list = similarity_matrix.tolist()
count=0
for line in matrix_list:
    for num in line:
        if num>0.2:
            count+=1

print(count)
with open('../data/new/interface_matrix.json','a',encoding='utf-8') as f:
    json.dump(matrix_list, f)
print(len(matrix_list))

