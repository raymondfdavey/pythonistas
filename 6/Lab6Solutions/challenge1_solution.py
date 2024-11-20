"""A simple random maze solver."""

import random


def setup_maze():
    """
    Setup an 8x8 maze.
    0 is a square we can move through, 1 is a rock
    """
    return \
        [                              # Row numbers
            [0, 1, 0, 0, 1, 1, 0, 1],  # 0
            [0, 1, 1, 0, 0, 1, 0, 1],  # 1
            [0, 0, 0, 0, 0, 1, 0, 1],  # 2
            [0, 0, 1, 0, 0, 1, 0, 1],  # 3
            [1, 0, 1, 0, 0, 0, 0, 0],  # 4
            [1, 0, 0, 0, 0, 1, 1, 0],  # 5
            [0, 0, 1, 0, 0, 1, 0, 0],  # 6
            [1, 1, 1, 1, 0, 0, 0, 0],  # 7
        ]  # 0, 1, 2, 3, 4, 5, 6, 7 # Column numbers


def find_path(maze, location):
    """Find a way through the maze using simple random search.
    Returns a list of directions we took to get to the goal."""

    path = []                       # Empty stack
    direction = 'east'              # Initial direction

    while location != (7, 7):       # Tuple to tuple comparison

        row, col = location  # Unpack the tuple into row and column for convenience

        if direction == 'east' and col+1 < 8 and maze[row][col+1] != 1:
            path.append('east')
            col += 1
            location = row, col
        elif direction == 'west' and col-1 >= 0 and maze[row][col-1] != 1:
            path.append('west')
            col -= 1
            location = row, col
        elif direction == 'north' and row-1 >= 0 and maze[row-1][col] != 1:
            path.append('north')
            row -= 1
            location = row, col
        elif direction == 'south' and row+1 < 8 and maze[row+1][col] != 1:
            path.append('south')
            row += 1
            location = row, col
        else:
            # We could not carry on moving in a straight line, so we change direction
            possible_directions = ['north', 'south', 'east', 'west']
            possible_directions.remove(direction)  # Remove the direction we already tried
            x = random.randrange(0, len(possible_directions))  # Get an index for the list
            direction = possible_directions[x]

    # Return the stack containing the directions we took
    return path

def display_path(path):
    """Takes a stack with all the directions we took."""

    # Note `path` is actually a list, but we are treating it as a stack.
    # This implementation is just to show you algorithmically how to reverse
    # a stack (assuming you can not access it from the bottom directly) even
    # though it is unnecessary and we could just print out the list directly.
    # A queue would have been another simpler alternative.

    # Our stack is in reverse order...
    r_path = []
    while len(path) > 0:
        r_path.append(path.pop())

    # Now print out the newly reversed stack...
    print('List of directions followed:')
    while len(r_path) > 0:
        print(r_path.pop())

def main():
    """Main program - using the 'if __name__ == "__main__":' construct below
    ensures that the code in main() is only run when you call this file as a
    script, but not when it is imported as a module."""
    maze = setup_maze()  # maze is a 2D list
    initial_location = 0, 0  # 2-tuple to hold current location as (row, column) indices
    maze = setup_maze()

    # Functions for you to implement...
    # path should be a stack returned by find_path()
    path = find_path(maze, initial_location)
    display_path(path)

if __name__ == "__main__":
    main()
