###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

# ================================
# Part B: Golden Eggs
# ================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """

    # Greedy solution

#    if len(egg_weights) == 0:
#        return 0
#    else:
#       if egg_weights[0] <= target_weight:
#           target_weight -= egg_weights[0]
#           total_eggs = dp_make_weight(egg_weights, target_weight, memo) + 1
#       else:
#           total_eggs = dp_make_weight(
#               egg_weights[1:], target_weight, memo)
#
#    return total_eggs
#

    # Brute force
#
#    current_solution = float("inf")
#
#    if target_weight == 0:
#        return 0
#    elif target_weight > 0:
#        for weight in egg_weights:
#            temp_result = dp_make_weight(egg_weights, target_weight-weight)
#            current_solution = min(temp_result, current_solution)
#
#    return current_solution + 1
    # Dynamical Programming

    current_solution = float("inf")

    if target_weight == 0:
        return 0
    elif target_weight in memo:
        return memo[target_weight]
    elif target_weight > 0:
        for weight in egg_weights:
            temp_result = dp_make_weight(
                egg_weights, target_weight-weight, memo)
            current_solution = min(temp_result, current_solution)

    memo[target_weight] = current_solution + 1
    return current_solution + 1

    # EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    egg_weights = (1, 6, 9)
    n = 14
    print("Egg weights = (1, 6, 9)")
    print("n = 14")
    print("Expected ouput: 4 (2*6  + 2*1 = 14)")
    print("Actual output:", dp_make_weight(egg_weights, n, {}))
    print()

    import pdb
    pdb.set_trace()
    egg_weights = (1, 2)
    n = 3
    print("Actual output:", dp_make_weight(egg_weights, n, {}))
