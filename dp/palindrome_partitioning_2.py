# my way solved this way on my own
s = "aab"

def cut_recur(s):
    n=len(s)
    def check_pelindrome(arr):
        mid=(len(arr))//2
        for k in range(mid):
            if arr[k]!=arr[len(arr)-k-1]:
                return False
        return True
            

    def solve(i,j):
        if check_pelindrome(s[i:j+1]) is True:
            return 0
        cost=float("inf")
        for k in range(i,j):
            cost=min(cost,solve(i,k)+solve(k+1,j)+1)
        
        return cost
    
    return solve(0,n-1)

print(cut_recur(s))

def cut_memo(s):
    n=len(s)
    dp=[[None for _ in range(n)] for _ in range(n)]

    def is_pelindrome(arr):
        mid=len(arr)//2
        for k in range(mid):
            if arr[k]!=arr[len(arr)-1-k]:
                return False
        return True
    
    def solve(i,j):
        if is_pelindrome(s[i:j+1]):
            return 0
        if dp[i][j]!=None:
            return dp[i][j]

        cost=float("inf")
        for k in range(i,j):
            cost=min(cost,solve(i,k)+solve(k+1,j)+1)
        dp[i][j]=cost
        return dp[i][j]
    return solve(0,n-1)

print(cut_memo(s))


def cut_tabu(s):
    n=len(s) 
    dp=[[0 for _ in range(n)] for __ in range(n)]

    def is_pelindrome(arr):
        mid=len(arr)//2
        for k in range(mid):
            if arr[k]!=arr[len(arr)-1-k]:
                return False
        return True
    
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if is_pelindrome(s[i:j+1]):
                dp[i][j]=0
                continue
            cost=float("inf")
            for k in range(i,j):
                cost=min(cost,dp[i][k]+dp[k+1][j]+1)
            dp[i][j]=cost
    return dp[0][n-1]

print(cut_tabu(s))