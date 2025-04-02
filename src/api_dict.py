import json

# # 读取 JSON 文件并解析为 Python 字典对象
# with open('../data/new/edge_list.json', 'r',encoding='utf-8') as f:
#     api_names = json.load(f)

# # 创建空字典用于存储 API 名称和对应的顺序
# api_order = {}

# # 使用 enumerate() 函数遍历 API 名称，并赋予顺序
# for i, api_name in enumerate(api_names):
#     api_order[api_name.split('/')[-1]] = i

# # 将更新后的字典转换为 JSON 格式
# api_order_json = json.dumps(api_order)

# # 将 JSON 写入到文件中
# with open('../data/new/connected_api_dict.json', 'w',encoding='utf-8') as f:
#     f.write(api_order_json)

# 读取 JSON 文件并解析为 Python 字典对象
with open('../dataset/category_dict.json', 'r',encoding='utf-8') as f:
    data = json.load(f)


# 构建新的字典
new_data = {}
for key, value in data.items():
    new_key = key.split('/')[-1]  # 使用 '/' 分隔字符串，取最后一部分作为新的 key
    new_data[new_key] = value

# 保存新的字典为 JSON 文件
with open('../dataset/new_category_dict.json', 'w') as file:
    json.dump(new_data, file)
