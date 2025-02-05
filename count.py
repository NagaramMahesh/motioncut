#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     02-02-2025
# Copyright:   (c) User 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def count_words(text):

    words = text.split()  # Splitting text into words based on spaces
    return len(words)

def main():

    print("📖 Welcome to the Word Counter Program! 📖")

    user_input = input("Enter a sentence or paragraph: ").strip()

    if not user_input:
        print(" Error: No text entered. Please try again with a valid input.")
        return

    # Count words and  the output
    word_count = count_words(user_input)
    print(f"\n Word Count: {word_count}")
    print(" Thank you for using the Word Counter Program! ")

# Run the program
if __name__ == "__main__":
    main()
