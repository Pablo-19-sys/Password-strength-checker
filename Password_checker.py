# Import the regular expression (re) module to use for pattern matching
import re

# Define a function to check the strength of a password
def check_password_strength(password):
    # Define a list of conditions to evaluate the password's strength
    conditions = [
        len(password) >= 8,  # Condition 1: Password must be at least 8 characters long.
        bool(re.search(r"[A-Z]", password)),  # Condition 2: Contain at least one uppercase letter.
        bool(re.search(r"[a-z]", password)),  # Condition 3: Contain at least one lowercase letter.
        bool(re.search(r"[!@#$%^?€&*]", password)),  # Condition 4: Contain at least one special character.
        bool(re.search(r"\d", password))  # Condition 5: Contain at least one digit (0-9).
    ]

    # Calculate the total strength score by summing the boolean values of the conditions.
    # True (1) values are counted, and False (0) values are ignored.
    strength_score = sum(conditions)

    # Determine the strength message based on the number of conditions that are met.
    if strength_score == 5:
        strength_message = "Great password!" # If all conditions are met (strength_score == 5), it's a "Great password!"
    elif strength_score >= 3: 
        strength_message = "Good password, but could be better." # If at least 3 conditions are met, it's "Good password, but could be better."
    else:
        strength_message = "Weak password. Consider improving it." # Otherwise, it's "Weak password. Consider improving it."

    # Create a list of improvement suggestions based on the conditions that were not met.
    suggestions = [
        "Increase the length to at least 8 characters" # Suggest length improvement if condition 1 is not met.
        if not conditions[0] else None, 
        "Add at least one uppercase letter" # Suggest adding an uppercase letter if condition 2 is not met.
        if not conditions[1] else None,
        "Add at least one lowercase letter" # Suggest adding a lowercase letter if condition 3 is not met.
        if not conditions[2] else None,
        "Add at least one special character (e.g., !@#$%^&*)" # Suggest adding a special character if condition 4 is not met.
        if not conditions[3] else None,
        "Add at least one number" # Suggest adding a number if condition 5 is not met.
        if not conditions[4] else None
    ]

    # Remove any `None` values from the suggestions list, keeping only the actual suggestions.
    suggestions = [s for s in suggestions if s]

    # Return the formatted result with the strength message and suggestions
    suggestions_text = ", ".join(suggestions) if suggestions else "None"
    return f"{strength_message}\nSuggestions to improve: {suggestions_text}."

# Ask the user to enter their password
password = input("Enter your password: ")

# Call the function and print the result
print(check_password_strength(password))
