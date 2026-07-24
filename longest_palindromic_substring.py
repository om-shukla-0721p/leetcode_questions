s = "babad"

def lp_dp(s):
    n=len(s)
    dp=[[None for _ in range(n)] for __ in range(n)]

    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if s[i]==s[j]:
                if j-i<=2 or dp[i+1][j-1]==True:
                    dp[i][j]=True

    ans=""
    for i in range(n):
        for j in range(n):
            if dp[i][j]==True and (j-i+1>len(ans)):
                ans=s[i:j+1]

    return ans

print(lp_dp(s))

def lp_expand(s):
    n=len(s)

    def expand(i,j):
        while i>=0 and j<n:
            if s[i]==s[j]:
                i-=1
                j+=1
            else:
                break
        return i+1,j

    ans=""
    for i in range(n):
        p,q=expand(i,i)
        if q-p+1>len(ans): # even q-p>len(ans) would work
            ans=s[p:q]
        p,q=expand(i,i+1)
        if q-p+1>len(ans):
            ans=s[p:q]
    return ans

print(lp_expand(s))

