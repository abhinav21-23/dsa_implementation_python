queue=[]
def enqueue():
    element=int(input("Enter the element\n"))
    queue.append(element)
    print(element, "is added to queue")

def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("Removed element is", e)

def display():
    print(queue)


while True:
    print("Select the opertaion 1.Add 2.Remove 3.Show 4.Quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter the correct option")