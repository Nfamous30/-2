
import json


edge_map = dict()



result_pairs_dict = dict()
result_nodes_dict = dict()
weight_isnot_zero = 0
with open("../data/new/pairs_result.txt", "r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        temp_list = line.split(' ')

        if temp_list[2] != 0:
            weight_isnot_zero = weight_isnot_zero + 1

        # BA 判断key，如果不存在，就按照AB key存到map中
        str_ba = temp_list[1] + "&" + temp_list[0]
        if str_ba not in result_pairs_dict:
            str_ab = temp_list[0] + "&" + temp_list[1]
            result_pairs_dict[str_ab] = int(temp_list[2])

            # 统计节点出现频率
            for i in (0, 1):
                preValue = 0
                if temp_list[i] in result_nodes_dict:
                    preValue = result_nodes_dict[temp_list[i]]

                result_nodes_dict[temp_list[i]] = int(temp_list[2]) + preValue

# 通过行数 校验最终结果
print(weight_isnot_zero)
print(len(result_pairs_dict))
print(len(result_nodes_dict))

with open('../data/new/pairs_result1.txt','a',encoding='utf-8') as f:
    f.write(json.dumps(result_pairs_dict, ensure_ascii=False)+'\n')

with open('../data/new/nodes_result1.txt','a',encoding='utf-8') as f:
    f.write(json.dumps(result_nodes_dict, ensure_ascii=False)+'\n')