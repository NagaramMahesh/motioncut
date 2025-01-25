import random
import string

# Step 1: Define adjective and noun lists
adjectives = ["Cool", "Happy", "Brave", "Lazy", "Silly", "Charming", "Funky", "Clever"]
nouns = ["Tiger", "Dragon", "Unicorn", "Ninja", "Pirate", "Wizard", "Robot", "Fox"]

# Step 2: Function to generate a username
def generate_username(include_numbers=False, include_special=False, length=None):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    # Add numbers if selected
    if include_numbers:
        username += str(random.randint(100, 999))
    
    # Add special characters if selected
    if include_special:
        username += random.choice(string.punctuation)
    
    # Adjust length if specified
    if length and length > len(username):
        extras = ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(username)))
        username += extras

    return username

# Step 3: Save usernames to a file
def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}!")

# Step 4: Interactive user input
def main():
    print("Welcome to the Random Username Generator!")
    
    try:
        num_usernames = int(input("How many usernames would you like to generate? "))
        include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
        include_special = input("Include special characters? (yes/no): ").lower() == "yes"
        length = input("Set a specific length? (Press Enter to skip): ")
        length = int(length) if length else None

        # Generate usernames
        usernames = [generate_username(include_numbers, include_special, length) for _ in range(num_usernames)]
        
        # Display usernames
        print("\nGenerated Usernames:")
        for username in usernames:
            print(username)

        # Save to file
        save_option = input("Save these usernames to a file? (yes/no): ").lower()
        if save_option == "yes":
            save_usernames_to_file(usernames)
    
    except ValueError:
        print("Invalid input. Please enter numbers where required.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
