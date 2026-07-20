n = 7
cuts = [1,3,4,5]
def cost_recur(n,cuts):
        m=len(cuts)
        cuts.sort()
        def solve(i,j):
            if i==j:
                return 0
            cost=float("inf")
            for k in cuts:
                if k<=i:
                    continue
                if k>=j:
                    break
                cost=min(cost,solve(i,k)+solve(k,j)+j-i)
            if cost==float("inf"):
                return 0
            return cost
        return solve(0,n)
    
def cost_memo(n,cuts):
    cuts.sort()
    dp=[[None for _ in range(n+1)] for __ in range(n+1)]

    def solve(i,j):
        if i==j or j-i==1:# no cuts possible
            return 0
        if dp[i][j]!=None:
            return dp[i][j]
        cost=float("inf")
        for k in cuts:
            if i>=k:
                continue
            if j<=k:
                break
            cost=min(cost,solve(i,k)+solve(k,j)+j-i)
        if cost==float("inf"):
            dp[i][j]=0
        else:
            dp[i][j]=cost
        return dp[i][j]
    return solve(0,n)

def cost_tabu(n,cuts):
    cuts.sort()
    dp=[[0 for _ in range(n+1)] for __ in range(n+1)]

    for i in range(n,-1,-1):
        for j in range(i+2,n+1):
            cost=float("inf")
            for k in cuts:
                if k<=i:
                    continue
                if k>=j:
                    break
                cost=min(cost,dp[i][k]+dp[k][j]+j-i)
            if cost==float("inf"):
                dp[i][j]=0
            else:
                dp[i][j]=cost
    return dp[0][n]
            
print(cost_recur(n,cuts))
print(cost_memo(n,cuts))
print(cost_tabu(n,cuts))


# pattern recognition
# in this we are looping only on the cuts
# 
def min_cost_recur(n,cuts):
    cuts.sort()
    cuts=[0]+cuts+[n]
    def solve(i,j):
        if j-i==1:
            return 0
        cost=float("inf")
        for k in range(i+1,j):
            cost=min(cost,solve(i,k)+solve(k,j)+cuts[j]-cuts[i])
        return cost
    return solve(0,len(cuts)-1)

print(min_cost_recur(n,cuts))


# memoization

def min_cost_memo(n,cuts):
    cuts.sort()
    cuts=[0]+cuts+[n]

    dp=[[None for _ in range(len(cuts))] for __ in range(len(cuts))]

    def solve(i,j):
        if j-i==1:
            return 0
        if dp[i][j]!=None:
            return dp[i][j]
        cost=float("inf")
        for k in range(i+1,j):
            cost=min(cost,solve(i,k)+solve(k,j)+cuts[j]-cuts[i])
        dp[i][j]=cost
        return dp[i][j]
    return solve(0,len(cuts)-1)

print(min_cost_memo(n,cuts))

    