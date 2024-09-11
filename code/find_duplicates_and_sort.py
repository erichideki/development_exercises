

def find_duplicates_and_sort(listed_numbers: list):
    """ Given a list of numbers, find the duplicates and print them sorted
        >>> find_duplicates_and_sort([5, 1, 4, 4, 2, 2, 3, 4, 5, 6])
        [2, 4, 5]
        >>> find_duplicates_and_sort([1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9])
        [1, 2, 5, 9]

        What's the time complexity of your solution?

        How does a HashMap work? How does it do hashing? How are equals() and hashcode() related?

        What is the performance difference between streams and loops?

        What is a REST API and how to use it?

        What is the difference between SQL and NoSQL databases? How do they scale?

        What asynchronous communication could you use for application communications?

        How do queue systems guarantee the delivery of messages?
    """
    #Solution 1
    #Time complexity: O(n^2) where n is the length of the input list
    #Auxiliary space: O(k) where k is the number of duplicates in the input list.
    
    """_size = len(listed_numbers)
    duplicated_numbers = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if listed_numbers[i] == listed_numbers[j] not in duplicated_numbers:
                duplicated_numbers.append(listed_numbers[i])
    
    sorted_duplicated_numbers = sorted(duplicated_numbers)
    
    return sorted_duplicated_numbers"""

    #Solution 2

    """uniqueList = []
    duplicatedList = []

    for i in listed_numbers:
        if i not in uniqueList:
            uniqueList.append(i)
        elif i not in duplicatedList:
            duplicatedList.append(i)
    
    sorted_duplicated_numbers = sorted(duplicatedList)
    return sorted_duplicated_numbers"""

    #Time Complexity: O(n)
    #Auxiliary Space: O(n)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# https://www.geeksforgeeks.org/python-program-print-duplicates-list-integers/