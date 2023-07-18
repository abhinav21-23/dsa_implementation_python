stack=[]
def push():
    if len(stack)!=n:
        element=int(input("Enter the element\n"))
        stack.append(element)
        print(stack)
    else:
        print("Stack is full")

def pop():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Removed element is:", e)
        print(stack)

n=int(input("Enter the limit of stack\n"))
while True:
    print("Enter the operation you want to perform 1.push, 2.pop, 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter the correct option!")