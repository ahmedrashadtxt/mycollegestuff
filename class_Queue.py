class Queue:

    def __init__(self):
        self.queue_list = []

    def print(self):
        print(self.queue_list)

    def enqueue(self,item):
        self.queue_list.append(item)

    def dequeue(self):
        if (self.isEmpty()):
            return None
        else:
            return self.queue_list.pop(0)

    def peek(self):
        if (self.isEmpty()):
            return None
        else:
            return self.queue_list[0]

    def isEmpty(self):
        return self.queue_list == []

    def legth(self):
        return len(self.queue_list)

queue = Queue()

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