def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create an empty dict to hold the data
    dictionary = {}

    # Going to want to loop through the arrays
    for  array in arrays:

        # loop through the items
        for item in array:

            # if the item is already in the dictionary, add 1
            if item in dictionary:
                dictionary[item] += 1
            
            #else, add it as a key
            else:
                dictionary[item] = 1
    
    #empty list will have the numbers that are in the array
    result = []

    # loop through the pairs through the dictionary
    for data in list(dictionary.items()):
        
        #if value in each key = length of the array, it has been in every array
        if data[1] == len(arrays):

            # append the key to the result
            result.append(data[0])


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
