#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Representing Heap as an array


class Heap:
    def __init__(self):
        self.heaplist=[]
        self.heapsize=0

    def parent(self, i):
        return i//2

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i+1

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l <= self.heapsize and self.heaplist[i] > self.heaplist[l]:
            self.heaplist[i], self.heaplist[l] = self.heaplist[l], self.heaplist[i]
            self.heapify(l)
        elif r <= self.heapsize and self.heaplist[i] > self.heaplist[r]:
            self.heaplist[i], self.heaplist[r] = self.heaplist[r], self.heaplist[i]
            self.heapify(r)

    def insert(self, x):
        self.heaplist.insert(0,x)
        self.heapify(0)
        self.heapsize = self.heapsize + 1

    def extract_min(self):
        if self.heapsize == 0:
            print(" Heap Empty")
            return
        self.heapsize = self.heapsize - 1
        return self.heaplist.pop(0)
        
        
    def printheap(self):
        print([x for x in self.heaplist])



h = Heap()
for i in range(11,0,-1):
    h.insert(i)

h.printheap()
