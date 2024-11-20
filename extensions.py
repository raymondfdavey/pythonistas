
#! W1C1 EXTENSIONS

# DECODER 1



# This encoding puts 3 random letters or white space between each true string value
# For example, "python#is#great" becomes "p*y*t*h*o*n*#*i*s*#*g*r*e*a*t"
encoded_message_3 = "p7x yf@t2% hZq!o&m nab i:)[ s1.* g3$;r@l#e7x[a8!t"
decoded_message_3 = ""
encoded_message_4 = "w9$!i*& nZ4%t?~ e2@[r7)  ^8#i:+ s!3( _X%[c$;*o1~ m&5#i8% n.@!g"
decoded_message_4 = ""

# Your solution here...
print("Decoded message 3:", decoded_message_3)
print("Decoded message 4:", decoded_message_4)



#! W1C2 EXTENSIONS

# Golden Ratio Approximation
# Calculate and display the ratio of consecutive Fibonacci numbers
# This ratio converges to the Golden Ratio (approximately 1.618033988749895)
num_elements = 20
# Your solution here...
# Hint: Calculate the ratio of each pair of consecutive numbers in the sequence
# and print it. Notice how it gets closer to the Golden Ratio as the sequence progresses.

# Fibonacci Sequence Reversal
# Given a Fibonacci number, find the two preceding numbers in the sequence
target_number = 144
# Your solution here...
# Hint: You may need to use a loop to generate Fibonacci numbers until you reach
# or exceed the target number.


#! W3C1 EXTENSIONS

# Lottery Simulation Extension Challenge

# Building on your previous lottery functions, let's create a more comprehensive lottery simulation.
# This extension will involve generating multiple tickets, simulating draws, and analyzing the results.

# Part A: Multiple Ticket Simulation

# Create a function simulate_lottery(num_tickets) that does the following:
# 1. Generate a single winning ticket using your previous function.
# 2. Generate the specified number of player tickets (num_tickets).
# 3. Check each player ticket against the winning ticket and calculate the winnings for each ticket.
# 4. Calculate and return the total winnings and a breakdown of wins in each category.

# Hints:
# - Use your previously created functions: gen_random(), generate_ticket(), and check_win().
# - You may want to use a dictionary to keep track of the number of wins in each category.
# - Remember to sum up the winnings from all tickets.

# Example usage:
# total_winnings, win_breakdown = simulate_lottery(10)
# print(f"Total winnings: £{total_winnings}")
# print("Win breakdown:")
# for prize, count in win_breakdown.items():
#     print(f"  £{prize} wins: {count}")

# Part B: Jackpot Wait Time Simulation

# Create a function simulate_until_jackpot(num_tickets) that does the following:
# 1. Generate a set number of player tickets (num_tickets) and keep them constant.
# 2. Repeatedly generate new winning numbers (simulating weekly draws) and check against the player tickets.
# 3. Keep track of how many draws (weeks) it takes before one of the player tickets hits the jackpot (£1,000,000 win).
# 4. Return the number of weeks it took to hit the jackpot.

# Hints:
# - Use a while loop that continues until a jackpot is found.
# - Generate new winning numbers in each iteration of the loop.
# - Be careful! This simulation might take a long time to run. Consider adding a maximum number of weeks.

# Example usage:
# weeks_to_jackpot = simulate_until_jackpot(1000)
# print(f"It took {weeks_to_jackpot} weeks for one of the 1000 tickets to hit the jackpot!")

# Bonus Challenge:
# Modify your simulation to run multiple times (e.g., 100 simulations) and calculate the average number
# of weeks needed to hit a jackpot with a fixed set of tickets. This will give you a more reliable estimate of the odds.

# Remember to test your code and handle any potential errors!

# Your code here...

#! W3C2 EXTENSIONS

# Word Guessing Game

# In this challenge, we'll create a word guessing game similar to Hangman.
# The rules are:
# • A word is selected at random from a predefined list.
# • The user then has a maximum number of attempts to guess the word letter by letter.
# • If the user guesses a correct letter, all instances of that letter in the word are revealed.
# • If the user guesses incorrectly, they lose an attempt.
# • If the user enters a letter they've already guessed, a message is shown and the attempt count is not increased.
# • The user can quit the game by entering '-1'.

# All user guesses should be stored in a list for convenience.

# To build this game, divide the functionality into these functions:

# • generate_word(): should return a randomly selected word from a predefined list.

# • analyse_guess(word, guess): should take the word and the user's guessed letter as parameters.
#   It should return True if the letter is in the word, False otherwise.

# • check_previous(guessed_letters, guess): should take the list of previous guesses and the current guess.
#   It should return True if the guess is already in the list, False otherwise.

# • update_word_state(word, word_state, guess): should take the word, current word state, and guessed letter.
#   It should return an updated word state with the guessed letter revealed if correct.

# • main(): to set up the game and run the main game loop.

# Hints:
# - Use underscores to represent unrevealed letters in the word state.
# - current_word_state = ["_"] * len(word_to_guess) will create a string of underscored equal to the word to guess length
# - Remember to handle both uppercase and lowercase letter inputs.
# - You can use a list of words like: ["python", "programming", "computer", "algorithm", "function", "variable"]
# - The random.choice() function can be used to select a random word from the list.
# - You can use an empty return to exit the main() function or break to break out of a loop
# - Word state: This is a string representing the current revealed state of the word to be guessed.
# - For example, if the word is "python" and the player has guessed 'p' and 'n',
# - the word state would be "p____n".

# - Your code here...

# Remember to test your game thoroughly!

#! W5C1 EXTENSION

# Advanced allergen Warning 

# For this extension challenge, we shall enhance our solution for the small café to include a better allergen warning system. 
# The following classes will need to be modified or added:

# • Customer: add capability to store customer allergies.
# • Item: add capability to store allergens present in the item.
# • Order: enhance to check for allergen conflicts and provide warnings.

# You should also be aware of the following additional business logic:

# • Customers may have multiple allergies, which should be stored and checked against all ordered items.
# • Each food or drink item may contain multiple allergens.
# • When an order is placed, the system should check if any ordered items contain allergens that the customer is allergic to.
# • If an allergen conflict is detected, a warning should be generated and included in the order summary.
# • The allergen warning should not prevent the order from being placed, but should clearly inform the customer of potential risks.

# Your task is to modify the existing classes and implement any new methods necessary to accommodate this allergen warning system. The main() function should be updated to demonstrate the new functionality.

# When you have it working, the output for an order with allergen warnings should look something like this:

# ```
# Customer: Alice (Allergies: nuts, lactose)
# Total items ordered: 3
# Black tea £2.00, large, Earl Gray
# Club sandwich £4.50, brown bread, chicken and bacon filling
# Chocolate cake £3.50, medium slice, chocolate (Warning: contains nuts!)

# Today you saved £0.30
# Total cost: £9.70

# Allergen Warnings:
# - Warning: Chocolate cake contains nuts, which you are allergic to.
# - Warning: Club sandwich contains lactose, which you are allergic to.
# ```
