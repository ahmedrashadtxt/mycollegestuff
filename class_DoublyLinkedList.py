from typing import TypeAlias


class DoublyLinkedListNode():

    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None


    def insert_to_front(self,data):
        newNode = DoublyLinkedListNode(data)

        if (self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            newNode.prev = newNode
            self.head = newNode

    def insert_to_last(self,data):
        newNode = DoublyLinkedListNode(data)

        if(self.tail == None):
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def insert_to_index(self,data,index):
        newNode = DoublyLinkedListNode(data)

        if(self.head == None):
            self.head = newNode
            self.tail = newNode
        elif(index == 0):
            self.insert_to_front(data)
        else:
            current = self.head
            count = 0
            while(current.next != None and index!=count+1):
                current = current.next
                count += 1

            if(current == self.tail):
                self.insert_to_last(data)
            else:
                newNode.next = current.next
                newNode.next.prev = newNode
                current.next = newNode
                newNode.prev = current
    
    def traverse(self):
        current = self.head

        print("[",end="")

        while(current != None):
            print(current.data,end="")

            if(current != self.tail):
                print(",",end="")

            current = current.next
            
        print("]")

node1 = DoublyLinkedList(10)
node2 = DoublyLinkedList(15)

node1.next = node2
node2.prev = node1