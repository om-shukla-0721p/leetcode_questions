s=["a","b","ab","cab","cdab","cabdae"]


def lsc_recur(words):
    n=len(words)    
    words.sort(key=len)

    def solve(ind,prev_ind):
        if ind==n:
            return 0
        pick=0
        if prev_ind==-1:
            pick=1+solve(ind+1,ind)
        elif len(words[ind])==len(words[prev_ind])+1:
            check=""
            length=len(words[ind])
            for i in range(length):
                check=words[ind][:i]+words[ind][i+1:]
                if check==words[prev_ind]:
                    pick=1+solve(ind+1,ind)
                    break
        
        not_pick=solve(ind+1,prev_ind)

        return max(pick,not_pick)
    return solve(0,-1)

print(lsc_recur(s))


# memoization

def lsc_memo(words):
    words.sort(key=len)
    n=len(words)

    dp=[[None for _ in range(n+1)] for __ in range(n)]

    def solve(ind,prev_ind):
        if ind==n:
            return 0
        if dp[ind][prev_ind+1]!=None:
            return dp[ind][prev_ind+1]
        
        pick=0
        if prev_ind==-1:
            pick=1+solve(ind+1,ind)
        elif len(words[ind])==len(words[prev_ind])+1:
            length=len(words[ind])
            check=""
            for i in range(length):
                check=words[ind][:i]+words[ind][i+1:]
                if check==words[prev_ind]:
                    pick=1+solve(ind+1,ind)
                    break
        not_pick=solve(ind+1,prev_ind)
        dp[ind][prev_ind+1]=max(pick,not_pick)
        return dp[ind][prev_ind+1]
    return solve(0,-1)

print(lsc_memo(s))


# tabulation
