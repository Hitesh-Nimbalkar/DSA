# MaKing Sinlge Linked Lists 
class Node:
    def __init__(self,item=None,next=None) -> None:
        self.item=item
        self.next=next 

class single_linked_list:
    def __init__(self,start=None) -> None:
        self.start=start
        
        
    def is_empty(self):
        return self.start==None
    
    
    def insert_at_start(self,data):
        print("Creating Node")
        n=Node(item=data,next=self.start)
        print(f"Node \n data = {n.item} ")

        self.start=n
        
        
    def insert_at_last(self,data):
        n=Node(item=data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            
            temp.next=n 

        else:

            self.start=n
    
    def search(self,data):
        temp=self.start 
        node_number=0
        while temp is not None:
            node_number=node_number+1

            if temp.item == data :
                print(f" Node location {node_number}")
                return temp
            temp=temp.next 

        return None 

    def insert_after(self,temp,data):

        # First search is called and we have temp pointing at the desiered node

        if temp is not None:
            n = Node(data,temp.next)
            temp.next=n 
            
    def print_list(self):
        temp=self.start
        node_number=0
        while temp is not None:
            print("\n")
            print("---------------------------------------")
            print(f"Node Number - {node_number}")
            node_number=node_number+1
            print(f" data --- {temp.item}",end=" ")
            temp=temp.next 
            
    def delete_first(self):
        self.start=self.start.next 
        
    def delete_last(self):
        temp=self.start
        
        while temp.next.next is not None:
            temp=temp.next 
        
        temp.next=None 
    
    def delete_item(self,data):
        
        # Search for the node with this data 
        temp =self.start 
        
        while temp.next is not None:
            if temp.next.item == data:
                temp.next=temp.next.next
                break
            temp=temp.next
            
            
mylist=single_linked_list()
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_last(30)
mylist.print_list()


# Search data on the node 
mylist.search(data=30)

        
        




        
