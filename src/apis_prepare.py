import json

with open("./deadpool_apis_data.txt",'r') as load_f:
    dead_json_arr = json.load(load_f)

with open("./active_apis_data.txt",'r') as load_file:
    active_json_arr = json.load(load_file)

url_tags_map = dict()
apiCount = 0
for j in dead_json_arr:
    if j is not None:
        temp_url = j['url'].replace('\n', '')
        apiCount += 1
        url_tags_map[temp_url] = j['tags']

for j in active_json_arr:
    if j is not None:
        temp_url = j['url'].replace('\n', '')
        apiCount += 1
        url_tags_map[temp_url] = j['tags']

print(apiCount)


# for url, tags in url_tags_map.items():
#     print("{} ^^ {}".format(url, tags))

with open('./apis_result.txt','a',encoding='utf-8') as f:
    f.write(json.dumps(url_tags_map, ensure_ascii=False)+'\n')

# with open("./apis_result.txt",'r') as load_f1:
#     map_json = json.load(load_f1)

# print(map_json)