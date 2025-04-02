import json


api_titles = set()
api_dict = json.load(open('../data/dataset/connected_api_dict.json'))
print(len(api_dict))
for api in api_dict:
    api_titles.add(api)
# 读取文件内容后，将每个JSON对象解析为Python字典，然后将这些字典组成一个Python列表，最后将列表转换为JSON数组。
# 读取文件内容
with open('../data/data/api_data.json', 'r') as f:
    content = f.read()

# 分割JSON对象
objects = content.strip().split('\n')

# 解析JSON对象为Python字典，并组成Python列表
data = []
for obj in objects:
    temp = json.loads(obj)
    if temp['Name'] in api_titles:
        data.append(json.loads(obj))

    # # 限制关注者大于10且依然活跃
    # if int(temp['Followers'])>=20:
    #     if 'Version status' in temp and 'active' in temp['Version status']:
    #         data.append(json.loads(obj))

print(len(data))
# # 将Python列表转换为JSON数组
# json_data = json.dumps(data)

# # 输出JSON数组
# # print(json_data)
# with open('api_data_new.json', 'w') as f:
#     json.dump(data, f)
