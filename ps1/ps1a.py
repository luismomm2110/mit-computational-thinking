###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

# ================================
# Part A: Transporting Space Cows
# ================================

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

    dict_cows = {}

    file = open(filename, "r")

    lines = file.readlines()

    for line in lines:
        cow = line.split(",")
        dict_cows[cow[0]] = cow[1]

    return dict_cows


# Problem 2

def greedy_cow_transport(cows, limit=10):
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
    trips = []

    cows_by_weight = {k: v for k, v in sorted(
        cows.items(), key=lambda item: item[1])}

    total_weight = 0
    trip = []

    for cow in cows_by_weight:
        total_weight = int(cows_by_weight[cow]) + total_weight
        if total_weight <= limit:
            trip.append(cow)
        else:
            total_weight = int(cows_by_weight[cow])
            trips.append(trip)
            trip = [cow]

    trips.append(trip)
    return trips

# Problem 3


def brute_force_cow_transport(cows, limit=10):
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
    partitions = get_partitions(cows)

    trips = []
    passed_limit = False

    for partition in partitions:
        passed_limit = False

        for trip in partition:
            total_weight = 0

            for cow in trip:
                total_weight = int(cows[cow]) + total_weight

                if total_weight >= limit:
                    passed_limit = True
                    break

            if passed_limit:
                break

        if passed_limit:
            continue

        trips.append(partition)

    return sorted(trips, key=len)[0]


# Problem 4


def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything
    """

    cows = load_cows("ps1_cow_data.txt")

    greedy_start = time.time()
    greedy_trips = greedy_cow_transport(cows)
    print(greedy_trips)
    print(len(greedy_trips))
    greedy_end = time.time()
    print(greedy_end - greedy_start)

    brute_start = time.time()
    brute_trips = brute_force_cow_transport(cows)
    print(brute_trips)
    print(len(brute_trips))
    brute_end = time.time()
    print(brute_end - brute_start)


def main():
    compare_cow_transport_algorithms()


if __name__ == "__main__":
    main()
