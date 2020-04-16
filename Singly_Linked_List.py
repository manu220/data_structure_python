class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:


    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_after(self,prev,data):
        new_node=Node(data)
        if prev is None:
            print("prev node should  be in list")
            return
        new_node.next=prev.next
        prev.next=new_node

    def append(self,data):
        new_node=Node(data)
        temp=self.head
        if temp is None:
            self.head.next=new_node
            return
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def printList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def delete(self,key):
        print("performing delete"*8)
        curr_node=self.head
        if curr_node and curr_node.data==key:
            self.head=curr_node.next
            return
        while curr_node and curr_node!=key:
            prev=curr_node
            curr_node=curr_node.next
        if curr_node is None: return
        prev.next=curr_node.next
        curr_node=None

    def del_LL(self):
        temp=self.head
        while temp:
            del temp.data
            temp=temp.next

    def length(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count

    def search(self,key): #iterative  search
        curr_node=self.head
        while curr_node!=None:
            if curr_node.data==key:
                return True
            curr_node=curr_node.next
        return False

    def searckh(self, li, key):
        if li==None: return False
        if li.data==key: return True
        return self.search(li.next,key)

    def getNth(self,index):
        curr=self.head
        i=0
        while i<index:
            curr=curr.next
            i+=1
        return curr.data

    def printNthFromLast(self,n): # Method1: Using length of the linked list
        current=self.head
        length=0
        while current:
            length+=1
            current=current.next
        if n>length:
            print("index is greater than the length of the linked list")
            return
        temp=self.head
        i=0
        while i<(length-n):
            temp=temp.next
            i+=1
        print(temp.data)

    def count(self,key):# method1 without recursison
        current=self.head
        counter=0
        while current:
            if current.data==key:
                counter+=1
            current=current.next
        return counter

    def count1(self,li,key):# Method 2 : using recursion
        if li is None:
            return 0
        if li.data==key:
            return 1+self.count1(li.next,key)
        return self.count1(li.next,key)

    def detect_loop(self):
        s=set() #used  for hashing
        curr=self.head
        while curr:
            if curr in s:
                return True
            s.add(curr)
            curr=curr.next
        return False

    def detect_loop_fastest(self):
        slow_p=self.head
        fast_p=self.head
        while slow_p and fast_p and fast_p.next:
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            if slow_p==fast_p:
                print("Loop found")
                return True
        print("Loop Not found")
        return False
    def detectandcountloop(self):
        if self.detect_loop_fastest():
            count=1
            init=slow_p
            while True:
                slow_p=slow_p.next
                if slow_p==init: break
                count+=1
        else: print("No loop found")
        return print("length of the loop is ",count)

if __name__=="__main__":
    llist=LinkedList()
    llist.head=Node(15)
    second=Node(20)
    third=Node(25)
    llist.head.next=second
    second.next=third
    llist.printList();print()
