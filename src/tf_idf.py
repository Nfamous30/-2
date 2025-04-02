import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

# 计算n个api之间根据功能关键词列表进行tf-idf计算，并计算余弦相似度的结果矩阵

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


with open('../data/new/api_categories.json', 'r',encoding = 'utf-8') as f:
    api_categories = json.load(f)

# 将功能关键词转换为文本列表
docs = [' '.join(api) for api in api_categories]

# 计算TF-IDF矩阵
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(docs)

# 计算相似度矩阵
similarity_matrix = cosine_similarity(tfidf_matrix)

print(len(similarity_matrix))
# 输出相似度矩阵
print(similarity_matrix[0])
matrix_list = similarity_matrix.tolist()
count=0
for line in matrix_list:
    for num in line:
        if num>0.2:
            count+=1

print(count)
with open('../data/new/tag_tf_idf_matrix.json','a',encoding='utf-8') as f:
    json.dump(matrix_list, f)
print(len(matrix_list))
# 1123
# [1. 0. 0. ... 0. 0. 0.]
# 76902
# 1123

