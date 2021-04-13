

# s = "11121"
# # print(s)
# n = len(s)
# res = 0

# cnt = 1
# for i in range(1, n):
#     if s[i] != s[i-1]:
#         res += (1+cnt)*cnt//2
#         cnt = 1
#     else:
#         cnt += 1

# res += (1+cnt)*cnt//2
# print(res)


# maxv = 6
# res = [[5], [4,1], [2,4]]
# print(maxv)
# for li in res:
#     print(li, end="")
# print("\n", end="")

n = 3
values = [5, 4, 1 ,2 ,4]

res = float("inf")
resli = []

length = len(values)
path = [0]
def dfs(i, dep):
    global res, resli
    if dep == n:
        path.append(length)
        # print(path)
        li = []
        for x in range(n):
            li.append(sum(values[path[x]:path[x+1]]))
        maxv = max(li)
        if maxv < res:
            res = maxv
            li = []
            for x in range(n):
                li.append(values[path[x]: path[x+1]])
            resli = li[:]

        path.pop()
        return
    for j in range(i, length-(n-dep)):
        path.append(j+1)
        dfs(j+1, dep+1)
        path.pop()

dfs(0, 1)
print(res)
# print(resli)
for li in resli:
    print(li, end="")
print("\n", end="")