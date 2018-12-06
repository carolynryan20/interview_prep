'''
Quick sort algorithm for sorting a list
O(nlogn)
'''

def make_wall(L, left, right):
    pivot_value = L[left]
    first = left

    left += 1
    while left <= right:
        while left <= right and L[left] <= pivot_value:
            left += 1
        while right >= left and L[right] >= pivot_value:
            right -= 1

        if left < right:
            temp = L[left]
            L[left] = L[right]
            L[right] = temp


    L[first] = L[right]
    L[right] = pivot_value

    return right

def quick_sort(L, left, right):
    if left >= right:
        return

    split = make_wall(L, left, right)
    print(L, split)
    quick_sort(L, left, split-1)
    quick_sort(L, split+1, right)

def main():
    L = [9,5,2,1,9,6,7,10,100,45,-3]
    quick_sort(L, 0, len(L)-1)
    print(L)

main()