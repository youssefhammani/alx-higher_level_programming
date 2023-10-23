#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            division_result = 0

            if i < len(my_list_1) and i < len(my_list_2):
                if (
                    isinstance(my_list_1[i], (int, float))
                    and isinstance(my_list_2[i], (int, float))
                    and my_list_2[i] != 0
                ):
                    division_result = my_list_1[i] / my_list_2[i]
                elif (
                    not isinstance(my_list_1[i], (int, float))
                    or not isinstance(my_list_2[i], (int, float))
                ):
                    print("wrong type")
                elif my_list_2[i] == 0:
                    print("division by 0")
            else:
                print("out of range")

            result.append(division_result)
        except ZeroDivisionError:
            result.append(0)

    return result
