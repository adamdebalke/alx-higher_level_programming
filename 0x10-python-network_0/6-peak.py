#!/usr/bin/python3
"""This module contains a peak finding function"""


def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
