from doublynode import DoublyNode

#Doublylinklist class to add links 
class DoublyLinkedList:
    #Initialization
    def __init__(self):
        self.head = None
        self.tail = None
    
    #insert new links in the class
    def insert(self, data):
        #DoublyNode class
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            prev = None
            #while loop here to traverse prescription id
            while current and current.data.prescription_id < data.prescription_id:
                prev = current
                current = current.next
            if prev:
                new_node.next = current
                new_node.prev = prev
                prev.next = new_node
                if current:
                    current.prev = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

    #display function to display links
    def display(self):
        current = self.head
        while current:
            print(current.data.name, end=" <-> ")
            current = current.next
        print("None")
