import numpy as np


def formatter(array):
    formatted_array = []
    for i in range(0,array.size):
        formatted_array.append(array.item(i-1))
    return formatted_array

def calculate(list):
    matrix = np.array([list[:3], list[3:6], list[6:]])
    axis0_mean = formatter(matrix.mean(0))
    axis1_mean = formatter(matrix.mean(1))
    mean = matrix.mean(dtype='float32')
    axis0_var = formatter(matrix.var(0))
    axis0_var = formatter(matrix.var(1))
    var = matrix.var(dtype='float32')
    axis0_std = formatter(matrix.std(0))
    axis0_std = formatter(matrix.std(1))
    std = matrix.std(dtype='float32')
    axis0_max = formatter(matrix.max(0))
    axis0_max = formatter(matrix.max(1))
    max_value = matrix.max()
    axis0_min = formatter(matrix.min(0))
    axis0_min = formatter(matrix.min(1))
    min_value = matrix.min()
    axis0_sum = formatter(matrix.sum(0))
    axis0_sum = formatter(matrix.sum(1))
    sum_value = matrix.sum()
    print(std)
    return {
      'mean': [axis0_mean, axis1_mean, mean],
    #   'variance': [np_matrix.var(0), np_matrix.var(1).transpose(), np_matrix.var()],
    #   'max': [np_matrix.max(0), np_matrix.max(1).transpose(), np_matrix.max()],
    #   'max': [np_matrix.min(0), np_matrix.min(1).transpose(), np_matrix.min()],
    #   'sum': [np_matrix.sum(0), np_matrix.sum(1).transpose(), np_matrix.sum()]
    }


print(calculate([0,1,2,3,4,5,6,7,8]))
print('hello')