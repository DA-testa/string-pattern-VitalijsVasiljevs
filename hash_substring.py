# Vitalijs Vasiljevs 3. grupa , 221RDB265 
import re
hashMap = {}
def read_input():
    mode = input()  
    if ((re.sub("[\r\n]", "", mode) == "I")) :
        return (input().rstrip(), input().rstrip())                
    elif (re.sub("[\r\n]", "", mode) == "F") : 
        file_name = "tests/06" 
        with open(file_name, 'r') as f:
            lines = f.readlines()
        return(re.sub("[\n]", "", lines[0]), lines[1])   
    pass

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    list = []
    i = 0
    if len(pattern) > len(text):
        return ""
    for char in text:
        if char.isdigit():
            hashMap[char] = int(char)
        if not char in hashMap:
            hashMap[char] = 10+i
            i = i + 1
    start_index = 0
    end_index = len(pattern)
    pattern_value = get_value(pattern)
    if pattern_value == "":
        return []
    substring_value = get_value(text[start_index:end_index])
    for i in range(len(text)-len(pattern)+1):
        if pattern_value == substring_value:
            list.append(start_index)
        if end_index == len(text):
            return list
        start_char_value = hashMap[text[start_index]] * 10**(len(pattern)-1)
        end_index = end_index + 1
        start_index = start_index + 1
        substring_value = (substring_value - start_char_value) * 10 + hashMap[text[end_index-1]]
    return list

def get_value(pattern):
    value = 0
    len_of_pattern = len(pattern) - 1
    i = 0
    for char in pattern:
        if not char in hashMap:
            return ""
        value = value + hashMap[char] * 10**(len_of_pattern-i)
        i = i + 1
    return value
    
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
