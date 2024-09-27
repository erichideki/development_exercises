from typing import Iterable

def reverse_words(word: str) -> str:
    """ https://www.youtube.com/watch?v=OksSY2X5KSU&list=PLA05yVJtRWYTEVEzX5XXV3Re7X7U3asa7&index=3
        >>> reverse_words('the sky is blue')
        'blue is sky the'
    """
    #split_words.reverse()
    #result = " ".join(str(w) for w in split_words)
    
    split_words = word.split(' ')
    result = ' '.join(split_words[::-1])
    return result

def constant_reverse_words(word: str) -> Iterable:
    """
    >>> list(constant_reverse_words('the sky is blue'))
        ['blue', 'is', 'sky', 'the']
    >>> list(constant_reverse_words('The Mordors home'))
        ['home', 'Mordors, 'The']
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()