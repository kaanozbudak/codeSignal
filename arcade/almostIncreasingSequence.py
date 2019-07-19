# Created by kaanozbudak at 2019-07-18 

# Given a sequence of integers as an array, determine whether it is possible to
# obtain a strictly increasing sequence by removing no more than one element from the array.
# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an.
# Sequence containing only one element is also considered to be strictly increasing.


sequence = [1, 3, 2, 1]


def almostIncreasingSequence(sequence):
    invalidItemsCount = 0;

    for i in range(len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            invalidItemsCount += 1
            if invalidItemsCount > 1:
                return False
        if sequence[i] <= sequence[i - 2] or sequence[i + 1] <= sequence[i - 1]:
            return True
    return True


print(almostIncreasingSequence(sequence))
