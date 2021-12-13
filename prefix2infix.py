class Stack:

    def __init__(self):
        self.stack_list = []

    def print(self):
        print(self.stack_list)
    
    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        if(self.isEmpty()):
            return None
        else:
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



def prefix_to_infix(expression):

    operators = ["+","-","*","/"]
    stack = Stack()

    infix = ""

    reversed_expression = expression[::-1]

    for i in reversed_expression:

        if(i not in operators):
            stack.push(i)
        else:
            infix = "(" + stack.pop() + i + stack.pop() + ")"
            stack.push(infix)

    return stack.pop()


def evaluate_prefix(expression):

    operators = ["+","-","*","/"]
    stack = Stack()

    total = 0

    reversed_expression = expression[::-1]

    for i in reversed_expression:

        if(i not in operators):
            stack.push(i)
        else:
            total = evaluate_operator(i,int(stack.pop()),int(stack.pop()))
            stack.push(total)
    
    return stack.pop()


def evaluate_operator(operator,number1,number2):

    if(operator == "+"):
        sum = number1 + number2
        return sum
    elif(operator == "-"):
        diff = number1 - number2
        return diff
    elif(operator == "*"):
        product = number1 * number2
        return product
    elif(operator == "/"):
        div = number1 / number2
        return div

    



str = "*+23+45"
print(prefix_to_infix(str))
print(evaluate_prefix(str))