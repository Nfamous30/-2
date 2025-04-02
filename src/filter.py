import json

with open("../data/edge/api组合次数.txt", "r") as load_f:
    edge_dict = json.load(load_f)

# edegSet = set()
# for d in edge_dict.keys():
#     keyList = d.split("&")
#     for k in keyList:
#         edegSet.add(k)
# print(len(edegSet))

with open("../data/edge/边节点顺序排列.txt", "r") as load_f:
    node_list = json.load(load_f)
print(len(node_list))
matrix_dimension = len(node_list)
api_titles = set()

node_index_dict = dict()
for i in range(matrix_dimension):
    # if i % 100 == 0:
    #     print(node_list[i])
    node_index_dict[node_list[i]] = i
    real_name = node_list[i].split("/")[-1]
    api_titles.add(real_name)

# print(node_index_dict["/api/43-places"])
# print(node_list[793])
# print(node_list[1215])
# 452、493
# 463、1067
with open('../data/data/api_data.json', 'r') as f:
    content = f.read()

# 分割JSON对象
objects = content.strip().split('\n')
data = []
for obj in objects:
    temp = json.loads(obj)
    real_name = temp['Name'].lower().replace(" ", "-")
    if real_name in api_titles:
        data.append(json.loads(obj))
print(len(data))
with open('../data/new/api_data_new.json', 'w') as f:
    json.dump(data, f)