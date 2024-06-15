input_str = "http://samplesite.com/ go to new page"


#find number of spaces
def count_spaces(input_param):
    space_count = 0
    for ch in input_param:
        if ch.isspace():
            space_count += 1
    return space_count



    
# space_count = count_spaces(input_str)

# revised_str_length = len(input_str) + space_count*2
 
# print("input_str length ", len(input_str)) 
# print ("space_count ", space_count) 
# print("revised_str_length ", revised_str_length)

# split the string into list of characters and join using %20
# split() method splits a string into a list. You can specify the separator, default separator is any whitespace.
def urlify1(in_string):
    return "%20".join(in_string.split())

#using string replace method. the string slicing has no impact. we get same output with or without slicing
# this gives best performance
def urlify2(in_string):
    in_string_length = len(in_string)   
    return in_string[:in_string_length].replace(' ', '%20')

# we are using list comprehension to iterate over the string and replace space with %20
# we are avoiding the use of string split and join   
def urlify3(in_string):
    in_string_length = len(in_string) 
    return ''.join('%20' if c == ' ' else c for c in in_string[:in_string_length])
    
def urlify(input_param):
    spaces_count = count_spaces(input_param)
    input_str_length = len(input_str)
    revised_str_length = len(input_str) + spaces_count*2    
  
    input_data_list =  [''] * revised_str_length
    new_index = revised_str_length - 1
    for i in reversed(range(0, input_str_length)):
        
        ch = input_param[i]
        if ch.isspace():
            input_data_list[new_index] = '0'
            input_data_list[new_index-1] = '2'
            input_data_list[new_index-2] = '%'
            new_index = new_index - 3 
        else:
            input_data_list[new_index] = ch
            new_index -= 1
    # print (input_param)
    return "".join(input_data_list)
    # print (len ("".join(input_data_list)))

# print(urlify(input_str, space_count))
# print(urlify1(input_str))
# print(urlify2(input_str))
# print(urlify3(input_str))

import timeit

print(timeit.timeit("urlify1(input_str)", globals=globals()))
print(timeit.timeit("urlify2(input_str)", globals=globals()))
print(timeit.timeit("urlify3(input_str)", globals=globals()))
print(timeit.timeit("urlify(input_str)", globals=globals()))
# print(timeit.timeit('[func(input_str) for func in (urlify,urlify1,urlify2, urlify3)]', globals=globals()))