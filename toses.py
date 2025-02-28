#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     28-02-2025
# Copyright:   (c) User 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_tosses(n):
    heads_count = 0
    tails_count = 0

    for _ in range(n):
        result = coin_toss()
        print(result)
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    total = heads_count + tails_count
    print("\nResults:")
    print(f"Heads: {heads_count} ({(heads_count/total)*100:.2f}%)")
    print(f"Tails: {tails_count} ({(tails_count/total)*100:.2f}%)")

def main():
    while True:
        try:
            flips = int(input("Enter the number of coin tosses: "))
            if flips <= 0:
                print("Please enter a positive integer.")
                continue
            multiple_tosses(flips)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        repeat = input("Do you want to play again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
