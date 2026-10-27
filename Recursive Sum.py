def r_sum(nested_num_list):
    tot = 0
    
    #fill in the missing code
    
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
            
    return tot

L1 = [1, 10, 9, [3, 5, 7], [5, [6, 7], 97]]
print(r_sum(L1))
