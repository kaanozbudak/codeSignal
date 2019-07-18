# Created by kaanozbudak at 2019-07-18

# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

inputArray = [3, 6, -2, -5, 7, 3]


def adjacentElementsProduct(inputArray):
    return max([inputArray[i] * inputArray[i + 1] for i in range(len(inputArray) - 1)])


print(adjacentElementsProduct(inputArray))
