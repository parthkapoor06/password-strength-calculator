import random

# Function to generate a randomly generated password of specified length
def generate_password(length):
    # Create a string of all possible characters from all 4 character groups
    ALL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*/?-+=,.|~"
    count = 0
    password = ""

    # While loop that runs for the specified length to generate the password
    while count < length:
        # Randomly pick a character from ALL_CHARS and add it to the password
        password += random.choice(ALL_CHARS)
        # Increment the count to ensure the loop runs only 'length' times
        count += 1

    # Return the generated password
    return password
