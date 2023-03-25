def pack_duplicates(lst):
    # Initialize variables
    result = []
    current_group = []

    # Iterate over the list
    for i in lst:
        if not current_group or current_group[-1] == i:
            current_group.append(i)
        else:
            result.append(current_group)
            current_group = [i]

    # Append the last group to the result
    if current_group:
        result.append(current_group)

    return result

my_list = [0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]
packed_list = pack_duplicates(my_list)
print( "After packing consecutive duplicates of the saaid list elements into s.lists is",packed_list)
