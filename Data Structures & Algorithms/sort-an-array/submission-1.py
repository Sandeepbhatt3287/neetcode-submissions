class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    
        if len(nums)<=1:
            return nums


        mid = len(nums)//2

        lefthalf= nums[:mid]
        righalf = nums[mid:]


        sortedLeft = self.sortArray(lefthalf)
        sortedright =self.sortArray(righalf)

        return  self.merge(sortedLeft, sortedright)   
    def merge(self,left, right):
        res = []
        i =j =0

        while i<len(left) and j< len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        
        res.extend(left[i:])
        res.extend(right[j:])

        return res

        
