input_str = "aaeebb"

def get_first_uniq_char(input_param):
    data_dict = dict()
    ret_val = -1
    
    for ch in range(len(input_param)):
        if input_param[ch] in data_dict:
            data_dict[input_param[ch]] = -1
        else:
            data_dict[input_param[ch]] = ch
            
    print (data_dict)

    for ch in range(len(input_param)):
        if data_dict[input_param[ch]] != -1:
            return ch
    
    return ret_val
            
print(get_first_uniq_char(input_str))            