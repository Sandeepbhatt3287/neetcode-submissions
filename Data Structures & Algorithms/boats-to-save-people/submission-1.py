class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        

        low= 0
        high = len(people) -1
        people.sort()

        res =0

        while low <= high:
            # the heaviest is going on a boat regardless,
            # so try to seat the lightest alongside them
            if people[low] + people[high] <= limit:
                low += 1

            # either way the heaviest leaves on this boat
            high -= 1
            res += 1

        return res
        
            