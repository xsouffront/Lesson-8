# Do not change the code below.

manual = '''Instructions:
 - To set up the game, place ten dog tokens in the yard and one cat token in the cat house.
 - Each dog character meows every time it sees a cat character.
 - All cat characters will bark at and chase all dog characters.
 - The point of the game is to make sure that all of the cat characters avoid being put in the cat pound.
 - Each of the dog characters has nine lives. Each of the cat characters has only one life.
 - Each cat character is the human's best friend and chases their own tail in circles.
'''

# Implement your algorithm here to switch all instances of the word 'dog' and the word 'cat'.
manual = manual.replace('dog', 'Xavier')
manual = manual.replace('cat', 'dog')
manual = manual.replace('Xavier', 'cat')


# Do not change any code below this line.

print(manual)