def rotate(list_rotate: list, k: int):
    """ https://www.youtube.com/watch?v=f84MhsTrh_g&list=PLA05yVJtRWYTEVEzX5XXV3Re7X7U3asa7&index=2
        >>> rotate([1, 2, 3, 4, 5, 6, 7], 3)
        [5, 6, 7, 1, 2, 3, 4]
        >>> rotate([1, 2, 3, 4, 5, 6, 7], 4)
        [4, 5, 6, 7, 1, 2, 3]
    """
    
    first_slice = list_rotate[-k:]
    second_slice = list_rotate[:-k]

    return first_slice + second_slice

if __name__ == "__main__":
    import doctest
    doctest.testmod()
