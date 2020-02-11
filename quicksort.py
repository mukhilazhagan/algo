#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Sort in Place , Worst case: O(n^2) , Best,Avg case: O(n lgn)

def quicksort(ar, p, r): # p = first element , r = last element inclusive
    
    if p < r:
        q = partition(ar, p, r)
        quicksort(ar, p, q-1)
        quicksort(ar, q+1, r)

def partition(ar, p, r):
    
    print("\nPartioning array:",ar[p:r+1])
    ## Returns a pivot q , where all elements q-1 are <= q & all elements q+1 are >q
    x = ar[r] # points to last element , to be pivot by end of function
    i = p-1 # points to before the first element
    
    ## i tracks are elements < q , while j tracks all elements > q
    for j in range(p, r): # to be inclusive of all elements < r
        if ar[j] <= x:
            i = i+1
            ar[i], ar[j] = ar[j], ar[i] # swapping elements
        
    ar[i+1],ar[r]= ar[r], ar[i+1]
    print("Found pivot:",ar[i+1])
    print("Partioned array:",ar[p:r+1])
    return i+1


a = [2,8,7,1,-193,5,6,4,-1,37,0,48]
quicksort(a, 0, len(a)-1)
print("Sorted Array:",a)

            
    

