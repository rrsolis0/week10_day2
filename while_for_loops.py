#  while loop = excute some code WHILE some conditions remains true
# while loops and for loops are forms of iteration 
# iteration is the process of repeating or looping through a set of instruction
# to iterate is the verb form of iteration
# be careful of infinite loops
# they will crash your program and you will have to restart it
# infinite loops are loops that never end



# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")


# print(f"Hello {name}") #not inside the while loop

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit)")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like (q to quit)")

# print("bye")

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"Your number is {num}")

##################### For loops ################################
# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

# for x in reversed(range(1, 11)):
#     print(x)
# print("HAPPY NEW YEAR")

# for x in range (1,11,3):
#     print(x)

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# for x in range (1,21):
#     if x == 13 or x == 15 or x == 19:
#         break
#         # continue #continue skips over it
#     else: print(x)

# challenge1
horror_movies = ['The Exorcist','The Shining','The Conjuring','The Ring']
# loop through the list of horror_movies
# if the name is 'The Shining', print 'The Shining'
# otherwise, print 'The Shining was not found!' and print out the other names using a loop

for movie in horror_movies:
    if movie == 'The Shining':
        print('The Shining is found!')
        print(movie)
        break
    else:
        print("The Shining is not found!")
        print(movie)


    
# challenge2
# create a list of your favorite horror movie chracaters 
# if the name is 'Freddy Kruger', skip over
# otherwise, print out the name of the character
horror_characters = ['Freddy Kruger','Chucky', 'Pennywise','Ghostface']
for character in horror_characters:
    if character == 'Freddy Kruger':
        continue
    else:
        print(character) 

# challenge 3
# create a list of your favorite horror monsters
# loop through the list of name
# if the name is for example, "swamp thing", replace it with another name
# otherwise, print out the  name of the monster
        
horror_monsters = ['swamp thing', 'The Possum marionette', 'Raatma', 'The Man With Fire in His Face']

for monster in horror_monsters:
    if monster == 'swamp thing':
        horror_monsters[0] = 'Frankenstein'
        print(horror_monsters)
    else: 
        print(monster)
