#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%% Creating Vertex of a Graph

class Vertex:
    
    def __init__(self, key):
        self.id = key
        self.adj = {}
        
    def add_connection(self, v, weight = 0):
        self.adj[v] = weight
    
    def __str__(self):
        return "Vertex "+ str(self.id)+" Connected to vertices "+ str([x.id for x in
                                                             self.adj])
    
    def get_adj(self):
        return self.adj.keys
    
    def get_weight(self, v):
        return self.adj[v]
    

class Graph:
    def __init__(self):
        self.vertList={}
        self.num_vertices = 0
    
    def add_vertex(self, key):
        self.vertList[key] = Vertex(key)
        self.num_vertices = self.num_vertices + 1

    
    def get_vertex(self, v):
        if v in self.vertList:
            return self.vertList[v]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList
    
    def add_edge(self, f, t, weight =0):
        if f not in self.vertList:
            newv = self.add_vertex(f)
        if t not in self.vertList:
            newv = self.add_vertex(t)
        self.vertList[f].add_connection(self.vertList[t], weight)
    
    def get_vertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())




    
#%% Calling Graph
        
g = Graph()
for i in range(7):
    g.add_vertex(i)
print(g.vertList)
print(g.get_vertices())

g.add_edge(0,1,5)
g.add_edge(0,5,2)
g.add_edge(1,2,4)
g.add_edge(2,3,9)
g.add_edge(3,4,7)
g.add_edge(3,5,3)
g.add_edge(4,0,1)
g.add_edge(5,4,8)
g.add_edge(5,2,1)

print(g.get_vertices())

print("Printing Edges:")
for v in g:
    for nbr in v.adj:
        print("( %s, %s )" % (v.id, nbr.id) ) 
        
# %% BFS
 
from collections import deque


def bfs(g, root, sink):
    #print(g.vertList)
    visited = {}
    q = deque()
    q.appendleft(root)
    #for i in root.adj:
    #   print(i.id)
    while len(q) != 0:
        ptr = q.pop()
        visited[ptr] = 1
        
        for i in ptr.adj:
            if i not in visited:
                q.appendleft(i)
            if i == sink:
                print("Found")
                return
    print("Not found")
    return

def dfs(g, root, sink):
    visited = {}
    q = deque()
    q.append(root)
    #for i in root.adj:
    #   print(i.id)
    while len(q) != 0:
        ptr = q.pop()
        visited[ptr] = 1 
        for i in ptr.adj:
            if i not in visited:
                q.appendleft(i)
            if i == sink:
                print("Found")
                return
    print("Not found")
    return        
    
print("BFS check for vertex 0 and vertex 6")
bfs(g, g.get_vertex(1), g.get_vertex(0))
bfs(g, g.get_vertex(1), g.get_vertex(6))
    
print("DFS check for vertex 0 and vertex 6")
dfs(g, g.get_vertex(1), g.get_vertex(0))
dfs(g, g.get_vertex(1), g.get_vertex(6))

## For Graph Traversal

#%% DFS With Discovery and Finishing times

class Vertex:
    
    def __init__(self, key):
        self.id = key
        self.val = float('inf')
        self.parent = None
        self.color = 'w'
        self.dtime = 0
        self.ftime = 0
        self.adj = {}
        
    def add_connection(self, v, weight = 0):
        self.adj[v] = weight
    
    def __str__(self):
        return "Vertex "+ str(self.id)+" Connected to vertices "+ str([x.id for x in
                                                             self.adj])
    
    def get_adj(self):
        return self.adj.keys
    
    def get_weight(self, v):
        return self.adj[v]


class Graph:
    def __init__(self):
        self.vertList={}
        self.num_vertices = 0
    
    def add_vertex(self, key):
        self.vertList[key] = Vertex(key)
        self.num_vertices = self.num_vertices + 1

    
    def get_vertex(self, v):
        if v in self.vertList:
            return self.vertList[v]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList
    
    def add_edge(self, f, t, weight =0):
        if f not in self.vertList:
            newv = self.add_vertex(f)
        if t not in self.vertList:
            newv = self.add_vertex(t)
        self.vertList[f].add_connection(self.vertList[t], weight)
    
    def get_vertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())

'''
g = Graph()
for i in range(7):
    g.add_vertex(i)
#print(g.vertList)
#print(g.get_vertices())

g.add_edge(0,1,5)
g.add_edge(0,5,2)
g.add_edge(1,2,4)
g.add_edge(2,3,9)
g.add_edge(3,4,7)
g.add_edge(3,5,3)
g.add_edge(4,0,1)
g.add_edge(5,4,8)
g.add_edge(5,2,1)
'''

top_sort = []

def get_time():
    global time
    time = time+1
    return time
def dfs(g):
    vert =[x for x in g.get_vertices()]
    q = deque()
    global time
    time = 0
    
    for v in vert:
        v = g.get_vertex(v)
        if v.color == 'w':
            q.append(v)
            v.dtime = get_time()
        while len(q) != 0:
            ptr = q.pop()
            ptr.color = 'g' 
            for i in ptr.adj:
                if i.color == 'w':
                    q.append(i)
                    i.color = 'g'
                    i.dtime = get_time()
                    i.parent = ptr
            ptr.color = 'b'
            ptr.ftime = get_time()
            top_sort.append(ptr.id)
  

g = Graph()
g.add_edge('undershorts','pants')
g.add_edge('undershorts','shoes')
g.add_edge('pants','belt')
g.add_edge('pants','shoes')
g.add_edge('socks','shoes')
g.add_edge('shirt','belt')
g.add_edge('belt','jacket')
g.add_edge('shirt','tie')
g.add_edge('tie','jacket')
g.add_vertex('watch')



                            
dfs(g)

#for i in g.vertList:
#   i = g.get_vertex(i)
#   print("for vertex %s ,the finishing time is %s " % (i.id, i.ftime) )

print(top_sort)   


#%% Kruskal MST


#for v in g.get_vertices():
 
#Prims MST

g = Graph()
g.add_edge('a','b',4)
g.add_edge('b','a',4)
g.add_edge('a','h',8)
g.add_edge('h','a',8)
g.add_edge('b','c',8)
g.add_edge('c','b',8)
g.add_edge('b','h',11)
g.add_edge('h','c',11)
g.add_edge('c','d',7)
g.add_edge('d','c',7)
g.add_edge('c','i',2)
g.add_edge('i','c',2)
g.add_edge('c','f',4)
g.add_edge('f','c',4)
g.add_edge('d','e',9)
g.add_edge('e','d',9)
g.add_edge('d','f',14)
g.add_edge('f','d',14)
g.add_edge('e','f',10)
g.add_edge('f','e',10)
g.add_edge('f','g',2)
g.add_edge('g','f',2)
g.add_edge('g','i',6)
g.add_edge('i','g',6)
g.add_edge('g','h',1)
g.add_edge('h','g',1)



import heapq

h = []
heapq.heapify(h)

root = g.get_vertex('a')
root.val = 0

for i in g.vertList:
    #print(i)
    heapq.heappush(h,i)

#print(h)
while ( len(h) > 0):
    u = heapq.heappop(h)
    u = g.get_vertex(u)
    for v in u.adj:
        #print(u.adj[v])
        #print(v.id)
        if( v.id in h and v.val > u.adj[v]):
            v.val = u.adj[v]
            v.parent = u






  








