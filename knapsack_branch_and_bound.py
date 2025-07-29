def k(i,capcity,val,wt,memo):
    if i == len(val):
        return 0
    if memo[i][capcity] != -1:
        return memo[i][capcity]
    take = 0
    if wt[i] <= capcity:
        take = val[i] + k(i,capcity-wt[i],val,wt,memo)
    noTake = k(i+1,capcity,val,wt,memo)
    memo[i][capcity] = max(take,noTake)
    return memo[i][capcity]

def k2(capcity,val,wt):
    memo = [[-1 for i in range(capcity+1)]for j in range(len(val))]
    return k(0,capcity,val,wt,memo)

val = [1,1]
wt = [2,1]
capcity = 3
print(k2(capcity,val,wt))
