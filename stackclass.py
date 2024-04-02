from doublylist import DoublyLinkedList

#Stack class implemented
class Stack:
    def __init__(self):
        #Create a new node of doublylink list
        self.items = DoublyLinkedList()
    
    #push function of stack
    def push(self, item):
        self.items.insert(item)
    
    #pop function of stack
    def pop(self):
        if not self.is_empty():
            data = self.items.tail.data
            self.items.tail = self.items.tail.prev
            if self.items.tail:
                self.items.tail.next = None
            return data
    
    #is empty function of stack
    def is_empty(self):
        return self.items.head is None