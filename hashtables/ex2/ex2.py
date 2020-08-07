#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

#create dictionary
dictionary = {}

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    I want to return the correct route of all the trips
    """
    # Your code here
    # first i want to loop thru the array & put the tickets in a dict
    for ticket in tickets:
        dictionary[ticket.source] = ticket.destination

    # This empty list will be holding the routes of the tickets
    route = []

    # start = location where we begin, our source 'None' will be stored there
    start = dictionary['NONE']

    # Now I'd want to append my start location to its routes
    route.append(start)

    current = dictionary["NONE"]

    while True:
        destination = dictionary[current]

        # if my destination is None, we've reached the end
        if destination == "NONE":
            # append destination to the route and break the loop
            route.append(destination)
            break

        #append the destination to routes again 
        route.append(destination)
        #update the current and continue my loop 
        current = destination

    return route
