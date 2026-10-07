lst = [1,8,6,2,9,4]



def containerWithMostWater(lst):
    left_idx = 0
    right_idx = len(lst)-1
    max_water = 0

    while (left_idx < right_idx):
        left_element = lst[left_idx]
        right_element = lst[right_idx]
        
        if left_element < right_element:
            max_water = max(max_water,(left_element*(right_idx-left_idx)))
            left_idx += 1
        else:
            max_water = max(max_water,(right_element*(right_idx-left_idx)))
            right_idx -= 1


    return max_water




print(containerWithMostWater(lst))
