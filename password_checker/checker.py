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
    
def password_policy_check(password):
    """Check if the password meets basic policy requirements."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."
    if not re.search(r'[^a-zA-Z0-9]', password):
        return False, "Password must contain at least one special character."
    
    return True, "Password meets all policy requirements."

def password_cracker(entropy,guesses_per_second = 1e9):
    """Estimate the time to crack a password based on its entropy."""
    total_guesses = 2 ** entropy
    seconds = total_guesses / guesses_per_second

    intervals = [
        ('years', 60 * 60 * 24 * 365),
        ('days', 60 * 60 * 24),
        ('hours', 60 * 60),
        ('minutes', 60),
        ('seconds', 1)
    ]

    result = []
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            result.append(f"{int(value)} {name}")
    
    return ', '.join(result) if result else "less than a second"


    
if __name__ == "__main__":
    pwd = input("Enter a password to evaluate: ")
    strength = password_strength(pwd)
    print(f"Password Strength: {strength}")
    print(f"Entropy: {calculate_entropy(pwd):.2f} bits")
    policy_ok, policy_msg = password_policy_check(pwd)
    print(f"Policy Check: {policy_msg}")
    crack_time = password_cracker(calculate_entropy(pwd))
    print(f"Estimated Time to Crack: {crack_time}")
    
