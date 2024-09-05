def fizz_buzz(n:int):
    """ Return fizz if is mod % 2, buzz if mod % 3. Fizzbuzz if mod % 2 and 3
        >>> fizz_buzz(6)
    """
    for i in range(1, n + 1):
        if i % (3 * 2) == 0:
            print(i)
            print("Fizzbuzz")
        elif i % 2 == 0:
            print(i)
            print("Fizz")
        elif i % 3 == 0:
            print(i)
            print("Buzz")


if __name__ == "__main__":
    import doctest
    doctest.testmod()