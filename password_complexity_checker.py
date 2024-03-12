import string

def check_length(password):
    return len(password) >= 8

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_special_char(password):
    special_characters = string.punctuation
    return any(char in special_characters for char in password)

def assess_strength(password):
    criteria = {
        "Length": check_length(password),
        "Lowercase": check_lowercase(password),
        "Uppercase": check_uppercase(password),
        "Digit": check_digit(password),
        "Special Character": check_special_char(password)
    }

    strength = sum(criteria.values())
    if strength >= 4:
        return "Strong", criteria
    elif strength >= 2:
        return "Average", criteria
    else:
        return "Weak", criteria

def main():
    password = input("Enter your password: ")
    strength, criteria = assess_strength(password)
    
    print("\nPassword Strength:", strength)
    print("Criteria:")
    for criterion, value in criteria.items():
        print(f"{criterion}: {'Yes' if value else 'No'}")

if __name__ == "__main__":
    main()
