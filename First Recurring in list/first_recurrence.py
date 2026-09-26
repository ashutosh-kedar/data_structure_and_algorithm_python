arr1 = [0,1,3,5,6,7,1]

arr2 = [0,1,3,4,5,5,1,7]


def first_recurrence(arr1):
    unique_ele = set()
    for item in arr1:
        if item in unique_ele:
            return item
        unique_ele.add(item)

    return None


# here arr2 = [0,1,3,4,5,5,1,7]
# this approach will give 5 as above. simple O(n^2) approach will give 1
def first_recurrence2(arr1):
    print(arr1)
    
    
    for i in range(len(arr1)):
        duplicate_items = set()
        
        for j in range (i+1,len(arr1)):
            if arr1[j] in duplicate_items:
                return arr1[j]
            
            duplicate_items.add(arr1[j])
            
            if arr1[i] == arr1[j]:
                return arr1[i]
            
    return None    




first_recurrence_value = first_recurrence2(arr2)

print(f'First recurrence:{first_recurrence_value}')
