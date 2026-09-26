#Problem statement
#You will be given a list of integer and a target value. Need to find if there are any pair of number whose sum is the target value

arr1 = [2,4,5,6,7]
arr2 = [3,7,9]
target_value = 16


def two_sum(arr1,target_sum):

    compl_set = set()

    for num in arr1:

        if num in compl_set:
            return True

        compl_set.add(target_sum-num)
        

    return False



print(two_sum(arr1,target_value))
