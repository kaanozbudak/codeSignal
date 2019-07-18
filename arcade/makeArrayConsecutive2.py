# Created by kaanozbudak at 2019-07-18


statues = [6, 2, 3, 8]


# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
# each statue having an non-negative integer size. Since he likes to make things perfect,
# he wants to arrange them from smallest to largest so that each statue will be bigger than the
# previous one exactly by 1. He may need some additional statues to be able to accomplish that.
# Help him figure out the minimum number of additional statues needed.

def makeArrayConsecutive2(statues):
    _sortedArray = sorted(statues)
    res = []
    for x in range(_sortedArray[0], _sortedArray[-1]):
        if not x in statues:
            res.append(x)
    return len(res)


print(makeArrayConsecutive2(statues))
