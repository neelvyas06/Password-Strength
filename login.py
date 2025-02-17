"""
******************************
CS 1026A - Assignment 2 – Password Strength
Code by: [Neel Vyas]
Student ID: [251442237]
File created: October 25, 2024
******************************
This file defines the function process_password.
- process_password: Manages user interaction for password entry or generation, and checks password strength.
"""

from password import count_groups, password_strength
from generate import generate_password

# Main function to handle user input for password creation or generation
def process_password(min_strength):
    """
    Continuously prompts the user to enter a new password or generates a random password until
    the password meets the required minimum strength.
    """
    print(f"Welcome! Please create a password with at least strength {min_strength}.")

    # Start loop to keep asking for input until minimum strength is achieved
    while True:
        # Prompt user input for password creation or generation
        user_input = input("Enter a new password or type 'X' for a random password: ").strip()

        if user_input.lower() == 'x':
            # Generate a random password if the user inputs 'X'
            random_password = generate_password(15)
            strength = password_strength(random_password)
            print(f"\nGenerated Password: {random_password}")
            print(f"Password Strength: {strength}\n")
        else:
            # Calculate the strength of the user-entered password
            strength = password_strength(user_input)
            print(f"\nEntered Password: {user_input}")
            print(f"Password Strength: {strength}\n")

        # Check if the password strength meets the required minimum
        if strength >= min_strength:
            print("Password is strong enough! Program complete.")
            break
        else:
            print("Password is not strong enough. Please try again.")

# Execute the function if this file is run directly
if __name__ == "__main__":
    process_password(3)
