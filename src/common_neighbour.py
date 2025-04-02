
import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 加载组合次数矩阵
with open('../data/res/weight_matrix.json', 'r',encoding = 'utf-8') as f:
    weight_matrix = np.array(json.load(f))

# 构建无向图
G = nx.Graph(weight='weight')
n = len(weight_matrix)
G.add_nodes_from(range(n))
for i in range(n):
    for j in range(i + 1, n):
        weight = weight_matrix[i][j]
        if weight > 0:
            G.add_edge(i, j, weight=weight)

print(n)

cn_matrix = nx.cn_soundarajan_hopcroft(G, community='weight')
# 计算节点之间的资源分配指数
ra_matrix = nx.resource_allocation_index(G)

cn_matrix_list = list(cn_matrix)
ra_matrix_list = list(ra_matrix)
print("共同邻居矩阵：")
print(cn_matrix_list[0])

print("资源分配指数矩阵：")
print(ra_matrix_list[0])



# # 将共同邻居矩阵存储到本地
# with open('../data/res/cn_matrix.json', 'w',encoding = 'utf-8') as f:
#     json.dump(nx.to_numpy_array(cn_matrix), f)

# # 将Jaccard相似性矩阵存储到本地
# with open('../data/res/jaccard_matrix.json', 'w',encoding = 'utf-8') as f:
#     json.dump(nx.to_numpy_array(jaccard_matrix), f)

# # 将资源分配指数矩阵存储到本地
# with open('../data/res/ra_matrix.json', 'w',encoding = 'utf-8') as f:
#     json.dump(nx.to_numpy_array(ra_matrix), f)



# # 绘制图G
# # 使用 spring_layout 布局节点
# pos = nx.spring_layout(G, k=0.2, scale=2)

# # 绘制节点和边
# nx.draw_networkx_nodes(G, pos, node_size=100)
# nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.7)

# # 显示节点标签
# labels = {i: f'node {i}' for i in G.nodes()}
# nx.draw_networkx_labels(G, pos, labels, font_size=8)

# # 显示图像
# plt.axis('off')
# plt.show()