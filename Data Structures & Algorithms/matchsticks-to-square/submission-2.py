class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:

        total = sum(matchsticks)

        # the four sides have to come out even
        if total % 4 != 0:
            return False

        target = total // 4

        # largest first, so dead ends surface near the top of the tree
        matchsticks.sort(reverse=True)

        # one oversized stick can never fit on any side
        if matchsticks[0] > target:
            return False

        sides = [0] * 4

        def dfs(i: int) -> bool:
            # every stick placed, and nothing ever overflowed
            if i == len(matchsticks):
                return True

            for side in range(4):
                # equal sides are interchangeable, so trying both wastes a branch
                if side > 0 and sides[side] == sides[side - 1]:
                    continue

                if sides[side] + matchsticks[i] > target:
                    continue

                sides[side] += matchsticks[i]
                if dfs(i + 1):
                    return True
                sides[side] -= matchsticks[i]

                # this stick must go somewhere, and an empty side is the most
                # forgiving place it will ever get, so nothing can work
                if sides[side] == 0:
                    break

            return False

        return dfs(0)