#!/usr/bin/python3

def pascal_triangle(number):
    ''' 
        returns a list of lists of integers representing
        the Pascal's triangle of n
    '''
    if (number <= 0):
        return []
    if (number == 1):
        return [1]
    lst = []
    for outer in range(number):
        if (outer == 0):
            lst.append([1])
        if (outer == 1):
            lst.append([1,1])
        tlst = []
        temp1 = outer
        temp2 = outer
        for x in range(0, temp1+1):
            y = x
            if (x == 0 or x == outer):
                tlst.append(1)
            else:
                tlst.append((lst[temp2-1][y-1]) + (lst[temp2-1][y+1]))
        lst.append(tlst)         


