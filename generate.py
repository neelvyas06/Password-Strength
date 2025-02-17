"""
******************************
CS 1026A - Assignment 2 – Password Strength
Code by: [Neel Vyas]
Student ID: [251442237]
File created: October 25, 2024
******************************
This file defines the function generate_password.
- generate_password: Generates a random password of a specified length, including characters from all groups.
"""

import random

# Function to generate a random password of a given length
def generate_password(length):
    """
    Generates a random password of the specified length using lowercase, uppercase, digits, and symbols.
    Returns the generated password as a string.
    """
    # Define character groups
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*/?-+=,.|~"

    # Combine all groups for random selection
    all_characters = lowercase + uppercase + digits + symbols
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password
