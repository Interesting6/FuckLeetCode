#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#

# @lc code=start
from typing import List
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        from collections import deque, defaultdict
        stop_buses = defaultdict(set) # 每个车站能乘坐的公交车
        for i, stops in enumerate(routes):
            for stp in stops:
                stop_buses[stp].add(i) # 在车站stp，能乘坐的公交车为i号，2号公交车能到达的路线则为routes[i]
        bus_stops = [set(r) for r in routes] # 每辆公交车能到达的站台
        dq = deque([source])
        vis_stops = set([source]) # 已经到达过的公交站
        vis_bus = set() # 已经乘过的公交车
        step = -1
        while dq:
            step += 1
            sz = len(dq)
            for _ in range(sz):
                stp = dq.popleft()
                if (stp == target):
                    return step
                valid_buses = stop_buses[stp] - vis_bus # 在车站stp可以乘坐的公交车集合
                for bus in valid_buses: # 在车站stp乘坐公交车bus
                    valid_stations = bus_stops[bus] - vis_stops # 乘坐公交车bus可以到达的站台
                    vis_bus.add(bus)
                    for next_stp in valid_stations: # 乘坐公交车bus到达车站stp
                        dq.append(next_stp)
                        vis_stops.add(next_stp)

        return -1
"""
Accepted
45/45 cases passed (204 ms)
Your runtime beats 75.26 % of python3 submissions
Your memory usage beats 5.1 % of python3 submissions (51.9 MB)
"""
# routes = [[1,2,7],[3,6,7]]; source = 1; target = 6
# routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]; source = 15; target = 12
# s = Solution().numBusesToDestination(routes, source, target)
# print(s)

# @lc code=end


