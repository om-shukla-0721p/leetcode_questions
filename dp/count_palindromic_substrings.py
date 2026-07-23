s="ababc"

def count_recur(s):
    n=len(s)
    def is_palindrome(l,r):
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    total=0
    for i in range(n):
        for j in range(i,n):
            if is_palindrome(i,j):
                total+=1
    return total

print(count_recur(s))

def count_memo(s):
    n=len(s)
    dp=[[None for _ in range(n)] for _ in range(n)]
    def is_palindrome(l,r):
        if dp[l][r]!=None:
            return dp[l][r]
        i,j=l,r
        while i<=j:
            if s[i]!=s[j]:
                dp[l][r]=False
                return False
            i+=1
            j-=1
        dp[l][r]=True
        return True
    total=0
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if is_palindrome(i,j) is True:
                total+=1
    return total

print(count_memo(s))

def count_tabu(s):
    n=len(s)
    dp=[[0 for _ in range(n)] for __ in range(n)]

    total=0
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if s[i]==s[j]:
                if j-i<=2 or dp[i+1][j-1]==1:
                    dp[i][j]=1
                    total+=1
    return total

print(count_tabu(s))