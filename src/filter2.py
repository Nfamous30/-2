import json


with open('../data/new/api_data_new.json', 'r',encoding = 'utf-8') as f:
    content = f.read()

node_list = json.loads(content)

print(len(node_list))
matrix_dimension = len(node_list)
api_titles = set()

node_index_dict = dict()
for i in range(matrix_dimension):
    real_name = node_list[i]['Name'].lower().replace(" ", "-")
    api_titles.add(real_name)

with open("../data/edge/边节点顺序排列.txt", "r",encoding='utf-8') as load_f:
    edge_list = json.load(load_f)
new_edge_list = []
for edge in edge_list:
    if edge.split("/")[-1] in api_titles:
        new_edge_list.append(edge)

print(len(new_edge_list))
# with open('../data/new/edge_list.json','a',encoding='utf-8') as f:
#     json.dump(new_edge_list, f)

# with open("../data/edge/api_use.json", "r",encoding='utf-8') as load_f:
#     api_use_list = json.load(load_f)
# new_api_use_dict = {}
# # print(api_use_list)
# for edge in api_use_list:
#     # print(edge)
#     if edge.split("/")[-1] in api_titles:
#         new_api_use_dict[edge]=api_use_list[edge]

# print(len(new_api_use_dict))
# with open('../data/new/api_use.json','a',encoding='utf-8') as f:
#     json.dump(new_api_use_dict, f)



with open("../data/edge/category_dict.json", "r",encoding='utf-8') as load_f:
    category_dict_list = json.load(load_f)
new_category_dict = {}
for edge in category_dict_list:
    if edge.split("/")[-1] in api_titles:
        new_category_dict[edge]=category_dict_list[edge]

print(len(new_category_dict))
with open('../data/new/category_dict.json','a',encoding='utf-8') as f:
    json.dump(new_category_dict, f)




