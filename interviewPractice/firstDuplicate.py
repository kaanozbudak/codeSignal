# Created by kaanozbudak at 2019-07-19 
# Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number
# for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers,
# return the number for which the second occurrence has a smaller index than the second occurrence of the other number does.
# If there are no such elements, return -1.

a = [2, 1, 3, 5, 3, 2]


def firstDuplicate(a):
    temp=set()
    for i in a:
        if i in temp:
            return i
        temp.add(i)
    return -1



firstDuplicate(a)