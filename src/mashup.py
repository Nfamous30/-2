import json
from collections import OrderedDict

with open('../data/data/api_data.json', 'r',encoding='utf-8') as f:
    content = f.read()
mashup_api_dict=OrderedDict()
api_pair_dict=OrderedDict()
# 分割JSON对象
objects = content.strip().split('\n')
for obj in objects:
    temp = json.loads(obj)
    mashup_api_dict[temp['Name']]=temp['Related APIs']
    