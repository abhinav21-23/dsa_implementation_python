import queue
stack=queue.LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(30)
# stack.put(40, timeout=0.5)
stack.get()
stack.get()
print(stack)
