stack = []
def push() :
    elements = input("Enter element")
    stack.append(elements)
    print(stack)
    
def pop() :
    if not stack :
        print("Stack is empty")
    else :
        e=stack.pop()
        print("At least one element is removed ",e)
        print(stack)

while True : 
    print("1.Push")
    print("2.Pop")
    print("3.Exit")
    choice = int(input("Enter your choice"))
    if choice == 1 :
        push()
    elif choice == 2 :
        pop()
    elif choice == 3 :
        break
    else :
        print("Invalid choice")