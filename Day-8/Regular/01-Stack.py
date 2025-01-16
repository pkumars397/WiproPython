def create_stack():
    stack=[]
    return stack

# class create_stack:
#     def __init__(self):
#         self.stack=[]  # we can also create stack via class ,all methods inside class

#isEmpty 
def isEmpty(s):
    return len(s)==0
#push
def push(s,e):
    s.append(e)

#Pop
def pop(stack):
    if (isEmpty(stack)):
        return "stack is empty"

    return stack.pop()
#peak
def peek(s):
    return s[-1]

stack=create_stack()

push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))