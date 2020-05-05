
#https://leetcode.com/problems/maximal-square/

dp = [[0]* (len(matrix)+2) for _ in range(len(matrix[0])+1)]
best = 0
for i in range(1, len(matrix)+1):
    for y in range(1, len(matrix[0])+1):
        if matrix[i-1][y-1] == "1":
            dp[i][y] = min(dp[i-1][y], dp[i-1][y-1], dp[i][y-1]) + 1
            print(dp)
    best = max(best, dp[i][y])

print(best)
