import numpy as np

# 假设matrix_list是一个包含多个n*n矩阵的列表
matrix_list = [matrix1, matrix2, matrix3, ...]

# 使用numpy的sum函数对多个矩阵进行相加
sum_matrix = np.sum(matrix_list, axis=0)
