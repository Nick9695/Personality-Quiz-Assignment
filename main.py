# This is a simple python code for personality question list

print("Welcome to Personality Quiz!!")
print('You will need to answer some questions :')

# Ask for the first name
while True:
    print('First please tell your First name: ')
    name = input()

    if name:
        if all(char.isalpha() or char.isspace() for char in name):
            print('Thanks for the input!!')
            break
        else:
            print('Please enter a valid name !!')
    else:
        print('Please enter a valid name!!')

# Ask for the age
while True:
    print('Now please tell your Age')
    Age = input()

    if Age:
        if Age.isdigit():
            birthdate = int(Age)
            print("Thanks for input")
            break
        else:
            print("Please enter a valid data!!")
    else:
        print("Please enter a valid data!!")

