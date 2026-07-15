nums=[2,1,1,5,6,2,3,1]
def mountain_memo(nums):
        n=len(nums)
        dp_lis=[[None for _ in range(n)] for __ in range(n)]
        dp_lds=[[None for _ in range(n)] for __ in range(n)]

        def lis(ind,prev_ind):
            if ind==-1:
                return 0
            if dp_lis[ind][prev_ind]!=None:   
                return dp_lis[ind][prev_ind]
            
            pick=0
            if nums[prev_ind]>nums[ind]:
                pick=1+lis(ind-1,ind)
            not_pick=lis(ind-1,prev_ind)

            dp_lis[ind][prev_ind]=max(pick,not_pick)
            return dp_lis[ind][prev_ind]
        
        def lds(ind,prev_ind):
            if ind==n:
                return 0
            if dp_lds[ind][prev_ind]!=None:
                return dp_lds[ind][prev_ind]
            pick=0
            if nums[ind]<nums[prev_ind]:
                pick=1+lds(ind+1,ind)
            not_pick=lds(ind+1,prev_ind)

            dp_lds[ind][prev_ind]=max(pick,not_pick)
            return dp_lds[ind][prev_ind]

        
        maxi=0
        for i in range(n):
            inc=lis(i-1,i)
            if inc==0:
                continue
            dec=lds(i+1,i)
            if dec==0:
                continue
            maxi=max(maxi,inc+dec+1)
        return n-maxi

print(mountain_memo(nums))


def mountain_tabu(nums):
    n=len(nums)

    