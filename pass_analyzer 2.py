# Import necessary libraries
import string
import math
import getpass

# Define minimum password length
MIN_LENGTH = 8

def calculate_entropy(password):
    """Calculate password entropy based on character diversity."""
    charset_size = 0
    
    # Check what types of characters are in the password
    if any(c in string.ascii_lowercase for c in password):
        charset_size += 26  # lowercase letters
    if any(c in string.ascii_uppercase for c in password):
        charset_size += 26  # uppercase letters
    if any(c in string.digits for c in password):
        charset_size += 10  # digits 0-9
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)  # special characters
    
    # Calculate entropy using the formula
    if charset_size > 0:
        entropy = len(password) * math.log2(charset_size)
    else:
        entropy = 0
    
    return entropy

def check_password_strength():
    """Analyze a password and provide detailed feedback."""
    
    # Get password from user (hidden input)
    password = getpass.getpass('Enter your password to analyze: ')
    
    # Check minimum length
    if len(password) < MIN_LENGTH:
        print(f"⚠️ PASSWORD TOO SHORT! Must be at least {MIN_LENGTH} characters.")
        return
    
    # Count different character types
    lower_count = sum(1 for c in password if c in string.ascii_lowercase)
    upper_count = sum(1 for c in password if c in string.ascii_uppercase)
    digit_count = sum(1 for c in password if c in string.digits)
    special_count = sum(1 for c in password if c in string.punctuation)
    
    # Calculate entropy score
    entropy = calculate_entropy(password)
    
    # Determine password strength based on entropy
    if entropy < 28:
        strength = "⚠️ VERY WEAK"
        advice = "Easily guessable! Change immediately."
    elif entropy < 36:
        strength = "⚠️ WEAK"
        advice = "Can be cracked quickly. Use a stronger password."
    elif entropy < 60:
        strength = "✅ MODERATE"
        advice = "Decent password, but can be improved."
    elif entropy < 80:
        strength = "✅ STRONG"
        advice = "Hard to guess, but consider making it longer."
    else:
        strength = "🔒 VERY STRONG"
        advice = "Excellent password! Highly secure."
    
    # Display results
    print("\n" + "="*50)
    print("PASSWORD ANALYSIS REPORT")
    print("="*50)
    print(f"Password Length: {len(password)} characters")
    print(f"Lowercase letters: {lower_count}")
    print(f"Uppercase letters: {upper_count}")
    print(f"Digits: {digit_count}")
    print(f"Special characters: {special_count}")
    print(f"\nEntropy Score: {entropy:.2f} bits")
    print(f"Strength Rating: {strength}")
    print(f"Advice: {advice}")
    print("="*50 + "\n")

def main():
    """Main program loop."""
    print("="*50)
    print("PASSWORD STRENGTH ANALYZER")
    print("="*50)
    
    while True:
        check_password_strength()
        
        # Ask if user wants to check another password
        choice = input("Check another password? (y/n): ").strip().lower()
        if choice != 'y':
            print("\n👋 Exiting... Stay secure!")
            break

# Run the program
if __name__ == "__main__":
    main()
