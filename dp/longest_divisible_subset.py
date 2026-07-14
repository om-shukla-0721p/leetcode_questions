def lds_recur(nums):
        
        nums.sort()
        n=len(nums)
        if n==0:
             return []
        
        def solve(ind,prev):
            if ind==n:
                return []

            pick=[]
            if prev==-1 or nums[ind]%nums[prev]==0:
                pick=[nums[ind]]+solve(ind+1,ind)
            not_pick=solve(ind+1,prev)
            if len(pick)>=len(not_pick):
                return pick
            else:
                return not_pick
        return solve(0,-1)
nums=[1,2,3,4,5,6,7,8,]
print(lds_recur(nums))
        