import json

api_titles = set()
api_index = {}
api_dict = json.load(open('../data/new/edge_list.json','r',encoding = 'utf-8'))
print(len(api_dict))
i=0
for api in api_dict:
    temp = api.split('/')[-1]
    api_titles.add(temp)
    api_index[temp] = i
    i+=1
# 读取文件内容后，将每个JSON对象解析为Python字典，然后将这些字典组成一个Python列表，最后将列表转换为JSON数组。
print(i)
with open('../data/new/api_data.json', 'r',encoding = 'utf-8') as f:
    objects = json.load(f)

# 解析JSON对象为Python字典，并组成Python列表
indices = []
for obj in objects:
    real_name = obj['Name'].lower().replace(" ", "-")
    if real_name in api_titles:
        indices.append(int(api_index[real_name]))
print(api_titles)


# 使用切片按照坐标重新排列列表
print(len(indices))

# 使用zip()函数将两个列表组合成元组的列表
combined_list = list(zip(objects, indices))

# 使用sorted()函数对元组列表进行排序，并按照下标排序
sorted_list = sorted(combined_list, key=lambda x: x[1])

# 使用列表推导式获取排列后的JSON对象，并添加到一个新的列表中
sorted_json_list = [x[0] for x in sorted_list]
print(sorted_json_list[0])
with open('../data/new/api_data_new.json', 'w') as f:
    json.dump(sorted_json_list, f)
