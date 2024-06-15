import queue
#
# q = queue.Queue()
# q.put(10)
# q.put(10)
#
# print(q.qsize())
# q.empty()
# print(q.get())

qq = queue.PriorityQueue()
qq.put(10)
qq.put(10)

print(qq.qsize())
qq.empty()
print(qq.get())
