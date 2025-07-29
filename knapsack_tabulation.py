def knapsack(wt, prof, W, n):
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]   
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if wt[i - 1] <= j:
                dp[i][j] = max(prof[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][W]

wt = [3, 4, 6, 5]
prof = [2, 3, 1, 4]
W = 8
n = len(wt)

print(knapsack(wt, prof, W, n))
