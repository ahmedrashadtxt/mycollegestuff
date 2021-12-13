class Stack:

    def __init__(self):
        self.stack_list = []

    def print(self):
        print(self.stack_list)
    
    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def isEmpty(self):
        return self.stack_list == []

    def length(self):
        return len(self.stack_list)


class S_Queue():

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def print(self):
        self.stack_1.print()

    def enqueue(self, item):
        #move items from stack1 to stack2 (empty stack1)
        while(not self.stack_1.isEmpty()):
            self.stack_2.push(self.stack_1.pop())

        #push the new item to stack1
        self.stack_1.push(item)

        #move back the items from stack2 to stack1
        while(not self.stack_2.isEmpty()):
            self.stack_1.push(self.stack_2.pop())

    def dequeue(self):
        if(self.isEmpty()):
            return None
        else:
            return self.stack_1.pop()

    def peek(self):
        if(self.isEmpty()):
            return None
        else:
            return self.stack_1.peek()

    def isEmpty(self):
        return self.stack_1.isEmpty()

    def length(self):
        return self.stack_1.length()


queue = S_Queue()

queue.print()
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(6)
queue.print()

queue.dequeue()
queue.print()

queue.dequeue()
queue.print()

queue.enqueue(7)
queue.print()

print(queue.peek())