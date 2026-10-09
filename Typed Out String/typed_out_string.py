#str1 = 'jskdab#h##g'
#str2 = 'jskdg'

str1 = 'ab#z'
str2 = 'az#z'

def is_same(str1,str2):

    str1_itr = len(str1)-1
    str2_itr = len(str2)-1
    skip_list = []

    is_same = True

    while (str1_itr >=0 and str2_itr >= 0):

        while str1[str1_itr] == '#' or  skip_list:
            if str1[str1_itr] == '#':
                skip_list.append('#')
            else:
                skip_list.pop()
            str1_itr -= 1
                        
        skip_list.clear()

        while str2[str2_itr] == '#' or skip_list:
            if str2[str2_itr] == '#':
                skip_list.append('#')
            else:
                skip_list.pop()
            str2_itr -= 1
                

        skip_list.clear()

        if str1[str1_itr] != str2[str2_itr]:
            is_same = False
            break
        else:
            str1_itr -= 1
            str2_itr -= 1
        
    #print(is_same)

    if str1_itr >= 0 or str2_itr >= 0:
        is_same = False
        
        
        
        
    return is_same


print(is_same(str1,str2))
        
