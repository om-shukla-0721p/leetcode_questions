# matrix multiplication is associative for multiplication thats why we can 
# go from in to out or out to in
# but cost does change with differnt order

arr=[1,2,3,4,3]

#output=30

def mcm_recur(arr):
    n=len(arr)

    def solve(i,j):
        if i==j:
            return 0
        cost=float("inf")
        for k in range(i,j):
            cost=min(cost,solve(i,k)+solve(k+1,j)+arr[i-1]*arr[k]*arr[j])
        return cost

    return solve(1,n-1)

print(mcm_recur(arr))


# memoization

def mcm_memo(arr):
    n=len(arr)
    dp=[[None for _ in range(n)] for __ in range(n)]

    def solve(i,j):
        if i==j:
            return 0
        if dp[i][j]!=None:
            return dp[i][j]
        cost=float("inf")
        for k in range(i,j):
            cost=min(cost,solve(i,k)+solve(k+1,j)+arr[i-1]*arr[k]*arr[j])
        
        dp[i][j]=cost
        return dp[i][j]
    
    return solve(1,n-1)

print(mcm_memo(arr))



