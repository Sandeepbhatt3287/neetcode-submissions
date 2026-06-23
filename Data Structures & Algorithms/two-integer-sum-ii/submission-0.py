class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers) -1

        left = 0

        while left<n:
            sum = numbers[left] + numbers[n]
            if sum == target:
                return [left+1,n+1]

            elif sum < target:
                left +=1

            else:
                n -=1 

        