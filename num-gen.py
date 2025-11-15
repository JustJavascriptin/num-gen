import random
import secrets

def generate_random_numbers():
    """
    Demonstrates generating various types of random numbers in Python.
    """
    print("--- Using the 'random' module (general purpose) ---")

    # 1. Random Integer (inclusive range)
    # Generates a number N such that 1 <= N <= 10
    rand_int = random.randint(1, 10)
    print(f"Random integer between 1 and 10: {rand_int}")

    # 2. Random Float between 0.0 and 1.0
    # Generates a number N such that 0.0 <= N < 1.0
    rand_float_01 = random.random()
    print(f"Random float between 0.0 and 1.0: {rand_float_01:.4f}")

    # 3. Random Float in a specified range
    # Generates a number N such that 10.0 <= N <= 20.0
    rand_float_range = random.uniform(10.0, 20.0)
    print(f"Random float between 10.0 and 20.0: {rand_float_range:.4f}")

    # 4. Random element from a list
    fruits = ['apple', 'banana', 'cherry', 'date']
    rand_fruit = random.choice(fruits)
    print(f"Randomly chosen fruit: {rand_fruit}")

    print("\n--- Using the 'secrets' module (cryptographically secure) ---")

    # 5. Secure random integer (for passwords/security tokens)
    # Generates a number N such that 0 <= N < 100
    secure_rand_num = secrets.randbelow(100)
    print(f"Secure random number between 0 and 99: {secure_rand_num}")

    # 6. Secure random token (e.g., for password resets)
    secure_token = secrets.token_hex(16)
    print(f"Secure random hexadecimal token: {secure_token}")

if __name__ == "__main__":
    generate_random_numbers()
