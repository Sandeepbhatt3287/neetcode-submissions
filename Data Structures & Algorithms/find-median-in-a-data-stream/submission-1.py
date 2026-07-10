class MedianFinder:

    def __init__(self):
        self.median =[]

    def addNum(self, num: int) -> None:
        self.median.append(num)
        

    def findMedian(self) -> float:
        n = len(self.median)
        self.median.sort()

        
        if n%2:
            return self.median[n // 2]
        else:
            return (self.median[n // 2] + self.median[n // 2 - 1]) / 2


        
        