class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # i ma thinging make two pointer and swap the values

        # left = 0 
        # right = len(nums) -1
        # k=0

        # while left <= right:

        #     if nums[left] == val:
        #         k+=1
        #         if nums[right] != val:
        #             nums[left],nums[right] = nums[right] , nums[left]
        #             left+=1
        #             right -=1
        #         else:
        #             right -=1
        #             nums[left],nums[right] = nums[right] , nums[left]
        #             left +=1
        #     else:
        #         left +=1
        
        # return k

        left = 0
        k = len(nums) - 1

        while left <= k:
            if nums[left] == val:
                nums[left] = nums[k]
                k -= 1
            else:
                left += 1
                
        return k + 1
