from os import stat


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
        if(self.isEmpty()):
            return None
        else:
            return self.stack_list[-1]

    def isEmpty(self):
        return self.stack_list == []

    def length(self):
        return len(self.stack_list)


def infix_to_postfix(expression):

    operators = ["+","-","*","/"]
    open_p = ["(","[","{"]
    close_p = [")","]","}"]

    postfix = ""

    stack = Stack()

    for i in expression:

        if (i in operators):
            if (stack.peek() in operators):
                while(operators.index(stack.peek()) >= operators.index(i)):
                    postfix += stack.pop()
                    if (not stack.peek() in operators):
                        break
            stack.push(i)

        elif (i in open_p):
            stack.push(i)

        elif (i in close_p):
            while(not stack.peek() in open_p):
                postfix += stack.pop()
            stack.pop()

        else:
            postfix += i

    while(not stack.isEmpty()):
        postfix += stack.pop()

    return postfix

expression = "A*B+C*D"

print(infix_to_postfix(expression))