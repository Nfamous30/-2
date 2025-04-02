import json

with open("../data/new/pairs_result.txt", "r",encoding='utf-8') as load_f:
    edge_dict = json.load(load_f)

# edegSet = set()
# for d in edge_dict.keys():
#     keyList = d.split("&")
#     for k in keyList:
#         edegSet.add(k)
# print(len(edegSet))

with open("../data/new/edge_list.json", "r",encoding='utf-8') as load_f:
    node_list = json.load(load_f)
print(len(node_list))
matrix_dimension = len(node_list)

node_index_dict = dict()
for i in range(matrix_dimension):
    # if i % 100 == 0:
    #     print(node_list[i])
    node_index_dict[node_list[i]] = i
result = [None] * len(node_list) # 创建对应长度的列表

# for i in range(len(data)):
#     result[indexes[i]] = data[i] # 将数据填充到对应下标的位置上


with open("../data/new/category_dict.json", "r",encoding='utf-8') as load_f:
    category_dict_list = json.load(load_f)
new_category_dict = {}
for edge in category_dict_list:
        index = node_index_dict[edge]
        result[index]=category_dict_list[edge]

with open('../data/new/api_categories.json','a',encoding='utf-8') as f:
    json.dump(result, f)