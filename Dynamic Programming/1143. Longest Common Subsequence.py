#https://leetcode.com/problems/longest-common-subsequence/

seen = [[False]*len(text2) for _ in range(len(text1))]
dp = [[0] * len(text2) for _ in range(len(text1))]
def LCS(i, j):
    if i==len(text1)or j==len(text2):
        return 0
    if seen[i][j]:
        return dp[i][j]

    best = 0
    if text1[i]==text2[j]:
        m =  1 + LCS(i+1, j+1)
        best = max(best, m)

    score = LCS(i+1, j)
    best = max(best, score)
    score = LCS(i, j+1)
    best = max(best, score)

    seen[i][j] = True
    dp[i][j] = best
    return best


print(LCS(0, 0))
