def fiddle_lists(a_list1, a_list2):
    a_list1 = [1, 5]
    a_list1.append(10)
    a_list2.append(10)

def main():
    list1 = [5, 3, 2]
    list2 = [4, 6, 2]
    fiddle_lists(list1, list2)
    print("1:", list1)
    print("2:", list2)

main()