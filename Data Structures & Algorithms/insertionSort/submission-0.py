# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []

        for i in range(0,n):
            for j in range(i,0,-1):
                if pairs[j-1].key > pairs[j].key:
                    pairs[j-1],pairs[j] = pairs[j],pairs[j-1]
                else:
                    break
            
            res.append(pairs[:])


        return res
        