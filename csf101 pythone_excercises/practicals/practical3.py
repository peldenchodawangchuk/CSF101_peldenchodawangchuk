#implementing stack
# class Stack:
#     def __init__(self):
#         self.items = []
#     def is_empty(self):
#         return len(self.items) == 0
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("stack is empty")
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError("stack is empty")
#     def size(self):
#         return len(self.items)
# #test the stack implementation
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())  # Output: 3
# print(stack.peek())  # Output: 2
# print(stack.size())  # Output: 2

#impementing queue
class Queue:
    def __init__(pele):
        pele.items = []
    
    def is_empty(pele):
        return len(pele.items) == 0
    
    def enqueue(pele, item):
        pele.items.append(item)
    
    def dequeue(pele):
        if not pele.is_empty():
            return pele.items.pop(0)
        else:
            raise IndexError("queue is empty")
    
    def peek(pele):
        if not pele.is_empty():
            return pele.items[0]
        else:
            raise IndexError("queue is empty")
    
    def size(pele):
        return len(pele.items)
#test the queue implementation
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.peek())     # Output: 2
print(queue.size())     # Output: 2