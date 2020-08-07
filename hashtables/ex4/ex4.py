def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # first, I'd want to sort this from largest to smallest order
    a.sort(reverse=True)

    # create my empty dictionary
    dictionary = {}

    #want to loop through the array
    for item in a:
        # if the item is positive  we want to add a key in the dictionary
        if item > 0:
            dictionary[item] = None

        # if the item is negative, we want to see if the numbers opposite is in the dictionary
        if item < 0:
            if abs(item) in dictionary:

                # if it is, add its value for its positive key
                dictionary[abs(item)] = item
    
    # now i want a list that will have positive nums that have the negatives as well
    result = []

    #loop through
    for key, value in dictionary.items():
        #if value is not None, it means that key: value pair contains an positive number and negative as well
        if value != None:
            #append the key (positive number)
            result.append(key)

    #result is in descending order, largest to smallest.
    result.sort()

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
