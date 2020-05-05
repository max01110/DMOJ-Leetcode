
#https://leetcode.com/problems/happy-number/

n = 19
memo = set()
def isHappy(n):
    if n==1:
        return True
    if n in memo:
        return False
    else:
        sumN = 0
        memo.add(n)
        for i in str(n):
            sumN += int(i)**2
        return isHappy(sumN)

print(isHappy(19))
