''' Next Link - Clark Brown - 2019

Utils: functions used through out various parts of the program
'''

def intersect(A, B):
    ''' Returns the intersection of two lists A and B (A ∩ B)

    Parameters:
        A, B (list): the lists to be intersected

    Returns:
        inter (list): A ∩ B
    '''
    inter = list(set(A) & set(B))
    return inter

def union(A, B):
    ''' Returns the union of two lists A and B (A ∪ B)

    Parameters:
        A, B (list): the lists to be unioned

    Returns:
        union (list): A ∪ B
    '''
    union = list(set(A) | set(B))
    return union