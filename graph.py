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
        return "Vertex"+ str(self.id)+" Connected to vertices "+ str([x.id for x in
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
for i in range(6):
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


















