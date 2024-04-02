from node import Node
from singlylinklist import SinglyLinkedList

#Implement queue by class 
class Queue:
    def __init__(self):
        #SINGLYlinklist class
        self.items = SinglyLinkedList()
    
    #enqueue function of queue
    def enqueue(self, item):
        new_node = Node(item)  # Create a new node
        if self.items.head is None:
            self.items.head = new_node  
        else:
            new_node.next = self.items.head
            self.items.head = new_node
    #dequeue function of queue 
    def dequeue(self):
        if not self.is_empty():
            data = self.items.head.data  #to get head
            self.items.head = self.items.head.next  # Move head pointer to the next node
            return data

    #is empty function of queue
    def is_empty(self):
        return self.items.head is None