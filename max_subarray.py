import operator

prices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
change = list( map( operator.sub ,prices[1:], prices[:-1]) )
sz = len(change)
#print(change)


def max_crossing_subarray(ar ,l ,r ,mid):
    sz = len(ar[l:r+1])
    sum, max_sum =0, 0
    l_end = mid
    r_end = mid
    for i in range(mid-1,l-1,-1):
        sum = ar[i]+ sum
        if sum >= max_sum :
            max_sum = sum
            l_end = i
    l_sum = max_sum


    sum, max_sum = 0, 0
    for i in range(mid,r+1):
        sum = ar[i]+ sum
        if sum >= max_sum:
            max_sum = sum
            r_end = i
    r_sum = max_sum

    tot_sum = l_sum+r_sum
    return l_end, r_end, tot_sum
        
    



def max_subarray(ar, l, r):
    #sz = len(ar[l:r+1]) # including l and r
    mid = (l+r+1)//2
    
    if l == r:
        return l, r, ar[l]
    
    #print("size:",sz)
    print("array:" ,ar[l:r+1])
    print("mid:",mid)
    print("l:",l)
    print("r:",r)
    print("---")
    
    l_end1, l_end2, l_sum = max_subarray(ar, l, mid-1)
    c_end1, c_end2, c_sum = max_crossing_subarray(ar, l, r, mid)
    r_end1, r_end2, r_sum = max_subarray(ar, mid, r)
    
    t1 = max([ l_sum, r_sum, c_sum])
    t2 = [ l_sum, r_sum, c_sum].index(t1)
    
    if t2 == 0:
        end1, end2, max_sum = l_end1, l_end2, l_sum
    if t2 == 1:
        end1, end2, max_sum = r_end1, r_end2, r_sum
    if t2 == 2:
        end1, end2, max_sum = c_end1, c_end2, c_sum

    print("max_sum:", max_sum)
    print("l_end:",end1," r_end:", end2)
    return end1, end2, max_sum

e1, e2, val = max_subarray(change,0, sz-1)
print(change[e1:e2+1], val)

# [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
