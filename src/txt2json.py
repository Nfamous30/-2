import json

# with open("../data/edge/边节点顺序排列.txt", "r",encoding='utf-8') as load_f:
#     edge_list = json.load(load_f)
# with open('../data/edge/edge_list.json','a',encoding='utf-8') as f:
#     json.dump(edge_list, f)

# with open("../data/edge/apis调用次数.txt", "r",encoding='utf-8') as load_f:
#     api_use_list = json.load(load_f)
# with open('../data/edge/api_use.json','a',encoding='utf-8') as f:
#     json.dump(api_use_list, f)

with open("../data/edge/api组合次数.txt", "r",encoding='utf-8') as load_f:
    api_con_list = json.load(load_f)
with open('../data/edge/api_con.json','a',encoding='utf-8') as f:
    json.dump(api_con_list, f)

with open("../data/edge/apis的Tags.txt", "r",encoding='utf-8') as load_f:
    category_dict_list = json.load(load_f)
with open('../data/edge/category_dict.json','a',encoding='utf-8') as f:
    json.dump(category_dict_list, f)

with open("../data/edge/边节点顺序对应tag.txt", "r",encoding='utf-8') as load_f:
    api_categories_list = json.load(load_f)
with open('../data/edge/api_categories.json','a',encoding='utf-8') as f:
    json.dump(api_categories_list, f)