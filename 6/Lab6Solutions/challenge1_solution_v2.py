"""A refined version of the simple random maze solver."""

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
    n_rows, n_cols = len(maze), len(maze[0])
    goal = (n_rows - 1, n_cols - 1)

    path = []  # Empty list
    # Here we define the changes in row and column for each direction
    directions = [('N', (-1, 0)), ('S', (1, 0)), ('E', (0, 1)), ('W', (0, -1))]
    name, (dr, dc) = ('E', (0, 1))  # Initial direction and changes in row and column

    while location != goal:  # Tuple to tuple comparison

        row, col = location
        # Using the changes in row and column, we can calculate the next
        # location without the need for many if statements
        next_row, next_col = row + dr, col + dc

        # In Python, we can check if a value is between two other values using
        #  lower <= value <= upper
        if 0 <= next_row < n_rows \
            and 0 <= next_col < n_cols \
            and maze[next_row][next_col] == 0:

            path.append(name)
            location = (next_row, next_col)
        else:
            # We can get a new direction directly from the list without needing
            # an index by using random.choice()
            possible_directions = [d for d in directions if d[0] != name]
            name, (dr, dc) = random.choice(possible_directions)

    return path

def display_path(path, compact=True):
    """Prints a list of all the directions we took."""

    print('List of directions followed:')
    # For this simple algorithm, we could print out a compact version of the path
    if compact:
        tidy_path = [path[0]]
        for i in range(1, len(path)):
            if path[i] != path[i - 1]:
                tidy_path.append(path[i])
        print("Tidy path:", ','.join(tidy_path))
    else:
        print("Full path:", ','.join(path))

def display_maze(maze):
    """Prints the maze."""
    for row in maze:
        print(row)


def main():
    """Main program - using the 'if __name__ == "__main__":' construct below
    ensures that the code in main() is only run when you call this file as a
    script, but not when it is imported as a module."""
    maze = setup_maze()  # maze is a 2D list
    initial_location = 0, 0  # 2-tuple to hold current location as (row, column) indices
    maze = setup_maze()

    # Functions for you to implement...
    # path should be a stack returned by find_path()...
    path = find_path(maze, initial_location)
    display_path(path)

if __name__ == "__main__":
    main()
