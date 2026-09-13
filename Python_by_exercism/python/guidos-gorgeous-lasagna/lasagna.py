"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): Minutes the lasagna has already baked.

    Returns:
        int: Minutes still needed to reach EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - time

#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(numberLayer) :
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): Minutes the lasagna has already baked.

    Returns:
        int: Minutes still needed to reach EXPECTED_BAKE_TIME.
    """
    PREPARATION_TIME = 2
    return PREPARATION_TIME * numberLayer


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): Minutes the lasagna has already baked.

    Returns:
        int: Minutes still needed to reach EXPECTED_BAKE_TIME.
    """ 
    PREPARATION_TIME = 2*number_of_layers
    return PREPARATION_TIME+elapsed_bake_time



# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
