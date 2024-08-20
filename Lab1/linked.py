class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next: 
                current = current.next
            current.next = new_node
            
    def insb(self,data):
        new_node=Node(data)
        if self.head!= None:
            
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=new_node
    def insl(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            prev=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def insm(self,data,pos):
        count=1
        new_node=Node(data)
        current=self.head
        prev=None
        
        while count<pos :
            prev=current
            current=current.next
            count+=1
            
        prev.next=new_node
        new_node.next=current
    def print_list(self):
        current = self.head
        while current.next:
            print(current.data, end=" -> ")
            current = current.next
        print(current.data) 
    def delb(self):
        if self.head:
            self.head=self.head.next
    def dele(self):
        if self.head!= None:
            prev=None
            current=self.head
            while current.next!=None:
                prev=current
                current=current.next
            prev.next=None

llist = LinkedList()
llist.insert(10)
llist.insert(20)
llist.insert(30)
llist.print_list()
llist.insb(5)
llist.print_list()
llist.insm(15, 3)
llist.print_list()
llist.insl(35)
llist.print_list()
llist.insl(70)
llist.delb()
llist.dele()