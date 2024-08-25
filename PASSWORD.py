import random
import string

def sanitize_base_words(base_words):
    """Remove base words that look like file paths or contain special characters."""
    sanitized_words = []
    for word in base_words:
        if any(char in word for char in "/\\"):
            print(f"Skipping invalid base word: {word}")
            continue
        sanitized_words.append(word)
    return sanitized_words

def generate_passwords(base_words, num_passwords=100000):
    passwords = set()
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>/?"

    def generate_single_word_variations(base_word):
        variations = set()
        variations.add(base_word + random.choice(string.ascii_letters + string.digits))
        variations.add(base_word + random.choice(special_chars) + random.choice(string.ascii_letters))
        number = random.randint(1000, 9999)
        variations.add(base_word + str(number))
        random_number = ''.join(random.choices(string.digits, k=3))
        special_char = random.choice(special_chars)
        variations.add(base_word + special_char + random_number)
        mixed_case_word = ''.join(random.choices(string.ascii_letters, k=len(base_word)))
        variations.add(mixed_case_word + random.choice(special_chars) + random.choice(string.digits))
        return variations

    def generate_combination_variations(base_word1, base_word2):
        variations = set()
        combined_word = base_word1 + base_word2
        variations.add(combined_word + random.choice(string.ascii_letters + string.digits))
        variations.add(combined_word + random.choice(special_chars) + random.choice(string.ascii_letters))
        number = random.randint(1000, 9999)
        variations.add(combined_word + str(number))
        random_number = ''.join(random.choices(string.digits, k=3))
        special_char = random.choice(special_chars)
        variations.add(combined_word + special_char + random_number)
        mixed_case_word = ''.join(random.choices(string.ascii_letters, k=len(combined_word)))
        variations.add(mixed_case_word + random.choice(special_chars) + random.choice(string.digits))
        return variations

    print("Generating passwords...")
    
    base_words = sanitize_base_words(base_words)  # Sanitize base words before generating passwords
    
    while len(passwords) < num_passwords:
        if random.choice([True, False]):
            base_word = random.choice(base_words)
            variations = generate_single_word_variations(base_word)
        else:
            base_word1 = random.choice(base_words)
            base_word2 = random.choice(base_words)
            if base_word1 != base_word2:
                variations = generate_combination_variations(base_word1, base_word2)
            else:
                continue

        for variation in variations:
            if len(passwords) < num_passwords:
                passwords.add(variation)
    
    print(f"Generated {len(passwords)} unique passwords.")

    return list(passwords)

# Example usage
def get_base_words():
    print("Enter base words separated by spaces (e.g., 'password admin june '): ")
    words = input().split()
    return words

def get_output_file_location():
    print("Enter the full file path where you want to save the passwords (e.g., 'C:\\Users\\Jinx\\Documents\\password.txt'):")
    file_path = input()
    return file_path

# Execution
base_words = get_base_words()
passwords = generate_passwords(base_words, num_passwords=100000)
output_file = get_output_file_location()

try:
    with open(output_file, 'w') as f:
        for pwd in passwords:
            f.write(f"{pwd}\n")
    print(f"Passwords successfully saved to '{output_file}'.")
except Exception as e:
    print(f"An error occurred while saving the file: {e}")
