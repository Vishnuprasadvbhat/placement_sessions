class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.max = 100
        self.queue = []

    def isfull(self):
        if self.rear == self.max -1:
            return print('Stack overflow')

    def isempty(self):
        if self.front and self.rear == -1:
            return print('Stack underflow')

    def enqueue(self, value):
        if self.isfull():
            return print("Stack Overflow: Cannot take input")
        elif self.isempty():
            self.queue.append(value)
            self.rear  += 1
            self.front += 1
            return print(self.queue)
        else:
            self.queue.append(value)
            self.rear += 1
            return print(self.queue,self.rear)

    def dequeue(self,value):

        if self.isempty():
            return print('Stack undeflow')

        elif self.rear == self.front:
            self. queue.pop(self.front)
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
            self.queue.pop(self.front)
        return print(self.queue, self.front)

    def display(self):
        print(self.queue)

queue =Queue()
queue.enqueue(15)
queue.enqueue(25)
queue.display()
