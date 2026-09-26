lst1 = [1,5,12,18,34]
lst2 = [3,15,21,29]





def merge_2_sorted_list(lst1,lst2):
    lst1.extend(lst2)
    lst1.sort()
    return lst1

# this is supress the duplicates
def merge_2_sorted_list2(lst1,lst2):
    lst1_idx = 0
    lst2_idx = 0
    merged_sorted_list = list()
    
    while lst1_idx < len(lst1) and lst2_idx < len(lst2):
        if lst1[lst1_idx] < lst2[lst2_idx]:
            merged_sorted_list.append(lst1[lst1_idx])
            lst1_idx += 1
        elif lst1[lst1_idx] > lst2[lst2_idx]:
            merged_sorted_list.append(lst2[lst2_idx])
            lst2_idx += 1
        else:
            merged_sorted_list.append(lst2[lst2_idx])
            lst2_idx += 1
            lst1_idx += 1


    while lst1_idx < len(lst1):
        merged_sorted_list.append(lst1[lst1_idx])
        lst1_idx += 1

    while lst2_idx < len(lst2):
        merged_sorted_list.append(lst2[lst2_idx])
        lst2_idx += 1
            
    return merged_sorted_list

# preserves the duplicate
def merge_2_sorted_list3(lst1,lst2):
    lst1_idx = 0
    lst2_idx = 0
    merged_sorted_list = list()
    
    while lst1_idx < len(lst1) and lst2_idx < len(lst2):
        if lst1[lst1_idx] <= lst2[lst2_idx]:
            merged_sorted_list.append(lst1[lst1_idx])
            lst1_idx += 1
        else:
            merged_sorted_list.append(lst2[lst2_idx])
            lst2_idx += 1


    while lst1_idx < len(lst1):
        merged_sorted_list.append(lst1[lst1_idx])
        lst1_idx += 1

    while lst2_idx < len(lst2):
        merged_sorted_list.append(lst2[lst2_idx])
        lst2_idx += 1
            
    return merged_sorted_list



marged_list = merge_2_sorted_list3(lst1,lst2)




print(f'Merged List:{marged_list}')
