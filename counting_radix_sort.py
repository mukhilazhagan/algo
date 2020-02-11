#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def counting_sort(ar, k):
    '''
    Parameters
    ----------
    ar : Array to be sorted.
    k : Range of Elements of ar .

    Returns
    -------
    Array ar_2

    '''
    c = [0 for x in range(k+1)]
    for i in ar:  # Count Freq
        c[i] = c[i]+1
    for i in range(1, len(c)):  # Running Sum
        c[i] = c[i]+c[i-1]
    ar_2 = [0 for x in range(len(ar))]
    for j in ar:
        ar_2[c[j]-1] = j
        c[j] = c[j]-1  # to take care of repetition
    return ar_2
    
    

a = [2, 5, 3, 0, 2, 3, 0, 3]
print("Original array:", a)
print("Sorted Array:", counting_sort(a, 5))