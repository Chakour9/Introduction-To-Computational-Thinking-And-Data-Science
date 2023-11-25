###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    file = open(filename,'r')
    dic_cow = {}
    for line in file:
        i = line.index(',')
        dic_cow[line[:i]] = int(line[i+1])
    return dic_cow


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    L = []
    for key in cows:
        L.append(key)
    sort = sorted(L,key= lambda x : cows[x], reverse= True)
    result = []
    while sort != []:
        acc,val = [],0
        for cow in sort:
            if val + cows[cow] < limit:
                acc.append(cow)
                val += cows[cow]
        for item in acc:
            sort.remove(item)
        result.append(acc)
    return result

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    L = []
    for key in cows:
        L.append(key)

    i = 10
    for partition in get_partitions(L):
        test = True
        for list_cow in partition:
            val = 0
            for cow in list_cow:
                val+= cows[cow]
            if val > 10:
                test = False
                break
        if test and len(partition) <= i:
            i = len(partition)
            result = partition
    return result

def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds."""

    start1 = time.time()
    greedy_cow_transport(load_cows("ps1_cow_data.txt"),10)
    end1 = time.time()
    print(end1 - start1)

    start2 = time.time()
    brute_force_cow_transport(load_cows("ps1_cow_data.txt"),10)
    end2 = time.time()
    print(end2 - start2)

compare_cow_transport_algorithms()

