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
        self.parent = None

class BinaryTree:
    def __init__(self, Node):
        self.root = Node
    
    def add_element(self, Node):
        ptr = self.root
        count = 1
        while(ptr != None):
            if count%2 != 0:#Odd Case
                parent = ptr
                ptr = ptr.left
                if ptr == None:
                    ptr = Node
                    parent.left = ptr
                    ptr.parent = parent
                    return
                count = count + 1
            else:
                parent = ptr
                ptr = ptr.right
                if ptr == None:
                    ptr = Node
                    parent.right = ptr
                    ptr.parent = parent
                    return
                count = count + 1


    def pre_order(self, ptr):
        
        if ptr == None:
            return
        else:
            print(ptr.val)
            self.pre_order(ptr.left)
            self.pre_order(ptr.right)

        
    def in_order(self, ptr):
        
        if ptr == None:
            return
        else:
            self.pre_order(ptr.left)
            print(ptr.val)
            self.pre_order(ptr.right)


    def post_order(self, ptr):
        
        if ptr == None:
            return
        else:
            self.pre_order(ptr.left)
            self.pre_order(ptr.right)
            print(ptr.val)

class RBNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.color = None

class RedBlackTree(BinaryTree):
    #def __init__(self, Node): No Overriding init
    def __init__(self, RBNode):
        self.root = RBNode
        self.root.color = 'b'
        
    def left_rotate(x : RBNode):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
#%% Interval Tree

class IntervalNode:
    def __init__(self, low, high):
        self.right = None
        self.left = None
        self.parent = None
        self.low = low
        self.high = high
        self.max_val = self.high
        #self.max_val = max(self.high, self.right.max_val, self.left.max_val)
    
    
class IntervalTree:
    def __init__(self, node):
        self.root = node
        self.count = 0
    
    def add_interval(self, node):
        temp = 0
    
    def trav(self, node):
        
        if node == None:
            return
        else:
            self.trav(node.left)
            print("(%s, %s)" %(node.low, node.high) )
            self.trav(node.right)
        
    def check_overlap(self, int1, int2):
        low1, high1 = int1 # Home node
        low2, high2 = int2 # query node
        if low2 > low1 and low2<high1:
            return True
        elif high2< high1 and high2> low1:
            return True
        else:
            return False
        
        
    def search(self, low, high):
        ptr = self.root
        overlap = self.check_overlap( (self.root.low, self.root.high), (low, high) )
        if overlap:
            print("Interval overlaps")
            return
        else:
            print("Interval doesn't overlap")
            
        while( ptr != None):
            
            if low< ptr.low:
                ptr = ptr.left
            else:
                ptr = ptr.right
        
            
            
i = IntervalTree(IntervalNode(0,3))
i.trav(i.root)
i.search(1,2)
i.search(1,5)
i.search(-1,2)
i.search(6,8)
i = IntervalTree(IntervalNode(5,8))
    
        

#%% Trie Node
class TrieNode:
    def __init__(self, key):
        self.val = key
        self.children = [None]*26
        self.parent = None
        
class Trie():
    def __init__(self):
        self.root = TrieNode(0)
    
    def add_string(self, s):
        
        ptr = self.root
        l = len(s)
        for k in range(l):
            x = s[k]
            i = ord(x)-97
            #print(chr(i+97))
            if ptr.children[i] == None:
                ptr.children[i] = TrieNode(chr(i+97))
            ptr = ptr.children[i]            

    
    def trav(self, ptr):
        if ptr == None:
            return
        else:
            for i in range(26):
                self.trav(ptr.children[i])
    
    def search(self, s):
        ptr = self.root
        for x in s:
            i = ord(x)-97
            if ptr.children[i] != None:
                ptr = ptr.children[i]
            else:
                print("Not Present")
                return
        print("Present")
        return

t = Trie()
t.add_string('hello')
t.add_string('hey')
t.add_string('my')
t.add_string('name')
t.add_string('mukhil')

t.search('he')
    
        

#%%
btree = BinaryTree(Node(11))
for i in range(10,0,-1):
    btree.add_element(Node(i))
    
btree.pre_order(btree.root)
#%%

rbtree = RedBlackTree(RBNode(11))
rbtree.pre_order(rbtree.root)











