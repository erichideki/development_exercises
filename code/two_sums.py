def two_sums(list_numbers: list, target: int):

    """Given an array of integers nums and an integer target, return indices of the 
    two numbers such that they add up to target
    nums = [2,7,11,15], target = 9
    >>> two_sums([2,7,11,15], 9)
    [0, 1]
    >>> two_sums([3,2,4], 6)
    [1, 2]
    >>> two_sums([3,3], 6)
    [0, 1]
    """
    #Solution 1

    """num_indices = {}
    for i, num in enumerate(list_numbers):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return []"""

    #Solution 2

    prevMap = {}
    for i, n in enumerate(list_numbers):
        diff = target - i
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()