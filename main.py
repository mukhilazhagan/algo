import sort

## Sort Tests:

def main():
    s = sort.Sort()
    orig_array = [10, 9, 13, 2, 5, 3, 6, 1, 9, 7]
    print("Orignal array: ", orig_array)

    ar = orig_array.copy()
    print("Bubble sort: ", s.bubble_sort(ar))
    print("Insertion sort desc: ", s.insertion_sort(ar))
    print("Selection sort: ", s.selection_sort(ar))
    print("Merge sort: ", s.merge_sort(ar))

if __name__ == '__main__':
    main()
