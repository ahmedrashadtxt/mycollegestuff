class SinglyLinkedListNode():

    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_to_front(self,data):
        newNode = SinglyLinkedListNode(data)

        if (self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insert_to_last(self,data):
        newNode = SinglyLinkedListNode(data)

        if(self.tail == None):
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def insert_to_index(self,data,index):
        newNode = SinglyLinkedListNode(data)

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
                current.next = newNode

    def traverse(self):
        current = self.head

        print("[",end="")

        while(current != None):
            print(current.data,end="")

            if(current != self.tail):
                print(",",end="")

            current = current.next

        print("]")
    
    def remove_from_front(self):
        data = None

        if(self.head != None):

            if(self.head == self.tail):
                data = self.head.data
                self.head = None
                self.tail = None
            else:
                node = self.head
                self.head = self.head.next
                node.next = None
                data = node.data

        return data

    def remove_from_back(self):
        data = None

        if(self.head != None):

            if(self.head == self.tail):
                data = self.head.data
                self.head = None
                self.tail = None
            else:
                node = self.head

                #while statement to reach the node before tail
                while(node.next != self.tail):
                    node = node.next

                node.next = None
                data = self.tail.data
                self.tail = node

        return data 
    
    def remove_from_index(self,index):
        
        data = None

        if(self.head != None):
            
            if(index == 0):
                data = self.remove_from_front()

            else:
                node = self.head
                count = 0
                while(node.next != self.tail and index != count+1):
                    node = node.next
                    count += 1
                
                if(index == count+1):
                    removedNode = node.next
                    node.next = removedNode.next
                    removedNode.next = None

                    if(removedNode == self.tail):
                        self.tail = node
                    
                    data = removedNode.data

        return data


    def search(self,value):

        current = self.head

        while(current != None):
            if(current.data == value):
                return True
            current = current.next

        return False 






singlyList = SinglyLinkedList()
singlyList.traverse()
singlyList.insert_to_front(10)
singlyList.traverse()
singlyList.insert_to_front(20)
singlyList.traverse()
singlyList.insert_to_last(100)
singlyList.traverse()
singlyList.insert_to_last(200)
singlyList.traverse()
singlyList.insert_to_index(500,2)
singlyList.traverse()
singlyList.remove_from_front()
singlyList.traverse()
singlyList.remove_from_back()
singlyList.traverse()
singlyList.remove_from_index(1)
singlyList.traverse()
print(singlyList.search(100))
print(singlyList.search(101))
    