class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k !=0:
            return False
        
        total = sum(nums)


        #  idea 
        #  if we are taking the value then we pop that value also, for next iteration

        nums.sort()

        target = total//k

        used = [False] * len(nums)

        def back(i,k,subsetSum):
            if k ==0:
                return True
            
            if subsetSum == target:
                return back(0,k-1,0)
            
            for j in range(i,len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                
                used[j] = True

                if back(j+1,k,subsetSum + nums[j]):
                    return True
                used[j]= False
        
        return back(0,k,0)