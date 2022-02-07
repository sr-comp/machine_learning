
def find_num(my_list):
    my_dict = {}
    for item in my_list:
        try:
            my_dict[item] += 1
        except KeyError:
            my_dict[item] = 1

    return my_dict

my_list = [1, 2, 3, 2, 3, 1, 4, 2, 4]
nums = find_num(my_list)
print(nums)