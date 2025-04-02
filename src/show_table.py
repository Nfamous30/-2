import json
import numpy as np

# 假设你的矩阵存储在一个列表中，例如：
with open('../data/new/edge_list.json', 'r',encoding = 'utf-8') as f:
    edge = json.load(f)
edge_list = []
for ed in edge:
    edge_list.append(ed)



def top_jaccard(name='jaccard'):
   
    print("res3_jaccard_matrix")
    with open('../data/res3/jaccard.json', 'r',encoding = 'utf-8') as f:
        res = json.load(f)
    for api in res:
        print(api['name'],api['score'])
# top_jaccard()

def top_tf_idf(name='tf-idf'):
    print("res3_tf_idf_matrix")
    
    with open('../data/res3/tf-idf.json', 'r',encoding = 'utf-8') as f:
        res = json.load(f)
    for api in res:
        print(api['name'],api['score'])

def top_values(edge_list, num_list, num_top=10, name = "matrix"):
    """
    输出 num_list 中前 num_top 个最大值所对应的 edge_list 中的字符串和对应的数值。

    参数：
        - edge_list：字符串列表，每个字符串表示一个节点。
        - num_list：数值列表，每个数值表示一个节点的重要性。
        - num_top：整数，表示要输出的前 num_top 个最大值。默认值为 10。

    返回值：
        无返回值。直接在控制台中输出结果。
    """
    # 将 num_list 转换成 NumPy 数组形式
    num_list = np.array(num_list)

    # 获取 num_list 元素从小到大的排序下标索引，并将排序下标索引倒序切片取前 num_top 个
    num_list_sorted_indices = np.argsort(num_list)[::-1][:num_top]
    print(name)
    # 输出前 num_top 个数字对应下标在 edge_list 中的对应字符串和对应的数值
    for i in range(len(num_list_sorted_indices)):
        index = num_list_sorted_indices[i]
        print(edge_list[index], num_list[index])


chose_num = 1105  #youtube
# chose_num = 968  #ytwitter





# with open('../data/res3/cn_matrix.json', 'r',encoding = 'utf-8') as f1:
#     data1 = json.load(f1)
# # 将json解析后转换为list格式
# matrix_list1 = []
# for row in data1:
#     matrix_list1.append(list(row))
# top_values(edge_list,matrix_list1[chose_num],name="res3_cn_matrix")

# with open('../data/res3/follower_matrix.json', 'r',encoding = 'utf-8') as f1:
#     data1 = json.load(f1)
# # 将json解析后转换为list格式
# matrix_list1 = []
# for row in data1:
#     matrix_list1.append(list(row))
# top_values(edge_list,matrix_list1[chose_num],name="res3_follower_matrix")

# with open('../data/res3/company_matrix.json', 'r',encoding = 'utf-8') as f1:
#     data1 = json.load(f1)
# # 将json解析后转换为list格式
# matrix_list1 = []
# for row in data1:
#     matrix_list1.append(list(row))
# top_values(edge_list,matrix_list1[chose_num],name="res3_company_matrix")

# with open('../data/res1/interface_matrix.json', 'r',encoding = 'utf-8') as f2:
#     data2 = json.load(f2)
# # 将json解析后转换为list格式
# matrix_list2 = []
# for row in data2:
#     matrix_list2.append(list(row))
# top_values(edge_list,matrix_list2[chose_num],name="interface_matrix")

# with open('../data/res1/tf_idf_matrix.json', 'r',encoding = 'utf-8') as f3:
#     data3 = json.load(f3)
# # 将json解析后转换为list格式
# matrix_list3 = []
# for row in data3:
#     matrix_list3.append(list(row))
# top_values(edge_list,matrix_list3[chose_num],name="tf_idf_matrix")

# with open('../data/res3/company_matrix.json', 'r',encoding = 'utf-8') as f1:
#     data1 = json.load(f1)
# # 将json解析后转换为list格式
# matrix_list1 = []
# for row in data1:
#     matrix_list1.append(list(row))
# top_values(edge_list,matrix_list1[chose_num],name="res3_company_matrix")

# with open('../data/res3/weight_matrix.json', 'r',encoding = 'utf-8') as f1:
#     data1 = json.load(f1)
# # 将json解析后转换为list格式
# matrix_list1 = []
# top_jaccard('jaccard')

# with open('../data/res3/tag_tf_idf_matrix.json', 'r',encoding = 'utf-8') as f1:
#     data1 = json.load(f1)
# # 将json解析后转换为list格式
# matrix_list1 = []
# top_tf_idf('tf-idf')

# with open('../data/res1/weight_matrix.json', 'r',encoding = 'utf-8') as f1:
#     data1 = json.load(f1)
# # 将json解析后转换为list格式
# matrix_list1 = []
# for row in data1:
#     matrix_list1.append(list(row))
# top_values(edge_list,matrix_list1[chose_num],name="weight_matrix")

# with open('../data/res1/interface_matrix.json', 'r',encoding = 'utf-8') as f2:
#     data2 = json.load(f2)
# # 将json解析后转换为list格式
# matrix_list2 = []
# for row in data2:
#     matrix_list2.append(list(row))
# top_values(edge_list,matrix_list2[chose_num],name="interface_matrix")

# with open('../data/res1/tf_idf_matrix.json', 'r',encoding = 'utf-8') as f3:
#     data3 = json.load(f3)
# # 将json解析后转换为list格式
# matrix_list3 = []
# for row in data3:
#     matrix_list3.append(list(row))
# top_values(edge_list,matrix_list3[chose_num],name="tf_idf_matrix")

# with open('../data/res1/company_matrix.json', 'r',encoding = 'utf-8') as f4:
#     data4 = json.load(f4)
# # 将json解析后转换为list格式
# matrix_list4 = []
# for row in data4:
#     matrix_list4.append(list(row))
# top_values(edge_list,matrix_list4[chose_num],name="company_matrix")

# with open('../data/res1/follower_matrix.json', 'r',encoding = 'utf-8') as f5:
#     data5 = json.load(f5)
# # 将json解析后转换为list格式
# matrix_list5 = []
# for row in data5:
#     matrix_list5.append(list(row))
# top_values(edge_list,matrix_list5[chose_num],name="follower_matrix")


# with open('../data/res1/cn_matrix.json', 'r',encoding = 'utf-8') as f4:
#     data4 = json.load(f4)
# # 将json解析后转换为list格式
# matrix_list4 = []
# for row in data4:
#     matrix_list4.append(list(row))
# top_values(edge_list,matrix_list4[chose_num],num_top=20,name="cn_matrix")


