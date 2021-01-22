from typing import List

'''
direx[]direy[] 的下标 i 代表了当前机器人的方向

    i=0,向北
    i=1,向东
    i=2,向南
    i=3,向西

当读取到调整方向的指令时，如

    "-1"：“向右转90度”，只要当前方向curdire + 1就可以得到右转方向
    "-2"：“向左转90度”，只要当前方向curdire + 3 就可以得到左转方向 (curdire + 3) % 4，
    因为不管curdire当前是哪个方向，左转都在其左边，在direx数组的定义中顺势针数3个就是其左边，所以就是加3
    (0, 1) -> turn right(1, 0) --> turn right(0, -1) -> turn right (-1, 0) == > (cur_dir + 1) % 4
    (0, 1) --> turn left (-1, 0) ==> index is 3 , so (cur_dir + 3) % 4 
'''
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        if not commands:
            return 0
        # up, right, down, left
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, cur_dir = 0, 0, 0
        res = 0

        obstacles_set = set()
        for i in range(len(obstacles)):
            obstacles_set.add((obstacles[i][0], obstacles[i][1]))

        for i in range(len(commands)):
            if commands[i] == -1:  # turn right
                cur_dir = (cur_dir + 1) % 4
            elif commands[i] == -2:  # turn left
                cur_dir = (cur_dir + 3) % 4
            else:
                for j in range(commands[i]):
                    nx = x + dirs[cur_dir][0]
                    ny = y + dirs[cur_dir][1]
                    if (nx, ny) not in obstacles_set:
                        x = nx
                        y = ny
                        res = max(res, x * x + y * y)
                    else:
                        break
        return res

sol = Solution()
commands = [4,-1,4,-2,4]
obstacles = [[2,4]]
res = sol.robotSim(commands, obstacles)
print(res)