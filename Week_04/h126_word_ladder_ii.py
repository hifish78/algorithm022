import collections


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    # res.extend(k for k in layer[w])
                    return layer[w]
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i] + c + w[i + 1:]
                            if neww in wordList:
                                for j in layer[w]:
                                    # w: dog;
                                    newlayer[neww] += [j + [neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res

sol = Solution()
wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "hit"
endWord = "cog"
res = sol.findLadders(beginWord, endWord, wordList)
print(res)

"""
layer: 
======
{'hit': [['hit']]}
{'hot': [['hit','hot']]}
{'dot':[['hit,'hot','dot']], 'lot':[['hit','hot', 'lot']]}
{'dog':[['hit', 'hot', 'dot', 'dog']], 'log': [['hit', 'hot', 'lot', 'log']]}
{'cog':[['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]}
"""



