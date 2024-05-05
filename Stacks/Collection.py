import collections
stack = collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)
stack.pop()
print(stack)
if not stack:
    print("Stack is empty")
else:
    print(stack)
       
