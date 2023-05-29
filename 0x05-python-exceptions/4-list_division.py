#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        divide = 0
        try:
            divide = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except (ZeroDivisionError, ValueError):
            print("divion by 0")
        except IndexError:
            print("out of range")
        finally:
            res.append(divide)

    return res
