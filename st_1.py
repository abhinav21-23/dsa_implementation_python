# using list
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

# top/peek element
print(stack[-1])

stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()

# stack.pop()   underflow condition
print(stack)

# length of stack
print(len(stack)==0)
print(not stack)

