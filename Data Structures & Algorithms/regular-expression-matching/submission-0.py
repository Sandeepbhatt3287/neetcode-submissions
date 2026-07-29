class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        ns = len(s)
        np = len(p)

        dp = {}

        def solve(i, j):

            # Pattern is finished
            if j == np:
                return i == ns

            if (i, j) in dp:
                return dp[(i, j)]

            # Check whether current characters match
            first_match = (
                i < ns
                and (s[i] == p[j] or p[j] == ".")
            )

            # Check whether the next pattern character is '*'
            if j + 1 < np and p[j + 1] == "*":

                # Do not use the current pattern character
                skip = solve(i, j + 2)

                # Use current pattern character once or more
                take = False

                if first_match:
                    take = solve(i + 1, j)

                dp[(i, j)] = take or skip

            else:
                # Normal character or '.'
                dp[(i, j)] = (
                    first_match
                    and solve(i + 1, j + 1)
                )

            return dp[(i, j)]

        return solve(0, 0)