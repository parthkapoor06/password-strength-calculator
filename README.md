# Password Strength Calculator

A Python project designed to calculate and validate the strength of passwords, with the option to generate secure passwords that meet minimum strength requirements.

## Features
- **Password Strength Calculation**:
  - Evaluates password strength based on length and diversity of character groups (e.g., uppercase, lowercase, digits, symbols).
- **Random Password Generator**:
  - Creates secure random passwords of specified length using a diverse set of characters.
- **User Interaction**:
  - Allows users to input their own passwords or generate one that meets a specified minimum strength.

## Files
### `password.py`
- Contains functions to:
  - Count the number of character groups in a password.
  - Calculate the strength of a password based on predefined rules.

### `generate.py`
- Contains a function to:
  - Generate a random password of a specified length using characters from all groups.

### `login.py`
- Implements user interaction to:
  - Allow users to input a password or generate one.
  - Validate the strength of the password against a minimum requirement.
  - Provide feedback on whether the password is strong enough.

## License
This project is licensed under the [MIT License](LICENSE).
