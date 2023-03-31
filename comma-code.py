# Write a function that takes a list value and returns a string with all items 
# separated by a comma and a space with 'and' inserted before the last item

def comma_func(raw_list):
    # Create an empty string
    new_string = ''
    # Prevent an empty list from going through the loop
    if not raw_list:
        print('List must not be empty.')
    
    # Prevent a single item list from going through the loop
    elif len(raw_list) == 1:
        print('One item does not make a list.')

    else:
        # Loop through all items and add them to the empty string with a comma
        # Stop before the last item
        for item in raw_list[:-1]:
            new_string += item + ', '

        # Add the final item to the string with 'and'
        new_string += 'and ' + str(raw_list[-1]) 
        print(f'Your list: {new_string}.')

# Create an empty list
new_list = []
print('Enter a word to add it to a list. Enter a blank space when you are finished.')
while True:
    user_input = input()
    # Check if user input is a single word with no spaces
    if user_input.isalpha() and ' ' not in user_input:
        # Add the word to the empty list
        new_list.append(user_input)
        # Continue to take user input
        continue
    # End the loop if a blank space is entered
    # Pass the list into the comma function
    elif user_input == '':
        comma_func(new_list)
        break
    # Prevent user from entering numbers and symbols
    else:
        print('Invalid input.')
        continue
