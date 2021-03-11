#
# 
# your comment header here
# 
# 

# import libraries you will need
import functions as fn

def main():
    # this function is complete, DO NOT MODIFY IT
    # you may modify it while you program, but when you turn in for grading
    # it must be returned to EXACTLY this state
    
    # this will create and initialize the array with
    # random numbers 10-100 (inclusive)
    numbers = fn.make_array()
    
    # show the array
    print("All the numbers...")
    print(numbers)
    print()
    
    print("The minimum is:", fn.minimum(numbers))
    print("The maximum is:", fn.maximum(numbers))
    print("The total is:", fn.total(numbers))
    print("The average is:", fn.average(numbers))
    print()

    # this will reverse the array
    numbers = fn.reverse_array(numbers)

    # show the array
    print("All the numbers...")
    print(numbers)
    print()
    
    print("The minimum is:", fn.minimum(numbers))
    print("The maximum is:", fn.maximum(numbers))
    print("The total is:", fn.total(numbers))
    print("The average is:", fn.average(numbers))
    print()

# this starts the program
main()

