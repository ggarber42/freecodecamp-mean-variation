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
    mean = matrix.mean()
    axis0_var = formatter(matrix.var(0))
    axis1_var = formatter(matrix.var(1))
    var = matrix.var()
    axis0_std = formatter(matrix.std(0))
    axis1_std = formatter(matrix.std(1))
    std = matrix.std()
    axis0_max = formatter(matrix.max(0))
    axis1_max = formatter(matrix.max(1))
    max_value = matrix.max()
    axis0_min = formatter(matrix.min(0))
    axis1_min = formatter(matrix.min(1))
    min_value = matrix.min()
    axis0_sum = formatter(matrix.sum(0))
    axis1_sum = formatter(matrix.sum(1))
    sum_value = matrix.sum()
    return {
      'mean': [axis1_mean, axis0_mean, mean],
      'variance': [axis1_var, axis0_var, var],
      'standard deviation': [axis1_std, axis0_std , std],
      'max': [axis1_max, axis0_max, max_value ],
      'min': [axis1_min, axis0_min, min_value],
      'sum': [axis1_sum , axis0_sum, sum_value ]
    }

# print(calculate([0,1,2,3,4,5,6,7,8]))
print(calculate([2,6,2,8,4,0,1,5,7]))