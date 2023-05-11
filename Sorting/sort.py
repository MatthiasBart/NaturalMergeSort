"""
Sort an array with the requested algorithm
"""

from array import array

def sort(a: array, l: int, r: int) -> None:
    """
    Sort a list with the requested sorting algorithm
    :param a: array of values to sort
    :param l: left boundary index - where to start sorting
    :param r: right boundary index - where to stop sorting
    :return: None
    """
    ll = -1
    mm = -1
    rr = -1
    # Begin implementation
    # gehe von 
    if r < l: return
    while ll != l:
        rr = l - 1
        while rr < r:
            ll = rr + 1
            mm = ll 
            while mm < r and a[mm + 1] >= a[mm]:
                mm = mm + 1 
            if mm < r:
                rr = mm + 1
                while rr < r and a[rr + 1] >= a[rr]:
                    rr = rr + 1
                a[slice(ll,rr+1)] = merge(a, ll, mm, rr)
            else:
                rr = mm


    # End implementation


# Add your auxiliary methods here
# Begin implementation

def merge(a: array, ll: int, mm: int, rr: int) -> array:
    buffer = array('i',[])
    m = mm + 1
    l = ll 
    while l <= mm and m <= rr:
        if a[l] <= a[m]:
            buffer.append(a[l])
            l = l + 1
        else:
            buffer.append(a[m])
            m = m + 1

    if l > mm:
        while m <= rr:
            buffer.append(a[m])
            m = m + 1
    else:
        while l <= mm:
            buffer.append(a[l])
            l = l + 1
    return buffer
# End implementation