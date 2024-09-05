def count_frequency_string(s: str):
    """Count the number of frequency of letters
        >>> count_frequency_string("eric")
        {'e': 1, 'r': 1, 'i': 1, 'c': 1}
        >>> count_frequency_string("banana")
        {'b': 1, 'a': 3, 'n': 2}
    """
    dct = {}

    for letter in s:
        dct[letter] = dct.get(letter, 0) + 1
    
    return dct

    #return dict(Counter(s))

if __name__ == "__main__":
    import doctest
    doctest.testmod()