from collections import deque
from typing import List


class Solution:
    # Time Complexity: O(MN) M -word length, N - wordList Length
    # Space Complexity: O(N): N -wordList Length
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # The reason to use set is: reduce the search time o(1)
        # otherwise is O(N) for endWord in wordList(timeout)
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque()
        queue.append((beginWord, 1))
        # for i in range(26):  chr(97+i) --> 'a' --> 'z'
        letters = "abcdefghijklmnopqrstuvwxyz"

        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            for idx, val in enumerate(word):
                for ch in letters:
                    if ch == val:
                        continue
                    new = word[:idx] + ch + word[idx+1:]
                    if new in word_set:
                        queue.append((new, level + 1))
                        word_set.remove(new)
        return 0

    # use set: visted to mark the word is visited or not
    # for i in range(97, 123): chr(i)
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque()
        queue.append((beginWord, 1))
        # letters = "abcdefghijklmnopqrstuvwxyz"
        visited = set()
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            for idx, val in enumerate(word):
                for i in range(97,123):
                    if chr(i) == val:
                        continue
                    new = word[:idx] + chr(i) + word[idx+1:]
                    if new in word_set and new not in visited:
                        queue.append((new, level + 1))
                        visited.add(new)
        return 0

    #和单向BFS不同的是，分别从beginWord和endWord开始做BFS，并分别将满足条件的单词加入到lqueue、lvisited和rqueue、rvisited。
    # 以层为单位递增step
    # 每次对元素少的队列进行BFS，如果访问到的单词在另外一边已被访问过，说明接龙成功，返回step
    def ladderLength3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        left_queue = deque()
        right_queue = deque()
        left_queue.append(beginWord)
        right_queue.append(endWord)

        left_visited = set()
        right_visited = set()
        left_visited.add(beginWord)
        right_visited.add(endWord)

        step = 0
        letters = "abcdefghijklmnopqrstuvwxyz"

        while left_queue and right_queue:
            # 每次对元素少的队列进行BFS，
            if len(left_queue) > len(right_queue):
                left_queue, right_queue = right_queue, left_queue
                left_visited, right_visited = right_visited, left_visited

            step += 1
            for _ in range(len(left_queue)):
                # 如果访问到的单词在另外一边已被访问过，说明接龙成功，返回step
                cur = left_queue.popleft()
                if cur in right_visited:
                    return step

                for idx, val in enumerate(cur):
                    for ch in letters:
                        if ch == val:
                            continue
                        new = cur[:idx] + ch + cur[idx + 1:]
                        if new in word_set and new not in left_visited:
                            left_queue.append(new)
                            left_visited.add(new)

        return 0


sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
res = sol.ladderLength2(beginWord, endWord, wordList)
print(res)
