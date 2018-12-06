'''
Binary search
O(logn)
'''

def binarysearch(L, item):
    _binarysearch(L, item, 0, len(L)-1)

def _binarysearch(L, item, left, right):
    if left > right:
        return None

    middle = (right-left)//2 + left

    print(left, right, middle)
    midpoint = L[middle]
    if midpoint == item:
        return item
    elif midpoint > item:
        _binarysearch(L, item, left, middle)
    else:
        _binarysearch(L, item, middle, right)

def main():
    L = [1,3,5,7,9]
    print(binarysearch(L, 5))
    print(binarysearch(L,2))

main()