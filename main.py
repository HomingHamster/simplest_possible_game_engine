# (c) 2024 Felix Farquharson
# This code is licensed under MIT license (see LICENSE.txt for details)

# SIMPLEST POSSIBLE GAME ENGINE IN PYTHON

# Please give me money:
# BTC: bc1qwm3rswv0xcunchw9q72mnsmxjzkhfdkwr0vlgu
# LTC: LdRc7Fz6poAuWvXexzGP4sQ7SFvn6uPuuX
# Card: https://buy.stripe.com/00g00m6e1gEW68E4gk

character_x = 0  # Initialize character's X position
character_y = 0  # Initialize character's Y position
screen_size_x = 10  # Define screen width
screen_size_y = 10  # Define screen height

# Function to render the game screen
def render_screen():
    for y in range(screen_size_y): #loop over the number of lines
        for x in range(screen_size_x): #loop over the number of pixels in that line
            if character_y == y and character_x == x:
                print("X", end="")  # Highlight character's position with "X"
            else:
                print(".", end="")  # Display empty cells with "."
        print("")  # Move to the next row

# Main game loop
while True:
    render_screen()  # Render the game screen
    key = input("Direction to move: ")  # Capture user input for movement

    # Update character's position based on user input
    if key == "w":
        character_y -= 1  # Move character up
    elif key == "a":
        character_x -= 1  # Move character left
    elif key == "s":
        character_y += 1  # Move character down
    elif key == "d":
        character_x += 1  # Move character right
    elif key == "q":
        break  # Exit the game if 'q' is pressed