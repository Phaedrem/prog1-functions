######################
# Name: Darren Bowers
# Coding 06
# Purpose: Assignment for writing functions to work with Numpy arrays.
######################

# SIZE is a global constant, use this throughout your program.
# you should be able to change this to any integer > 0 and your
# whole program will still work correctly. TEST THIS!
SIZE = 10

import numpy as np
import random

def make_array():
    array = np.array([0] * SIZE, dtype=int)
    for i in range(SIZE):
        array[i] = random.randint(10,100)
    return array
    
def total(nums):
    total_numbers = 0
    for i in range(SIZE):
        total_numbers += nums[i]
    return int(total_numbers)

def average(nums):
    average_numbers = float(total(nums))/float(SIZE)
    return float(average_numbers)

def minimum(nums):
    minimum = nums[0]
    for i in range(1, SIZE):
        if nums[i] < minimum: minimum = nums[i]
    return minimum

def maximum(nums):
    maximum = nums[0]
    for i in range(1, SIZE):
        if nums[i] > maximum: maximum = nums[i]
    return maximum

def reverse_array(arr):
    array = np.array([0] * SIZE, dtype=int)
    for i in range(SIZE):
        array[SIZE -(i+1)] = arr[i]
    return array
