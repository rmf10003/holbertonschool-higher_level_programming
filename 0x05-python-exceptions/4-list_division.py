#!/usr/bin/python3
def list_division(l1, l2, length):
    newList = []
    result = 0
    for i in range(0, length):
        try:
            result = l1[i] / l2[i]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            newList.append(result)
            result = 0
    return newList
