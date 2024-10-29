def sum(alist):
    # sums elements of a list
    out = 0
    out_str = ""
    if len(alist) <= 1:
        out += alist[0]
        out_str += f"0 + {alist[0]} = {out}"
        print(out_str)
    else: 
        out = alist[0] + sum(alist[1:])
        out_str += f"  + {alist[0]} = {out}"
        print(out_str)
    return out
    

def sort(alist):
    # uses bubble sort
    print("\n====== SORTING ======")
    for i in range(1, len(alist)):
        swap = False
        for j in range(0, len(alist)-1):
            if alist[j] > alist[j+1]:
                swap = True
                print(f"Swapping {alist[j]} and {alist[j+1]}: ", end ="")
                alist[j], alist[j+1] = alist[j+1], alist[j]
                print(alist)
            else: print("No swap occurred:  ", alist)
        if swap: print(f"List after Pass {i}:  {alist}\n")
    print("List fully sorted")
    return alist

def search (alist, item):
    # uses binary search
    print("\n====== SEARCHING ======")
    first = 0
    last = len(alist)
    found = False
    i = 0
    while first <= last and not found:
        i+=1
        print("\nCOMPARISON #", i)
        mid = (first+last)//2
        print("Search space: ", alist[first:last+1])
        print("Middle element: ", alist[mid])
        if alist[mid] == item: found = True
        else:
            if alist[mid] < item: first = mid+1
            else: last = mid-1
            print("New search space: ", alist[first:last+1])
    if found: print(item, "is in the collection")
    else: print(item, "is not in the collection")

def main():
    numbers = [22, 15, 63, 56, 62, 14, 84, 42, 41]
    print("Starting list: ", numbers)
    print("===== SUMMING =====")
    print("-------------------\nResult:", sum(numbers))
    sort(numbers)
    search(numbers, 56)

if __name__ == "__main__":
    main()
        