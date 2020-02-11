import copy

class Sort:
    def __init__(self):
	    self.desc = " Class for Sorting"

    def __str__(self):
        return self.desc
        	
    def bubble_sort(self, ar):
        length = len(ar)
        for i in range(length):
            for j in range(i+1, length):
                if ar[i] > ar[j]:
                    ar[i], ar[j] = ar[j], ar[i]
        return ar

    def insertion_sort(self, ar):
        ## Sorts in Descending
        length = len(ar)
        for j in range(1, length):
            key = j-1			
            while key>=0 and ar[key+1] > ar[key] :
                ar[key+1], ar[key] = ar[key], ar[key+1]								
                key = key-1
        return ar

    def merge_sort(self, ar):
        length = len(ar)
        mid = length//2 # ciel of length/2
        if length == 1:
            return ar
        
        a1 = self.merge_sort(ar[:mid])
        a2 = self.merge_sort(ar[mid:length])
        a = []
        
        i,j = 0,0
        while True:
            if i == len(a1) :
                a = a + a2[j:]
                break
            if j == len(a2) :
                a = a+ a1[i:]
                break
            if a1[i] < a2[j]:
                a.append(a1[i])
                i = i+1
            else:
                a.append(a2[j])
                j = j+1
                
        return a
        
    
    def selection_sort(self, ar):
        length = len(ar)
        for i in range(length):
            min_val, arg_min = float('inf'), 0
            for j in range(i, length):
                if ar[j] < min_val:
                    min_val = ar[j]
                    arg_min = j
            ar[arg_min] =  ar[i]
            ar[i] = min_val
        return ar
    

def debug():
    ## Broken for User Input
    s = Sort()
    i = input("Do you want to input an array to be sorted: Y/N \n")
    if i == 'Y':
        orig_array = list(input("Input Array in form x,y,z...: \n").split(","))
        print('Original array: ', orig_array)
    elif i == 'N':
        orig_array = [10, 9, 13, 2, 5, 3, 6, 1, 9, 7]
        print("Orignal array: ", orig_array)

    ar = copy.deepcopy(orig_array)
    print("Bubble sort: ", s.bubble_sort(ar))
    ar = copy.deepcopy(orig_array)
    print("Selection sort desc: ", s.insertion_sort(ar))
    
if __name__ == '__main__':
    debug()
