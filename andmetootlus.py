my_list =["abc","123","456","def"]

def only_numbers(str_list):
    result = []
    for string in str_list:
        if string.isdigit():
            result.append(string)
    return result

result = only_numbers(my_list)
print(result)