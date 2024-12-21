from password import *
from generate import *

# Function that prompts the user to either enter their own password or generate a random password
def process_password(min_strength):
    # Initialize the strength variable
    strength = -1

    # This while loop ensures the user's password meets or exceeds the minimum strength
    while strength < min_strength:
        # Ask the user to either input a password or generate one
        user_input = input("Type in a new password or type X for a randomly generated password: ")

        # If the user chooses to generate a random password
        if user_input.lower() == "x":
            generated_password = ""

            # Generate random passwords until one meets the minimum strength
            while strength < min_strength:
                # Call the generate_password function and store the result
                generated_password = generate_password(15)
                # Calculate the strength of the generated password
                strength = password_strength(generated_password)

            # Output the generated password and its strength
            print("Your password:", generated_password)
            print("Your password has a strength of", strength)
            print("Your password is strong enough! Thank you.")

        # If the user enters their own password
        else:
            # Print the entered password
            print("You entered:", user_input)
            # Calculate the strength of the user's password
            strength = password_strength(user_input)
            # Print the strength of the entered password
            print("Your password has a strength of", strength)

            # Check if the password meets the minimum strength
            if strength < min_strength:
                print("Your password is not strong enough. Please create a new password that is stronger.\n")
            else:
                print("Your password is strong enough! Thank you.")
