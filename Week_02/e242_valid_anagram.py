import collections


class Solution:
    # Time: O(N); Space: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False

        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1

        for ch in t:
            dic[ch] = dic.get(ch, 0) - 1

        for key in dic:
            if dic[key] != 0:
                return False
        return True

    # Time: O(N); Space: O(1)
    def isAnagram2(self, s: str, t: str) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False

        freq_list = [0] * 26
        for ch in s:
            key = ord(ch) - ord('a')
            freq_list[key] += 1

        for ch in t:
            key = ord(ch) - ord('a')
            freq_list[key] -= 1

        for item in freq_list:
            if item != 0:
                return False
        return True

    # Time: O(NlogN); Space: O(1)
    def isAnagram3(self, s: str, t: str) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def isAnagram4(self, s: str, t: str) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False
        return collections.Counter(s) == collections.Counter(t)
