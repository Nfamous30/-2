# 资源分配
import json
import numpy as np
import networkx as nx


# 从 api_data.json 文件中读取 API 信息，并构建一个 NetworkX 图对象
with open('api_data.json', 'r', encoding='utf-8') as f:
    api_data = json.load(f)

G = nx.Graph()

for api_info in api_data:
    G.add_node(api_info['id'], name=api_info['name'])

# 从 mashup_data 中读取 mashup 数据，并在图中添加边
with open('mashup_data.json', 'r', encoding='utf-8') as f:
    mashup_data = json.load(f)

for mashup_info in mashup_data:
    api_ids = mashup_info['api_ids']
    for i in range(len(api_ids)):
        for j in range(i+1, len(api_ids)):
            G.add_edge(api_ids[i], api_ids[j], mashup_id=mashup_info['id'])

# 构建邻接矩阵
adj_matrix = np.zeros((len(api_data), len(api_data)))



# 计算资源分配相似性
def get_ra_similarity(api_id1, api_id2):
    numerator = 0.0
    for j in range(len(api_data)):
        if adj_matrix[api_id1][j] and adj_matrix[api_id2][j]:
            numerator += 1.0 / degree[j]
    denominator = degree[api_id1] * degree[api_id2]
    if denominator == 0:
        return 0.0
    else:
        return numerator / denominator

# 找到每个api的前k个相似的api
k = 5
similar_apis = {}
for api_id in api_ids:
    similarities = []
    for other_api_id in api_ids:
        if api_id != other_api_id:
            similarity = get_ra_similarity(api_id, other_api_id)
            similarities.append((other_api_id, similarity))
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:k]
    similar_apis[api_id] = similarities

# 打印每个api的前k个相似的api
