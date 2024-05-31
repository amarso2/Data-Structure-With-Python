queue =[]
def enqueue():
    el =input("Enter the element: ")
    queue.append(el)
    print(queue,"is add to queue")
def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e=queue.pop(0)
        print("The element is ",e)
        print(queue,"is remove from queue")
while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        break
    else:
        print("Invalid choice")