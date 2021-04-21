


# class Solution:
#     def getOrder(self, tasks):
#         tasks = sorted(t + [i] for i, t in enumerate(tasks))
#         avail = []
#         time = 1
#         ans = []
#         from bisect import insort
#         import heapq
#         while tasks or avail: # 还有任务未到，或还有任务等待
#             while tasks and tasks[0][0] <= time: 
#                 enqueue, proc_tm, index = tasks.pop(0)
#                 insort(avail, [proc_tm, index])
#                 # heapq.heappush(avail, [proc_tm, index]) # 小根堆不行
#             if avail: # 有任务在等待，优先处理在等待的任务
#                 proc_tm, index = avail.pop(0)  # 处理所需时间最短的任务
#                 time += proc_tm  # 进入完成该等待任务的
#                 ans.append(index)
#             elif tasks: # 无任务在等待
#                 time = tasks[0][0] # 进入下一个未到任务的时间
#         return ans

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        heap = []
        tasks = [[x, y, i] for i, (x, y) in enumerate(tasks)]
        tasks = deque(sorted(tasks))

        cur = 0
        while heap or tasks: # 还有等待的任务和未出现的任务
            if heap == []: # 当前无等待任务，由上while知肯定有还未出现的任务
                cur = max(cur, tasks[0][0]) # 取第一个未出现的任务时间作为当前时间
            while tasks and tasks[0][0] <= cur: # 还有为出现的任务时，将小于当前时间(即已经出现的任务)加入小根堆中
                s, t, i = tasks.popleft() # 把当前出现的任务从未出现中删掉
                heappush(heap, [t, i]) # 同时将其加入等待任务中
            t, i = heappop(heap) # 按顺序每次一个处理等待中的任务
            cur += t # 时间跳到处理完该任务的时间
            res.append(i)
        return res
