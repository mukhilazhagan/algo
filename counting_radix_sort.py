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
    for j in ar[::-1]:
        ar_2[c[j]-1] = j
        c[j] = c[j]-1  # to take care of repetition
    return ar_2

def mod_counting_sort(ar, d, k):
    '''
    Parameters
    ----------
    ar : Array to be sorted.
    k : Range of Elements of ar .
    d : Digit to sort along

    Returns
    -------
    Array ar_2

    '''
    # print("Sorting Array:")
    # for i in range(len(ar)):
    #     print(ar[i][d])
    c = [0 for x in range(k+1)]
    for i in range(len(ar)):  # Count Freq
        c[ar[i][d]] = c[ar[i][d]]+1
    for i in range(1, len(c)):  # Running Sum
        c[i] = c[i]+c[i-1]
    ar_2 = [[0]*3 for x in range(len(ar))]
    #print(ar_2)
    
    for j in ar[::-1]:
        #print(j)
        #print(ar_2[c[j[d]]-1])
        ar_2[c[j[d]]-1] = j
        c[j[d]] = c[j[d]]-1  # to take care of repetition
    # print("Sorted Array:")
    # for i in range(len(ar_2)):
    #     print(ar_2[i][d])
    return ar_2


def radix_sort(ar, d , n):
    num_ar =[]
    for i in range(len(ar)):
        num_ar.append([int(digits) for digits in str(ar[i])])
    #print(len(num_ar))
    
    for i in range(3):
        num_ar = mod_counting_sort(num_ar, 2-i, n)
        # print("\nRecieved Array:", num_ar)
    #print(num_ar)
    return num_ar
    
        


#a = [2, 5, 3, 0, 2, 3, 0, 3]
a = [329, 457, 657, 839, 436, 720, 355] 
print("Original array:", a)
#print("Sorted Array:", counting_sort(a, 5))
ar = radix_sort( a, 3, 10)
print("Radix Sorted array:",ar)