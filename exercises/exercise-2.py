# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

letter = input('Please enter a word or phrase:').lower()
print(f'The user typed "{letter}" ')
while letter != "quit":
        print(f'What you entered is {len(letter)} characters long')
        letter = input('Please enter a word or phrase: ').lower()