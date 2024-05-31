import queue
q = queue.PriorityQueue()
q.put(10)
q.put(100)
q.put(90)
q.put(1)
q.put(200)

print(q.get())
print(q.get())
print(q.get())

print(q.get())
print(q.get())