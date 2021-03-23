######################
# Name: Darren Bowers
# Coding 06
# Purpose: Assignment for writing functions to work with Numpy arrays.
######################

# SIZE is a global constant, use this throughout your program.
# you should be able to change this to any integer > 0 and your
# whole program will still work correctly. TEST THIS!
SIZE = 10
MIN = 10
MAX = 100

import numpy as np
import random

def make_array():
    if isinstance(SIZE, int):
        array = np.array([0] * SIZE, dtype=int)
        for i in range(SIZE):
            array[i] = random.randint(MIN,MAX)
    else:
        array = 0
    return array
    
def total(nums):
    if all(nums > 0):
        total_numbers = 0
        for i in range(SIZE):
            total_numbers += nums[i]
    else:
        total_numbers = 0
    return int(total_numbers)

def average(nums):
    #needs a validation step
    #average_numbers = float(total(nums))/float(SIZE)
    #return float(average_numbers)
    # this will accept a Numpy integer array
    # find the average of the array by calling total() and dividing by SIZE
    # you may not use the Numpy average function or anything similar
    # return the average as a float which has ensures pure float
    # calculations and guarantees maximum precision
    pass

def minimum(nums):
    # this will accept a Numpy integer array
    # find the minimum of the array USING A LOOP and return it
    # you may not use the Numpy min function or anything similar
    # return the minimum as an integer
    pass

def maximum(nums):
    # this will accept a Numpy integer array
    # find the maximum of the array USING A LOOP and return it
    # you may not use the Numpy max function or anything similar
    # return the maximum as an integer
    pass

def reverse_array(arr):
    # this will accept a Numpy integer array
    # do NOT alter the array passed in. use it as-is
    # put the numbers from arr in another array in reverse order
    # you MUST use a loop to do this
    # return the reversed array
    pass

