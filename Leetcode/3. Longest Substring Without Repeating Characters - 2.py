
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
l, r, m = 0, 0, 0
seen = []
while r<len(s):
    if s[r] in seen:
        l += 1
        seen.pop(0)
    else:
        seen.append(s[r])
        r+=1
    m = max(m , r-l)


print(m)
