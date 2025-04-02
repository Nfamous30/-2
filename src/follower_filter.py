import json

# 读取api_data.json文件，获取API的名称列表
with open('../data/new/api_data_new.json' ,'r',encoding = 'utf-8') as f:
    api_data = json.load(f)

api_names = set([api['Name'] for api in api_data])

# 过滤follower.txt文件
with open('../data/follower/followers_data.txt', 'r',encoding = 'utf-8') as f, open('../data/follower/filtered_follower.txt', 'w',encoding = 'utf-8') as fw:
    for line in f:
        api_name = line.split('#####')[1].strip()
        if api_name in api_names:
            fw.write(line)
