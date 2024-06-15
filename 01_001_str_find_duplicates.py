input = "duplicatedstring"
# input = "no_duplicates"
# input = u"నేను అను సర్వనామము"

#encoding the input string from unicode to utf-8
# input = input.encode('utf-32')



# creating empty set - to check if the character is already present
chars_set = set()

def has_duplicates(input_str):
    for char in input_str:
        if char in chars_set:
            print("Duplicate found ")
            return
        else:
            chars_set.add(char)
    print("No duplicates found")
        
# creating a dictionary to store the characters with their count
char_dict = dict()

def find_duplicates_count(input_str):
    for char in input_str:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    # print dictionary if the value is greater than 1
    for key, value in char_dict.items():
        if value > 1:
            print(key, value)
    
    # if dictionary has no value greater than 1, print no duplicates found
    if not any(value > 1 for value in char_dict.values()):
        print("No duplicates found 1")

    if all(i < 2 for i in char_dict.values()):
        print("No duplicates found 2")
    



has_duplicates(input)      
find_duplicates_count(input)  