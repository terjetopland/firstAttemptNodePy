# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

class node:
    def __init__ (self, data = None):
        self.data = data
        self.next = None
    
class linked_list :
    def __init__(self):
        self.head = node()
        
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print (elems)
        
    def get(self, index):
        if index>=self.length():
            print ("ERROR: Get index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            if cur_index==index:
                return cur_node.data
            cur_index+=1
        
    def erase(self, index):
        if index>=self.length():
            print("ERROR: Erase index out of range!")
            return
        cur_index = 0
        cur_node = self.head
        while cur_node.next!=None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index==index:
                last_node.next = cur_node.next
                print("Erased index " + str(cur_index))
                return 
            cur_index+=1
                
            
my_list = linked_list()

my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()

length = str(my_list.length())

print ("lenght of the list is " + length)

print ("Data at index 2 is " + str(my_list.get(2)))

my_list.erase(1)

my_list.display()

print("Length of my_list is now " + str(my_list.length()))