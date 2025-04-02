# 定义一个空的集合，用于存储所有的 API
all_apis = set()
# 定义一个空的字典，用于存储 API 组合次数的分布
pair_count = {}

# 打开文本文件并读取数据
with open('../data/api_mashup/all_pairs.txt', 'r',encoding='utf-8') as f:
    for line in f:
        # 将当前行数据解析为元组
        data = eval(line.strip())
        # 将 API 加入到集合中
        if int(data[3])>0:
            all_apis.add(data[0].split('/')[-1])
            all_apis.add(data[1].split('/')[-1])
            # 统计 API 组合次数的分布
            pair_count[(data[0], data[1])] = data[3]
print(len(all_apis))
# 输出所有的 API
# print("All APIs: ", all_apis)

# # 输出 API 组合次数的分布
# print("Pair Count Distribution:")
# for pair, count in sorted(pair_count.items(), key=lambda x: x[1], reverse=True):
#     print(pair, count)
