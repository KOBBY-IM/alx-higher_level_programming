#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    # Get the sum of all scores.
    sum_scores = sum(score for score, weight in my_list)

    # Get the sum of all weights.
    sum_weights = sum(weight for score, weight in my_list)

    # Calculate the weighted average.
    weighted_average = sum_scores / sum_weights

    return weighted_average
