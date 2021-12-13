class Queue:
    
    def __init__(self):
        self.queue_list = []

    def print(self):
        print(self.queue_list)

    def enqueue(self, item):
        self.queue_list.append(item)

    def dequeue(self):
        if(self.isEmpty()):
            return None
        else:
            return self.queue_list.pop(0)
    
    def peek(self):
        if(self.isEmpty()):
            return None
        else:
            return self.queue_list[0]

    def isEmpty(self):
        return self.queue_list == []

    def length(self):
        return len(self.queue_list)


class Q_Stack:

    def __init__(self):
        self.queue_1 = Queue()
        self.queue_2 = Queue()

    def print(self):
        self.queue_1.print()

    def push(self, item):
        while(not self.queue_1.isEmpty()):
            self.queue_2.enqueue(self.queue_1.dequeue())

        self.queue_1.enqueue(item)

        while(not self.queue_2.isEmpty()):
            self.queue_1.enqueue(self.queue_2.dequeue())

    def pop(self):
        if(self.queue_1.isEmpty()):
            return None
        else:
            return self.queue_1.dequeue()

    def peek(self):
        if(self.queue_1.isEmpty()):
            return None
        else:
            return self.queue_1.peek()

    def isEmpty(self):
        self.queue_1.isEmpty()

    def length(self):
        self.queue_1.length()


my_stack = Q_Stack()
my_stack.push(9)
my_stack.print()
my_stack.push(11)
my_stack.print()
my_stack.pop()
my_stack.print()