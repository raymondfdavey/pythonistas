"""An Object-Oriented version of maze solvers."""

import random
import time
import copy
from abc import abstractmethod

class MazeSolver:
    """Solves a maze."""

    def __init__(self, maze=None, goal=None) -> None:
        """Initialise the maze solver."""
        # This gives us the flexibility to pass in a maze of our own
        if maze is None:
            self.maze = self.setup_maze()
        else:
            self.maze = maze
        self.n_rows = len(self.maze)
        self.n_cols = len(self.maze[0])
        # Similarly, this gives us the flexibility to pass in a different goal
        if goal is None:
            self.goal = (self.n_rows - 1, self.n_cols - 1)
        else:
            self.goal = goal
        # This is now a dictionary mapping directions to changes in row and column
        self.directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
        # Set a limit on the number of steps we can take so we don't get stuck
        self.max_steps = self.n_rows * self.n_cols

    def can_move(self, location, direction):
        """Check if we can move in a direction."""
        row, col = location
        dr, dc = self.directions[direction]
        next_row, next_col = row + dr, col + dc

        return 0 <= next_row < self.n_rows \
            and 0 <= next_col < self.n_cols \
            and self.maze[next_row][next_col] == 0

    @abstractmethod
    def choose_direction(self, location, direction):
        """Choose a direction to move in."""
        # This method implements the core logic of the maze solver which will
        # be different for each algorithm. We therefore make it abstract, so
        # we must implement it in each subclass (while inheriting other common
        # attributes and methods from this class).

    def find_path(self, location, direction='E'):
        """Finds a way through the maze.
        Returns a list of directions we took to get to the goal."""

        path = []  # Empty list

        while location != self.goal and len(path) < self.max_steps:

            direction = self.choose_direction(location, direction)

            # Step forward
            path.append(direction)
            row, col = location
            dr, dc = self.directions[direction]
            location = (row + dr, col + dc)

        if len(path) == self.max_steps:
            print(f"Maximum number of steps ({self.max_steps}) reached!",
                "Could not find a path to the goal!")

        return path

    def display_path(self, path):
        """Prints a list of all the directions we took."""
        print(f'Steps taken: {",".join(path)}')

    def display_maze(self, maze):
        """Prints the maze."""
        print('-' * (self.n_cols + 2))
        for row in maze:
            print('|', end='')
            for value in row:
                if value == 0:
                    print(' ', end='')
                elif value == 1:
                    print('X', end='')
                else:
                    print(value, end='')
            print('|')
        print('-' * (self.n_cols + 2))

    def clear_lines(self, n=1):
        """Clears the last n lines of the terminal."""
        # These are ANSI escape codes to:
        line_up = '\033[1A'  # move the cursor up one line
        line_clear = '\x1b[2K'  # clear the line
        for _ in range(n):
            print(line_up, end=line_clear)

    def animate_path(self, path, initial_location=(0, 0), delay=0.5, symbol='*'):
        """Prints the maze for each move after a delay."""
        maze = copy.deepcopy(self.maze)
        row, col = initial_location
        maze[row][col] = symbol
        print("Animating moves...")
        self.display_maze(maze)

        for step in path:
            # Use deepcopy to make a copy of the maze so we can modify it on
            # each step independently, otherwise the previous locations will
            # still be marked
            maze = copy.deepcopy(self.maze)
            self.clear_lines(self.n_rows + 2)  # Clear the maze from the terminal

            dr, dc = self.directions[step]
            row, col = row + dr, col + dc
            maze[row][col] = symbol
            self.display_maze(maze)
            time.sleep(delay)
        
        if (row, col) == self.goal:
            print("Goal reached!")
        else:
            print("Could not find a path to the goal!")

    def setup_maze(self):
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


class RandomMazeSolver(MazeSolver):
    """Solves a maze by continuing forward until blocked and choosing a random
    direction. Increases the maximum number of steps by a factor of 10."""
    def __init__(self, maze=None, goal=None, seed=None) -> None:
        super().__init__(maze, goal)
        if seed is not None:
            random.seed(seed)
        self.max_steps *= 10

    def choose_direction(self, location, direction):
        if not self.can_move(location, direction):
            choices = [d for d in self.directions if self.can_move(location, d)]
            direction = random.choice(choices)
        return direction


class LeftWallFollowerMazeSolver(MazeSolver):
    """Solves a maze by following the left wall."""

    def turn_left(self, direction):
        """Turn left and return the new direction."""
        left_turn = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}
        return left_turn[direction]

    def choose_direction(self, location, direction):
        """Choose a direction to move in by following the left wall."""
        # Get all directions by rotating anti-clockwise
        forward = direction
        left = self.turn_left(direction)
        backward = self.turn_left(left)
        right = self.turn_left(backward)

        # Choose direction, prioritising left, forward, right, backward
        if self.can_move(location, left):       # _<*
            direction = left                    #  |
        elif self.can_move(location, forward):  # |^
            pass                                # |*
        elif self.can_move(location, right):    #  _
            direction = right                   # |* >
        else:                                   #  _
            direction = backward                # |*|

        return direction


class RightWallFollowerMazeSolver(LeftWallFollowerMazeSolver):
    """Solves a maze by following the right wall."""

    def choose_direction(self, location, direction):
        """Choose a direction to move in by following the right wall."""
        # Get all directions by rotating anti-clockwise
        forward = direction
        left = self.turn_left(direction)
        backward = self.turn_left(left)
        right = self.turn_left(backward)

        # Choose direction, prioritising right, forward, left, backward
        if self.can_move(location, right):
            direction = right
        elif self.can_move(location, forward):
            pass
        elif self.can_move(location, left):
            direction = left
        else:
            direction = backward

        return direction


def main():
    """Main program - using the 'if __name__ == "__main__":' construct below
    ensures that the code in main() is only run when you call this file as a
    script, but not when it is imported as a module."""

    initial_location = 0, 0  # 2-tuple to hold current location as (row, column) indices

    # Uncomment one of the solvers below to try a different algorithm
    # For RandomMazeSolver seed=None means we get a different path every time,
    # setting it to a number e.g. seed=42 means we get the same path every time
    solver = RandomMazeSolver(seed=None)
    # solver = LeftWallFollowerMazeSolver()
    # solver = RightWallFollowerMazeSolver()

    path = solver.find_path(initial_location)
    solver.display_path(path)
    solver.animate_path(path)

if __name__ == "__main__":
    main()
