# 计算拥有共同关注者的矩阵
import json

# 读取API数据文件，获取API的名称列表
with open('../data/new/api_data_new.json', 'r',encoding = 'utf-8') as f:
    api_data = json.load(f)

api_names = [api['Name'] for api in api_data]

# 为每个API分配一个唯一的编号
api_indices = {api_name: i for i, api_name in enumerate(api_names)}

# 获取API数量
n = len(api_names)

# 初始化关联矩阵
adj_matrix = [[0] * n for _ in range(n)]

follower_dict ={}

# 处理follower.txt文件
with open('../data/follower/filtered_follower.txt', "r",encoding='utf-8') as f:
    for line in f:
        follower, api_names = line.strip().split("#####")
        if follower not in follower_dict:
            follower_dict[follower] = []
        if api_names in api_names:
            follower_dict[follower].append(api_names)
print(len(follower_dict))
for follower in follower_dict:
    api_list = follower_dict[follower]
    for i in range(len(api_list)):
        for j in range(i + 1, len(api_list)):
            api1_index = api_indices[api_list[i]]
            api2_index = api_indices[api_list[j]]
            adj_matrix[api1_index][api2_index] += 1
            adj_matrix[api2_index][api1_index] += 1

# 输出关联矩阵
print(len(adj_matrix))
print(adj_matrix[0])
with open('../data/res/follower_matrix.json','a',encoding='utf-8') as f:
    json.dump(adj_matrix, f)

