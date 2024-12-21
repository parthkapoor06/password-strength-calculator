# Function to check the number of character groups in a password
def count_groups(pwd):
    number_of_groups = 0
    # Check if the password contains lowercase letters
    for char in pwd:
        if char in "abcdefghijklmnopqrstuvwxyz":
            number_of_groups += 1
            break
    # Check if the password contains uppercase letters
    for char in pwd:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            number_of_groups += 1
            break
    # Check if the password contains digits
    for char in pwd:
        if char in "0123456789":
            number_of_groups += 1
            break
    # Check if the password contains symbols
    for char in pwd:
        if char in "!@#$%^&*/?-+=,.|~":
            number_of_groups += 1
            break
    return number_of_groups

# Function to calculate the strength of a password
def password_strength(pwd):
    # Get the number of character groups in the password
    groups = count_groups(pwd)
    # Get the length of the password
    length = len(pwd)
    strength = 0

    # Check if the password contains invalid characters (space, tab, newline)
    for char in pwd:
        if char in " \t\n":
            return 0  # Password strength is 0 if invalid characters are present

    # If length is less than 5, the strength is 0 (per assignment table)
    if length < 5:
        return 0

    # For passwords 5 to 8 characters long, determine strength based on groups
    if 5 <= length <= 8:
        if groups < 2:
            strength = 1
        elif groups == 2 or groups == 3:
            strength = 2
        elif groups == 4:
            strength = 3
        return strength

    # For passwords 9 to 12 characters long, determine strength based on groups
    if 9 <= length <= 12:
        if groups < 2:
            strength = 2
        elif groups == 2 or groups == 3:
            strength = 3
        elif groups == 4:
            strength = 4
        return strength

    # For passwords longer than 12 characters, determine strength based on groups
    if length > 12:
        if groups < 2:
            strength = 3
        elif groups == 2 or groups == 3:
            strength = 4
        elif groups == 4:
            strength = 5
        return strength
