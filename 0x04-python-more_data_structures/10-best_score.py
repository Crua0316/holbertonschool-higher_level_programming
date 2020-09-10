#!/usr/bin/python3
def best_score(a_dictionary):
    d_max = None
    if a_dictionary:
        d_max = max(a_dictionary, key=a_dictionary.get)
    return d_max
