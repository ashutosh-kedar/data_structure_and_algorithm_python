values = [0,1,0,2,1,0,3,1,0,1,2]


def find_trapped_rain_water(values):

    left_itr = 0
    right_itr = len(values)-1
    
    left_max = values[left_itr]
    right_max = values[right_itr]

    water = 0

    while(not left_itr >= right_itr):

        left_element = values[left_itr]
        right_element = values[right_itr]

        if left_element > right_element:
            if right_element < right_max:
                 water += (right_max - right_element)
            else:
                right_max = right_element
            right_itr -= 1
        else:
            if left_element > left_max:
                left_max = left_element
            else:
                water += (left_max-left_element)
            left_itr += 1

    return water
        
    

print(find_trapped_rain_water(values))
        
