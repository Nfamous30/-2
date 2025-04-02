import json 

with open('../data/new/api_categories.json','r',encoding='utf-8') as load_f:
    category_dict_list = json.load(load_f)

category_dict=set()
for edge in category_dict_list:
    cat_list = edge
    for cat in cat_list:
        category_dict.add(cat)

print(len(category_dict))
category_lsit = list(category_dict)

with open('../data/new/category_list.json','w',encoding='utf-8') as f:
    json.dump(category_lsit, f)