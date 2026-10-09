data = 'abcbde'
#data = 'abcccde'
#data = 'abcbdaac'



def get_largest_substring(data):

    unique_set = set()
    right_ptr = 0
    left_ptr = 0
    max_length = 0

    while(right_ptr < len(data)):

        while data[right_ptr] in unique_set:
            unique_set.remove(data[left_ptr])
            left_ptr += 1


        unique_set.add(data[right_ptr])


        max_length =  max(max_length,len(unique_set))
        
        right_ptr += 1

    return max_length
          

    






print(get_largest_substring(data))
