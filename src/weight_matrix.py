import json

with open("../data/new/pairs_result.txt", "r",encoding='utf-8') as load_f:
    edge_dict = json.load(load_f)



with open("../data/new/edge_list.json", "r",encoding='utf-8') as load_f:
    node_list = json.load(load_f)
print(len(node_list))
matrix_dimension = len(node_list)

node_index_dict = dict()
for i in range(matrix_dimension):
    # if i % 100 == 0:
    #     print(node_list[i])
    node_index_dict[node_list[i]] = i



# 开始根据数组下标赋权重
weight_matrix = [[0 for i in range(matrix_dimension)] for j in range(matrix_dimension)]

for d in edge_dict.keys():
    keyList = d.split("&")
    
    node_i = node_index_dict[keyList[0]]
    node_j = node_index_dict[keyList[1]]
    weight_matrix[node_i][node_j] = edge_dict[d]
    weight_matrix[node_j][node_i] = edge_dict[d]

# with open('../data/new/weight_matrix.json','a',encoding='utf-8') as f:
#     json.dump(weight_matrix, f)
print(len(weight_matrix))
