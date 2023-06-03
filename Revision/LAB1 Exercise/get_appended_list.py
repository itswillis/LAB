def get_appended_list(numbers, value):
    list = []
    for number in numbers:
        list.append(number)
    list.append(value)
    return (list)

source_list2 = [1,2,3]
print("before", source_list2)
print("after")
target_list = get_appended_list(source_list2, 4)
print("source", source_list2)
print("target", target_list)
