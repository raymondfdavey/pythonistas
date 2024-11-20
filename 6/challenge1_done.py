# Solution for the simple random maze search 1 problem

import random

def setup_maze():
    """
    Setup an 8x8 maze.
    0 is a square we can move through, 1 is a rock
    """
    return \
        [ [0, 1, 0, 0, 1, 1, 0, 1], \
          [0, 1, 1, 0, 0, 1, 0, 1], \
          [0, 0, 0, 0, 0, 1, 0, 1], \
          [0, 0, 1, 0, 0, 1, 0, 1], \
          [1, 0, 1, 0, 0, 0, 0, 0], \
          [1, 0, 0, 0, 0, 1, 1, 0], \
          [0, 0, 1, 0, 0, 1, 0, 0], \
          [1, 1, 1, 1, 0, 0, 0, 0], \
        ]

def find_path(maze,location):
    solved = False
    current_row, current_column = location
    path = []
    directions = ['right', 'down', 'left', 'up']
    # good_direction = 0

    
    # as long as not solved, repeat the 'move' code below
    while not solved:
        print('IN LOOP 1')
        print(f'DIRCTIONS AT LOOP 1 = ({current_row}, {current_column}')
        
        moved = False
        direction_counter = 0 
        
        while not moved:

            print('in loop 2')
            print(f'DIRCTIONS AT LOOP 2 = ({current_row}, {current_column}')
            
            current_direction = directions[direction_counter]
            
            #try current direction
            if current_direction == 'right':
                if current_column + 1 > len(maze[current_row]) -1: 
                    direction_counter += 1
                    continue
                if maze[current_row][current_column + 1] == 0:
                    print('*********************************moving right')
                    moved = True
                    path.append(current_direction)
                    current_column = current_column + 1
 
                else:
                    direction_counter += 1
                    continue
                
            if current_direction == 'down':
                if current_row + 1 > len(maze)-1: 
                    direction_counter += 1
                    continue
                if maze[current_row +1][current_column] == 0:
                    print('*********************************moving down')
                    moved = True
                    path.append(current_direction)
                    current_row = current_row + 1
                else:
                    direction_counter += 1
                    continue
                
            if current_direction == 'left':
                if current_column - 1 < 0: 
                    direction_counter += 1
                    continue
                if maze[current_row][current_column - 1] == 0:
                    print('*********************************moving left')
                    moved = True
                    path.append(current_direction)
                    current_column = current_column - 1
                else:
                    direction_counter += 1
                    continue
                
            if current_direction == 'up':
                if current_column - 1 < 0: 
                    direction_counter += 1
                    continue
                if maze[current_row - 1][current_column] == 0:
                    print('*********************************moving up')
                    moved = True
                    path.append(current_direction)
                    current_row = current_row - 1
                else:
                    direction_counter += 1
                    continue
                
        if current_row == len(maze)-1 and current_column == len(maze)-1:
            print('SOLVED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            solved = True
    print(path)
             
    return path
    
def display_path(maze, path):
    row, col = (0,0)
    maze[row][col] = 2
    for direction in path:
        if direction == "right":
            col += 1
            maze[row][col] = 2
        elif direction == "down":
            row += 1
            maze[row][col] = 2
        if direction == "left":
            row -= 1
            maze[row][col] = 2
        if direction == "up":
            col -= 1
            maze[row][col] = 2
    for row in maze:
        print(row)
    return maze


def main():
    
    initial_location = 0, 0  # 2-tuple to hold current location as (row, column)
    maze = setup_maze()

    # # Functions for you to implement...
    # # path should be a stack returned by find_path()...

    path = find_path(maze, initial_location)
    display_path(maze, path)

if __name__ == "__main__":
    main()
