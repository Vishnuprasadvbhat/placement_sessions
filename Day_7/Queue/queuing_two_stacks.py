#implement Queue using 2 stacks

# def
#     self.temp = self.stack[:-1]
#     self.temp = self.temp[::-1]
#     self.stack.clear
#
class Queue:
    def __init__(self):
        self.temp = []
        self.stack = []

    def enqueue(self,value):
        self.temp = self.stack[1:]
        self.temp = self.temp[::-1]
        value = self.stack(len(self.stack)-1)
        self.stack.clear()
        self.stack = self.temp[::-1]
        return value

q = Queue()
for i in [12,3,4,5,6,7,78]:
    q.enqueue(i)
print(q.stack)


