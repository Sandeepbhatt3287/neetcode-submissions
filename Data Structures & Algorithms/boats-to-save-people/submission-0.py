class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        

        l= 0
        r = len(people) -1
        people.sort()

        res =0

        while l<r:

            if people[r] == limit:
                res +=1
                r -=1
            elif people[l] + people[r] <= limit:
                res +=1
                l +=1
                r -=1
        if len(people)%2 ==0:
            return res
        else:
            return res+1
            