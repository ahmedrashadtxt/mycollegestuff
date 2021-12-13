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


def infix_to_prefix(expression):
    operators = ["+","-","*","/"]
    open_p = ["(","[","{"]
    close_p = [")","]","}"]
    stack = Stack()

    prefix = ""

    reversed_expression = expression[::-1]

    for i in reversed_expression:

        if (i in operators):
            if(stack.peek() in operators):
                while(operators.index(stack.peek()) >= operators.index(i)):
                    prefix += stack.pop()
                    if(not stack.peek() in operators):
                        break
            stack.push(i)

        elif (i in open_p):
           while(not stack.peek() in close_p):
               prefix += stack.pop()
           stack.pop() 

        elif (i in close_p):
            stack.push(i)
        else:
            prefix += i

    while(not stack.isEmpty()):
        prefix += stack.pop()

    return prefix[::-1]

expression = "(2+3)*(4+5)"

print(infix_to_prefix(expression))