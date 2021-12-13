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


def check_parentheis(expression):
    #return True if expression is balanced

    stack = Stack()

    for i in expression:
        if (i=="(" or i=="[" or i=="{"):
            stack.push(i)
        elif (i==")" or i=="]" or i=="}"):
            if (not stack.isEmpty()):
                item = stack.pop()

                if(i==")"):
                    if(not item=="("):
                        return False
                elif(i=="]"):
                    if(not item=="["):
                        return False
                elif(i=="}"):
                    if(not item=="{"):
                        return False
            else:
                return False

    if(stack.isEmpty()):
        return True
    else:
        return False

expression1 = "[{(2+4)*12}-24]"
expression2 = "[{(2+4)*12]-24]"

print(check_parentheis(expression1))
print(check_parentheis(expression2))