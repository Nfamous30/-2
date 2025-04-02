import json

# 读取输入输出数据文件并将其转换为python对象
with open('input_data.json') as f:
    input_data = json.load(f)
    
with open('output_data.json') as f:
    output_data = json.load(f)
    
# 将输入输出数据按照需要的格式存储在字典中
apis = {
    'api1': {
        'input': input_data[0],
        'output': output_data[0]
    },
    'api2': {
        'input': input_data[1],
        'output': output_data[1]
    },
    # ...
}



# 计算每对api之间的接口兼容性
for api1 in apis:
    for api2 in apis:
        if api1 != api2:
            # 计算输入数据之间的相似度
            input_set1 = set(apis[api1]['input'])
            input_set2 = set(apis[api2]['input'])
            jaccard_input = len(input_set1.intersection(input_set2)) / len(input_set1.union(input_set2))
            # 计算输出数据之间的相似度
            output_set1 = set(apis[api1]['output'])
            output_set2 = set(apis[api2]['output'])
            jaccard_output = len(output_set1.intersection(output_set2)) / len(output_set1.union(output_set2))
            # 输出结果
            print(f'{api1} and {api2}: input similarity = {jaccard_input:.2f}, output similarity = {jaccard_output:.2f}')
