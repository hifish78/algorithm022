import collections
from typing import List

'''

Maintain a map : {String -> List} where each key K is a sorted string, and each value is the list of strings from the 
initial input that when we sorted, are equal to K.

In Java, we will store the kye as as a string. In python, we will store the key as a hashable tuple/

dict.get(key) vs dict[key] ???
d = dict()
d['xyz'] --> throw KeyError

d.get('xyz')  --> no error throw , it is "None"
dict.get(key) --> Return the value for key if key is in the dictionary, else default like dict.get(key, xxx)
                  If default is not given, it defaulst to None.so NEVER raise a KeyError

Note: we can NOT write the line:
dic.get(key).append(s)  => key does NOT exist in dic, so it will return None. We will hit the error:
AttributeError: 'NoneType' object has no attribute 'append'
    dic.get(key).append(s)
We can use dic[key] since if key does NOT exist in dic, will use default one (list)
'''

# Time Complexity: O(NKLogK)
# K is the maximum length of a string in strs, sorted : KLogK
# N is the length of strs
#Space Complexity: total information conetent sorted in dic is: O(NK)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            dic[key].append(s)
            # dic.get(key).append(s)  =>
        return dic.values()

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in dic:
                dic.get(key).append(str)
            else:
                dic[key] = [str]
        return dic.values()

    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for str in strs:
            dic[tuple(sorted(str))].append(str)
        return dic.values()
