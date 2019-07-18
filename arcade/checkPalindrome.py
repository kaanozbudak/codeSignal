
# Created by kaanozbudak at 2019-07-18

inputString = "aabaa"

def checkPalindrome(inputString):
    return inputString == inputString[::-1]



print(checkPalindrome(inputString))