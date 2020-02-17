#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#n = 4
#max_cap = 8

n = 3
max_cap = 50

#val = [15,10,9,5]
#w =[1, 5, 3, 4]
val = [60, 100, 120]
w =[10, 20, 30]

#v_w =[ v/w for v,w in zip(val,weight)]
#print(v_w)
#v_w.sort(reverse = True)

#tab = [[0]*(max_cap+1)]*(len(val)+1) # This creates clones of list, doesnt work

# Only this works
tab = [[0 for x in range( max_cap+1 )] for x in range( len(val)+1) ]

for i in range(1, ( len(val)+1) ):
    for j in range(1, (max_cap+1) ):
        tab[i][j] = max( tab[i-1][j] , val[i-1] + tab[i-1][ max(0,j-w[i-1])] )
print(tab)        