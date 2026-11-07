class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:

        # where each letter sits in the alien alphabet
        rank = {}
        for i in range(len(order)):
            rank[order[i]] = i

        # true when first belongs at or before second
        def in_order(first: str, second: str) -> bool:
            shorter = min(len(first), len(second))

            # the first position where they differ settles the whole comparison
            for i in range(shorter):
                if rank[first[i]] != rank[second[i]]:
                    return rank[first[i]] < rank[second[i]]

            # one is a prefix of the other, so the shorter one has to come first
            return len(first) <= len(second)

        # the list is sorted exactly when every neighbouring pair is
        for i in range(len(words) - 1):
            if not in_order(words[i], words[i + 1]):
                return False

        return True