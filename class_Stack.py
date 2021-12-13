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

my_stack = Stack()
my_stack.push(9)
my_stack.print()
my_stack.push(11)
my_stack.print()
my_stack.pop()
my_stack.print()