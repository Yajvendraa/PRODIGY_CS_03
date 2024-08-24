import re

def assess_password_strength(password):
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "numbers": bool(re.search(r'[0-9]', password)),
        "special_characters": bool(re.search(r'[@#$%^&*!]', password))
    }

    # Count how many criteria are met
    criteria_met = sum(strength_criteria.values())

    # Feedback based on the number of criteria met
    if criteria_met == 0:
        return "Very Weak", strength_criteria
    elif criteria_met == 1:
        return "Weak", strength_criteria
    elif criteria_met == 2:
        return "Weak", strength_criteria
    elif criteria_met == 3:
        return "Moderate", strength_criteria
    elif criteria_met == 4:
        return "Strong", strength_criteria
    else:
        return "Very Strong", strength_criteria

# Example usage
password = input("Enter your password: ")
strength, criteria = assess_password_strength(password)

print(f"Password Strength: {strength}")
print("Criteria Met:")
for criterion, met in criteria.items():
    print(f"{criterion}: {'Yes' if met else 'No'}")
