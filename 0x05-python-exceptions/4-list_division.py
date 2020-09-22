#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    n_list = []
    for a in range(list_length):
        try:
            count = my_list_1[a] / my_list_2[a]
        except (ValueError, TypeError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            n_list.append(count)
    return n_list
