from node import Node
from patient import Patient
from doctor import Doctor

#Singlylinklist class to add links
class SinglyLinkedList:
    #function initialization
    def __init__(self):
        self.head = None
    
    #function to insert new links
    def insert(self, data):
        new_node = Node(data)    #Node class
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            prev = None
            #while loop here to traverse the link list
            while current and isinstance(current.data, Patient) and current.data.current_condition < data.current_condition:
                prev = current
                current = current.next
            while current and isinstance(current.data, Doctor) and current.data.doctor_id < data.doctor_id:
                prev = current
                current = current.next

            if prev:
                prev.next = new_node
                new_node.next = current
            else:
                new_node.next = self.head
                self.head = new_node
    
    #display function to display
    def display(self):
        current = self.head
        while current:
            print(current.data.name, end=" -> ")
            current = current.next
        print("None")
