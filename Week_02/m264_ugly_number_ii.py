'''
(1) 1x2,  2x2, 2x2, 3x2, 3x2, 4x2, 5x2...
(2) 1x3,  1x3, 2x3, 2x3, 2x3, 3x3, 3x3...
(3) 1x5,  1x5, 1x5, 1x5, 2x5, 2x5, 2x5...

仔细观察上述三个列表，可以发现每个子列表都是一个丑陋数分别乘以 2，3，5，
而要求的丑陋数就是从已经生成的序列中取出来的，每次都从三个列表中取出当前最小的那个加入序列
https://www.cnblogs.com/grandyang/p/4743837.html
https://leetcode-cn.com/problems/chou-shu-lcof/solution/chou-shu-ii-qing-xi-de-tui-dao-si-lu-by-mrsate/

1.第一个丑数是1，分别被p2,p3,p5三个指针指向。三个指针分别代表该丑数等待被 * 2 * 3 * 5,或者说是该丑数是否通过* 2 * 3 * 5产生过新丑数的标识
2.当一个丑数已经被* 2 * 3 * 5后，对于生成丑数已经没有用了，我们把对应指针前移一位（即复用标识），让下一个丑数等待被*来生成新丑数。
3.每次计算出来个三个丑数的最小的一个作为新丑数加入，然后判断是通过 * 多少得到的来后移对应指针。（这里记得去重）
通过123我们可以发现，我们每次生成的都是最小的丑数（保证是升序），并且每个丑数都尝试过被 *2 *3 *5（保证无遗漏）

主要的两点：
1）一个丑数乘以 2， 3， 5 之后， 一定还是一个丑数;
2）一个丑数和2，3 5相乘以后，应该丢弃（所以指针后移动）
'''
import heapq


class Solution:
    # Time Complexity: O(N) to retrieve prelimiary computed N ugly number(如果说明丑数不超过1690， 那么时间复杂度是O（1））
    # Space Complexity: O(N) (如果说明丑数不超过1690， 那么空间复杂度是O（1））
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            next_ugly = min(u2, u3, u5)
            if next_ugly == u2:
                i2 += 1
            if next_ugly == u3:
                i3 += 1
            if next_ugly == u5:
                i5 += 1
            ugly.append(next_ugly)
            n -= 1
        return ugly[-1]

    def nthUglyNumber2(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        ugly = [1]
        for i in range(1, n):
            next_ugly = min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5]* 5)
            ugly.append(next_ugly)
            if next_ugly == ugly[p2] * 2:
                p2 += 1
            if next_ugly == ugly[p3] * 3:
                p3 += 1
            if next_ugly == ugly[p5] * 5:
                p5 += 1
        return ugly[-1]

    # Python default is min heap
    '''
    很容易想到的方法是：从1起检验每个数是否为丑数，直到找到n个丑数为止。但是随着n的增大，绝大部分数字都不是丑数，我们枚举的效率非常低。因此，换个角度思考，如果我们只生成丑数，且生成n个，这道题就迎刃而解。
    不难发现生成丑数的规律：如果已知丑数ugly，那么ugly * 2，ugly * 3和ugly * 5也都是丑数。
    既然求第n小的丑数，可以采用最小堆来解决。每次弹出堆中最小的丑数，然后检查它分别乘以2、3和 5后的数是否生成过，如果是第一次生成，那么就放入堆中。第n个弹出的数即为第n小的丑数。
    
    创建最小堆heap，哈希表 seen和质因数列表factors = [2, 3, 5]。heap用于存储已生成的丑数，弹出最小值；seen用于标记堆中出现过的元素，避免重复入堆。
    初始化将1入堆，并添加到seen。
    重复以下步骤n次： 弹出堆中最小的数字 curr_ugly。 对于factors中每个因数f，生成新的丑数new_ugly。若new_ugly不在seen中，则将其添加到heap中并更新seen。
    curr_ugly即为第n小的丑数，返回。
    '''
    # Time Complexity: O(NLOGN), 弹出每个最小值时，时间复杂度都为堆的高度，因此时间复杂度为O(nlog(n))。
    # SPACE TIME: O(n)。遍历n个丑数，并将每个丑数乘以2、3和5的结果存入堆中。堆和哈希表的元素个数都不会超过n * 3。
    def nthUglyNumber3(self, n: int) -> int:
        heap = []
        heapq.heappush(heap, 1)

        seen = set()
        seen.add(1)

        factors = [2, 3, 5]

        cur_ugly = 1
        for _ in range(n):
            # 每次弹出当前最小丑数
            cur_ugly = heapq.heappop(heap)
            # 生成新的丑数
            for f in factors:
                new_ugly = f * cur_ugly
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return cur_ugly


sol = Solution()
res = sol.nthUglyNumber3(2)
print(res)