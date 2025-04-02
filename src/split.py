import json
from collections import OrderedDict

# 创建一个有序字典
my_dict = OrderedDict()

# 定义一个空的集合或字典，用于存储 API 的 title
api_names = set()
# 或者
# api_titles = {}

# 打开文本文件并读取数据
with open('../data/api_mashup/active_apis_data.txt', 'r',encoding='utf-8') as f:
        json_str = f.read()

# 将 JSON 字符串转换为 Python 对象
json_data = json.loads(json_str)
i=0
for data in json_data:
        if data and  'title' in data and data['title']:
        # print(data['title'])
                index=data['title'].find('API')
                # print(index)
                name=data['title'][:index].strip()
                api_names.add(name)

# 输出 Python 对象
print(len(api_names))
# first =api_names.pop(0)
with open('../data/data/api_data.json', 'r',encoding='utf-8') as f:
    content = f.read()

# 分割JSON对象
objects = content.strip().split('\n')

# 解析JSON对象为Python字典，并组成Python列表
data = []
item = set()
category_set=set()
prime_category_dict=OrderedDict()
item_dict=OrderedDict()
api_category_dict=OrderedDict()
i=0
for obj in objects:
    temp = json.loads(obj)
    if temp['Name'] in api_names:
        # data.append(json.loads(obj))

        # 限制关注者大于10且依然活跃
        if int(temp['Followers'])>=10:
                if 'Version status' in temp and 'active' in temp['Version status'] and 'Primary Category' in temp and temp['Primary Category']:
                        data.append(json.loads(obj))
                        item.add(temp['Name'])
                        category = temp['Primary Category']
                        prime_category_dict[temp['Name']]=category
                        if 'Secondary Categories' in temp and temp['Secondary Categories']:
                              category+=','+temp['Secondary Categories']
                        api_category_dict[temp['Name']]=category
                        categories = category.split(',')
                        for cate in categories:
                              category_set.add(cate)

print(len(data))
print(len(item))
for api in item:
       item_dict[api]=i
       i+=1

print(len(item_dict))

print(len(category_set))

category_list = [str(item) for item in category_set]
# 将category列表存储
# with open("../data/write/category_list.json", "w") as f:
#     json.dump(category_list, f)



# # 将字典序列化为JSON字符串
# json_str = json.dumps(item_dict)

# 将api序号列表存储
# with open("../data/write/api_dict.json", "w",encoding='utf-8') as f:
#     f.write(json_str)
#     # 将字典序列化为JSON字符串
# api_category_str = json.dumps(api_category_dict)

# 将api-category对应关系存储
# with open("../data/write/api_category_dict.json", "w",encoding='utf-8') as f:
#     f.write(api_category_str)

# api_prime_category_str = json.dumps(prime_category_dict)

# # 将api-prime_category对应关系存储
# with open("../data/write/api_prime_category_dict.json", "w",encoding='utf-8') as f:
#     f.write(api_prime_category_str)
