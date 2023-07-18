import queue
q=queue.Queue()
q.put(10)
q.put(20)
q.put(30)
print(q)
print(q.get())
print(q.get())
print(q.get())