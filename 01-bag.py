
W = 4
N = 3
wt = [2, 1, 3]
val = [4, 2, 3]

def f(bagW, Nthing, values, weights):
    dp = [[0]*(bagW+1) for _ in range(Nthing+1) ]
    for i in range(1, Nthing+1): # 注意这里是从1-N，后面i需要向左移一位
        for j in range(1, bagW+1):
            tmp = j - weights[i-1] # 装了第i个物品后，背包的容量
            if tmp < 0: # 即装不下
                dp[i][j] = dp[i-1][j] # 不装第i个物品
            else: # 能装下第i个物品
                dp[i][j] = max(
                    dp[i-1][j], 
                    dp[i-1][tmp] + values[i-1]
                ) 
                # dp[i-1][j]为不装第i个，values[i-1]为第i个物品的重量
                # dp[i-1][tmp] 为装第i个之前的背包重量装从前i-1里的最优值
    return dp[Nthing][bagW]

res = f(W, N, val, wt)

print(res)




