# Import the regular expression (re) module to use for pattern matching
import re

# Define a function to check the strength of a password
def check_password_strength(password):
    # Define a list of conditions to evaluate the password's strength
    conditions = [
        len(password) >= 8,  # Condition 1: Password must be at least 8 characters long
        bool(re.search(r"[A-Z]", password)),  # Condition 2: Password must contain at least one uppercase letter (A-Z)
        bool(re.search(r"[a-z]", password)),  # Condition 3: Password must contain at least one lowercase letter (a-z)
        bool(re.search(r"[!@#$%^?€&*]", password)),  # Condition 4: Password must contain at least one special character (e.g., !@#$%^&*)
        bool(re.search(r"\d", password))  # Condition 5: Password must contain at least one digit (0-9)
    ]
    
    # Calculate the total strength score by summing the boolean values of the conditions
    # True (1) values are counted, and False (0) values are ignored
    strength_score = sum(conditions)
    
    # Determine the strength message based on the number of conditions that are met
    # If all conditions are met (strength_score == 5), it's a "Great password!"
    # If at least 3 conditions are met, it's "Good password, but could be better."
    # Otherwise, it's "Weak password. Consider improving it."
    strength_message = "Great password!" if strength_score == 5 else "Good password, but could be better." if strength_score >= 3 else "Weak password. Consider improving it."
    
    # Create a list of improvement suggestions based on the conditions that were not met
    suggestions = [
        "Increase the length to at least 8 characters" if not conditions[0] else None,  # Suggest length improvement if condition 1 is not met
        "Add at least one uppercase letter" if not conditions[1] else None,  # Suggest adding an uppercase letter if condition 2 is not met
        "Add at least one lowercase letter" if not conditions[2] else None,  # Suggest adding a lowercase letter if condition 3 is not met
        "Add at least one special character (e.g., !@#$%^&*)" if not conditions[3] else None,  # Suggest adding a special character if condition 4 is not met
        "Add at least one number" if not conditions[4] else None  # Suggest adding a number if condition 5 is not met
    ]
    
    # Remove any `None` values from the suggestions list, keeping only the actual suggestions
    suggestions = [s for s in suggestions if s]  # Filter out None values
    
    # Return a formatted string with the strength message and improvement suggestions
    return f"{strength_message}\nSuggestions to improve: {', '.join(suggestions) if suggestions else 'None'}"

# Ask the user to enter their password
password = input("Enter your password: ")

# Call the function and print the result
print(check_password_strength(password))
