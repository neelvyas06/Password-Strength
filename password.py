"""
******************************
CS 1026A - Assignment 2 – Password Strength
Code by: [Neel Vyas]
Student ID: [251442237]
File created: October 25, 2024
******************************
This file defines two functions: count_groups and password_strength.
- count_groups: Counts the number of character groups in a password.
- password_strength: Calculates the strength of a password based on length and character groups.
"""

# Function to count the number of character groups in a password
def count_groups(pwd):
    """
    Counts and returns the number of character groups in a password.
    Character groups are: lowercase letters, uppercase letters, digits, symbols.
    """
    # Define character groups
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*/?-+=,.|~"

    # Initialize a list to track which groups are used
    used_groups = [False] * 4  # [lowercase, uppercase, digits, symbols]

    # Check each character in the password
    for char in pwd:
        if char in lowercase:
            used_groups[0] = True
        elif char in uppercase:
            used_groups[1] = True
        elif char in digits:
            used_groups[2] = True
        elif char in symbols:
            used_groups[3] = True

    # Count and return the number of active groups
    return sum(used_groups)

# Function to calculate the strength of a password
def password_strength(pwd):
    """
    Determines the strength of the password based on its length and number of character groups.
    Returns an integer strength level from 0 to 5.
    """
    # Check for invalid characters
    if ' ' in pwd or '\t' in pwd or '\n' in pwd:
        return 0

    # Determine password length and character groups
    length = len(pwd)
    num_groups = count_groups(pwd)

    # Evaluate password strength
    if length < 5:
        return 0
    elif length <= 8:
        if num_groups <= 1:
            return 1
        elif num_groups == 2:
            return 2
        elif num_groups == 3:
            return 3
    elif length <= 12:
        if num_groups <= 1:
            return 2
        elif num_groups == 2:
            return 3
        elif num_groups == 3:
            return 4
    else:  # length > 12
        if num_groups <= 1:
            return 3
        elif num_groups == 2:
            return 4
        elif num_groups >= 3:
            return 5

    return
