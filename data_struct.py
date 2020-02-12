#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %% Lists

l = [x for x in range(10)]
print(l)
l.append(10)
print(l)
l.pop()
print(l)
l.pop(0)
print(l)







#%% Strings



 


# %% Deque
'''
Double Ended Queue
Mainly used as Stacks and Queues

'''


from collections import deque


d = deque('abcdefghij')

print(d)

print(len(d))

d.append('k')
d.appendleft('z')
print(d)

d.pop()
d.popleft()
print(d)

# %% heapq

import heapq

def heapsort(iterable):
    h = []
    for i in iterable:
        heapq.heappush(h, i)
    return h
x=[9,8,7,6,5,4,3]

h = heapsort(x)
for i in range(len(h)):
    print(heapq.heappop(h))

# %% Binary Tree
    
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, Node):
        self.root = Node
    
    def add_element(self, Node):
        ptr = self.root
        count = 1
        while(ptr != None):
            if count%2 != 0:#Odd Case
                ptr = ptr.left
                count = count + 1
            else:
                ptr = ptr.right
                count = count + 1
            #print(count)
            #print(ptr)
            if ptr == None:
                ptr = Node
                return
    
    
btree = BinaryTree(Node(3))
btree.add_element(Node(4))















