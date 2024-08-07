# Algorithm/technique: hash table
# Time complexity:     O(n)
# Auxiliary space:     O(n)
# Optimal:             yes

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        i: int
        c: str
        count: dict[str, int] = {}
        for i, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1

        return not any(count.values())
