'''
Merge sort algorithm
O(nlogn)
'''
def merge(l1, l2):
    l1_index = 0
    l2_index = 0
    k = 0
    merged_list = [None] * len(l1+l2)
    while l1_index < len(l1) and l2_index < len(l2):
        if l1[l1_index] < l2[l2_index]:
            merged_list[k] = l1[l1_index]
            l1_index += 1
        else:
            merged_list[k] = l2[l2_index]
            l2_index += 1
        k += 1

    while l1_index < len(l1):
        merged_list[k] = l1[l1_index]
        l1_index += 1
        k += 1

    while l2_index < len(l2):
        merged_list[k] = l2[l2_index]
        l2_index += 1
        k += 1

    return merged_list


def merge_sort(L):
    list_length = len(L)
    if list_length == 0 or list_length == 1:
        return L

    l1 = L[:list_length//2]
    l2 = L[list_length//2:]
    sorted_l1 = merge_sort(l1)
    sorted_l2 = merge_sort(l2)

    sorted_accum = merge(sorted_l1, sorted_l2)
    return sorted_accum

def main():
    L = [9,5,2,1,9,6,7,10,100,45,-3]
    print(merge_sort(L))

if __name__ == '__main__':
    main()

