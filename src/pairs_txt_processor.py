import json

edge_map = dict()

# with open("all_pairs_temp.txt", "r") as f:
#     for line in f.readlines():
#         line = line.strip('\n')  #去掉列表中每一个元素的换行符
#         line = line.replace('\'','').replace(' ','').replace('(','').replace(')','')
#         line_list = line.split(',')
#         # print(line.split(','))

#         node1 = line_list[0]
#         node2 = line_list[1]
#         weight = line_list[3]
#         line_result = node1 + " " + node2 + " " + weight
#         with open('./pairs_result.txt','a',encoding='utf-8') as f:
#             f.write(line_result +'\n')

#         #print("{}+{}:{}".format(node1, node2, weight))

with open("../data/new/category_dict.json", "r",encoding='utf-8') as load_f:
    api_tags_dict = json.load(load_f)

result_pairs_dict = dict()
weight_isnot_zero = 0
count_notag_node = 0
with open("../data/edge/all_pairs【提取api组合次数】.txt", "r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        temp_list = line.split(' ')

        # 过滤 权重 = 0
        if int(temp_list[2]) == 0:
            continue

        # 保证边的节点 肯定有关键词
        if temp_list[0] not in api_tags_dict or temp_list[1] not in api_tags_dict:
            # print(temp_list)
            count_notag_node = count_notag_node + 1
            continue

        # if temp_list[2] != 0:
        #     weight_isnot_zero = weight_isnot_zero + 1

        # BA 判断key，如果不存在，就按照AB key存到map中 (字母序排序)
        if (temp_list[0] > temp_list[1]):
            tmp = temp_list[1]
            temp_list[1] = temp_list[0]
            temp_list[0] = tmp

        # str_ba = temp_list[1] + "&" + temp_list[0]
        str_ab = temp_list[0] + "&" + temp_list[1]
        if str_ab not in result_pairs_dict and int(temp_list[2]) > 0:
            result_pairs_dict[str_ab] = int(temp_list[2])


# 通过行数 校验最终结果
print(count_notag_node)
print(len(result_pairs_dict))

with open('../data/new/pairs_result.txt','a',encoding='utf-8') as f:
    f.write(json.dumps(result_pairs_dict, ensure_ascii=False)+'\n')
