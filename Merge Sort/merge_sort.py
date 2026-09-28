arr1 = [4,2,6,5,1,8,0,9]

def merge(left_arr,right_arr):

    merged_sorted_lst = []
    left_itr = 0
    right_itr = 0

    while left_itr < len(left_arr) and right_itr < len(right_arr):

        if left_arr[left_itr] < right_arr[right_itr]:
            merged_sorted_lst.append(left_arr[left_itr])
            left_itr += 1
            continue

        elif left_arr[left_itr] > right_arr[right_itr]:
            merged_sorted_lst.append(right_arr[right_itr])
            right_itr += 1
            continue

    merged_sorted_lst.extend(left_arr[left_itr:])
    merged_sorted_lst.extend(right_arr[right_itr:])

    return merged_sorted_lst


def merge_sort(arr1):

    if len(arr1) <= 1:
        return arr1

    arr_length = len(arr1)
    mid_pt = int(arr_length/2)
    
    left_arr = merge_sort(arr1[0:mid_pt])
    right_arr = merge_sort(arr1[mid_pt:arr_length])

    return merge(left_arr,right_arr)




if __name__ == '__main__':
    print(f'Original:{arr1}')
    sorted_arr = merge_sort(arr1)
    print(f'Sorted:{sorted_arr}')
