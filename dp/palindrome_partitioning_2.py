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


# without only 1 variable but without precomputation of is_pal
def cut_recur_better(s):
    n=len(s)
    def is_palindrome(l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    def solve(i):
        if i==n:
            return -1
        
        cost=float("inf")
        for j in range(i,n):
            if is_palindrome(i,j) is True:
                cost=min(cost,solve(j+1)+1)
        return cost
    return solve(0)

print(cut_recur_better(s))
    
def cut_memo_better(s):
    n=len(s)
    dp=[None for __ in range(n)]

    def is_palindrome(l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    
    def solve(i):
        if i==n:
            return -1
        if dp[i]!=None:
            return dp[i]
        
        cost=float("inf")
        for j in range(i,n):
            if is_palindrome(i,j):
                cost=min(cost,solve(j+1)+1)
        dp[i]=cost
        return dp[i]
    
    return solve(0)

print(cut_memo_better(s))

def cut_tabu_better(s):
    n=len(s)
    dp=[-1 for _ in range(n+1)]

    def is_palindrome(l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    for i in range(n-1,-1,-1):
        cost=float("inf")
        for j in range(i,n):
            if is_palindrome(i,j) is True:
                cost=min(cost,dp[j+1]+1)
        dp[i]=cost
    return dp[0]

print(cut_tabu_better(s))

def cut_best(s):
    n=len(s)
    is_palindorme=[[False for _ in range(n)] for __ in range(n)]
    # loops for precomputing the palindrome pairs
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if s[i]==s[j]:
                if j-i<=2 or is_palindorme[i+1][j-1]==True:
                    is_palindorme[i][j]=True

    # making dp
    dp=[0 for _ in range(n+1)]
    dp[n]=-1 # base condition

    # taking the best possible pair of palindormes possible
    for i in range(n-1,-1,-1):
        cost=float("inf")
        for j in range(i,n):
            if is_palindorme[i][j]==True:
                cost=min(cost,dp[j+1]+1)
        dp[i]=cost

    return dp[0]


print(cut_best(s))

    

