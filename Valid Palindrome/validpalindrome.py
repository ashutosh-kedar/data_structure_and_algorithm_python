##data = 'asaasasf'


##def valid_palindrome(data):
##    if len(data) <= 1:
##        return True
##
##    reversed_data = list(data)
##    reversed_data.reverse()
##    return data == ''.join(reversed_data)





##def valid_palindrome(data):
##
##    if len(data) <= 1:
##        return True
##
##    right_ptr = len(data)-1
##    left_ptr = 0
##
##    while left_ptr != right_ptr and left_ptr < right_ptr:
##
##        if data[left_ptr] !=  data[right_ptr]:
##            return False
##
##        left_ptr += 1
##        right_ptr -= 1
##
##    return True



data = "abcdefdba" -> False
##data = 'abccdba' -> True


def valid_palindrome(data,left_ptr,right_ptr,is_remove=True):

    if len(data) <= 1:
        return True

    invalid_palindrome = False

    while left_ptr != right_ptr and left_ptr < right_ptr:

        if data[left_ptr] != data[right_ptr]:
            invalid_palindrome = True
            break

        right_ptr -= 1
        left_ptr += 1


    if invalid_palindrome:
        if is_remove:
            return valid_palindrome(data,left_ptr+1,right_ptr,is_remove=False) or valid_palindrome(data,left_ptr,right_ptr-1,is_remove=False)
        else:
            return False
    else:
        return True




print(valid_palindrome(data,0,len(data)-1))
