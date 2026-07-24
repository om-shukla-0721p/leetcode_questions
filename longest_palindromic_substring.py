s = "babad"

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
        if q-p+1>len(ans):
            ans=s[p:q]
        p,q=expand(i,i+1)
        if q-p+1>len(ans):
            ans=s[p:q]
    return ans

print(lp_expand(s))

