import re
import math

def calculate_entropy(password):
    """Calculate the entropy of a given password."""
    if not password:
        return 0

    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'\d', password):
        pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        pool_size += 32  # Approximate number of special characters

    entropy = len(password) * math.log2(pool_size)
    return entropy

def password_strength(password):
    """Evaluate the strength of a password based on its entropy."""
    entropy = calculate_entropy(password)
    
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Reasonable"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"
    
if __name__ == "__main__":
    pwd = input("Enter a password to evaluate: ")
    strength = password_strength(pwd)
    print(f"Password Strength: {strength}")
    print(f"Entropy: {calculate_entropy(pwd):.2f} bits")
