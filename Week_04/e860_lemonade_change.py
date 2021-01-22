class Solution:
    # 我们只需要统计5， 10元的数量，20元的不需要统计，因为20元的对找零没有任何用处
    # 顾客给5元，5元的数量+1
    # 顾客给10元，如果没有5元的，return false. 10元的数量+1， 5元的数量-1
    # 顾客给20元，优先消耗一个10和一个5，如果不够，再消耗三个5
    # 因为美元10只能给账单20找零，而美元5可以给账单10和账单20找零，美元5更万能！
    # 所以局部最优：遇到账单20，优先消耗美元10，完成本次找零。全局最优：完成全部账单的找零。

    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
            if bill == 10:
                if five <= 0:
                    return False
                ten += 1
                five -= 1
            if bill == 20:
                if five > 0 and ten > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True