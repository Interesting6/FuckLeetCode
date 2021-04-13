#
# @lc app=leetcode.cn id=1603 lang=python3
#
# [1603] 设计停车系统
#

# @lc code=start
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cap = [big, medium, small]
        self.now = [0, 0, 0]


    def addCar(self, carType: int) -> bool:
        if self.now[carType-1] < self.cap[carType-1]:
            self.now[carType-1] += 1
            return True
        else:
            return False




# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end

