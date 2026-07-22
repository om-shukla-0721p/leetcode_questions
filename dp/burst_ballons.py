nums=[3,1,5,8]

def coins_recur(nums):
    nums=[1]+nums+[1]
    
    def solve(i,j):
        if j-i==1:
            return 0
        
        coins=float("-inf")
        for k in range(i+1,j):
            coins=max(coins,solve(i,k)+solve(k,j)+nums[i]*nums[k]*nums[j])
        return coins
    return solve(0,len(nums)-1)

print(coins_recur(nums))

def coins_memo(nums):
    nums=[1]+nums+[1]
    n=len(nums)
    dp=[[None for _ in range(n)] for __ in range(n)]

    def solve(i,j):
        if j-i==1:
            return 0
        if dp[i][j]!=None:
            return dp[i][j]
        
        coins=float("-inf")
        for k in range(i+1,j):
            coins=max(coins,solve(i,k)+solve(k,j)+nums[i]*nums[k]*nums[j])
        dp[i][j]=coins
        return dp[i][j]
    return solve(0,n-1)

print(coins_memo(nums))


def coins_tabu(nums):
    nums=[1]+nums+[1]
    n=len(nums)
    dp=[[0 for _ in range(n)] for __ in range(n)]

    for i in range(n-1,-1,-1):
        for j in range(i+2,n):
            coins=float("-inf")
            for k in range(i+1,j):
                coins=max(coins,dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
            dp[i][j]=coins
    return dp[0][n-1]


print(coins_tabu(nums))