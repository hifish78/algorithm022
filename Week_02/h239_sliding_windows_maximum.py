import collections

# postion (i -k + 1) ---> position(i) have K elements
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic queue
        # 当加入一个新元素后，会把queue里面所有比它小的数都删掉
        # 只存储从当前位置开始可能的最大值，把所有不可能的剔除掉
        # 维护一个长度小于等于k的单调递减的单调队列，不断向右滑动，该单调队列的第一个元素即为该窗口的最大元素

        # 需要使用双端队列，存入的是数组nums的index而不是nums的值，因为这里要实时计算单调队列中的最大元素是不是在[i - k + 1, i]中，
        # 如果当前元素大于单调队列中的尾端元素的话：pop（弹出尾端元素）单调队列中的尾端元素，直到单调队列为空，再加入当前元素
        # https://leetcode-cn.com/problems/sliding-window-maximum/solution/python-jian-ji-de-dan-diao-dui-lie-jie-f-q56i/

        res = []
        n = len(nums)

        # 使用双端队列，并且存入index
        deque = collections.deque()

        for i in range(n):
            # 如果当前元素大于单调队列中的尾端元素的话：pop单调队列中的尾端元素
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)

            # 当单调队列的第一个元素（即最大的元素）不在[i - k + 1, i]，
            # 说明该最大元素在当前的窗口之外，则popleft单调队列中的第一个元素
            if deque[0] < i - k + 1:
                deque.popleft()

            # 在当前index >= k -1 的时候（即这时候已经能够构成长度为k的窗口）把单调队列的第一个元素加入
            if i - k + 1 >= 0:
                res.append(nums[deque[0]])
        return res