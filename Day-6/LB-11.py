# def countChar(s):
#     dict_char={}
#     for c in s:
#         if c not in dict_char:
#             dict_char[c]=1
#         else:
#             dict_char[c]+=1
#     return dict_char
# print(f'Total char is:{countChar('wiprobangalore')}')


def char_frequency(str1):
    
    dict = {}
    
    for n in str1:
        # Retrieve the keys (unique characters) in the 'dict' dictionary.
        keys = dict.keys()
        
        # Check if the character 'n' is already a key in the dictionary.
        if n in keys:
            # If 'n' is already a key, increment its value (frequency) by 1.
            dict[n] += 1
        else:
            # If 'n' is not a key, add it to the dictionary with a frequency of 1.
            dict[n] = 1
    
    # Return the dictionary containing the frequency of each character in the input string.
    return dict


print(char_frequency('doss'))