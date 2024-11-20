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


def test_point(maze, current_x, current_y, move):
    move_x, move_y = move
    new_x, new_y = current_x+move_x, current_y+move_y
    
    # print(current_x, current_y)
    # print(move_x, move_y)
    # print(new_x, new_y)
    if new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:
        return False
    
    maze_at_new_point = maze[new_x][new_y]
    if maze_at_new_point == 1:
        return False
    else:
        return new_x, new_y
    
    
    

def find_path(maze, start_location):
    possible_directions = {"east": [0, 1] , "south": [1, 0], "west": [-1, 0], "north": [0, -1]}
    path = []
    location_x, location_y = start_location
    goal = [7, 7]
    
    print(location_x, location_y)
    while [location_x, location_y] != goal:
    # for i in range(3):
        print("\n")
        for direction in possible_directions.keys():
            move_outcome = test_point(maze, location_x, location_y, possible_directions[direction])
            print(move_outcome)
            if move_outcome:
                location_x, location_y = move_outcome
                path.append(direction)
                print("moving: ", direction)
                break
            else: 
                print("can't move: ", direction)
        
    print("MAZE COMPLETE!!!!!!!")    
        
     
    return path
    # You code here...

def display_path(path):
    print("PATH TO SUCCESS:")
    for i, move in enumerate(path):
        print(f'{i}: {move}')


def main():
    """Main program - using the 'if __name__ == "__main__":' construct below
    ensures that the code in main() is only run when you call this file as a
    script, but not when it is imported as a module."""
    maze = setup_maze()  # maze is a 2D list
    initial_location = 0, 0  # 2-tuple to hold current location as (row, column) indices

    # Functions for you to implement...
    # path should be a stack returned by find_path()...

    path = find_path(maze, initial_location)
    display_path(path)

if __name__ == "__main__":
    main()
