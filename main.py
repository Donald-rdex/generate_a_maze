import random
from random import randint


class Maze:
    """Maze class, on init generates an empty maze, and then fills with walls"""
    WALL = '#'
    VOID = '.'
    START = 'S'
    TARGET = 'T'

    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.maze = {}
        self.start_pos = (0, 0)
        self.target_pos = (self.width, self.height)

        for x in range(0, self.width):
            for y in range(0, self.height):
                position = (x, y)
                if self.is_wall(position):
                    self.maze[position] = self.WALL
                else:
                    self.maze[position] = "."

        # just to add some variety to the start and target.
        if randint(0, 1):
            self.start_pos = (0, randint(1, self.height - 2))
            self.target_pos = (self.width - 1, randint(1, self.height - 2))
        else:
            self.start_pos = (randint(1, self.width - 2), 0)
            self.target_pos = (randint(1, self.width - 2), self.height - 1)

        self.maze[self.start_pos] = self.START
        self.maze[self.target_pos] = self.TARGET

        # fill the maze with walls!
        self.generate_interior_walls()

    def is_wall(self, position) -> bool:
        """ if the position tuple (x, y) is at a 0 or Width/height boundary return true
        :param: position - (x, y) tuple
        :returns: bool
        """
        if position[0] == 0:
            return True
        elif position[0] == self.width - 1:
            return True
        elif position[1] == 0:
            return True
        elif position[1] == self.height - 1:
            return True

        return False

    def is_next_to_start(self, position) -> bool:
        """Is the position to the right or below start?
        :param: position: the position to check
        """
        right = (position[0] - 1, position[1])
        below = (position[0], position[1] - 1)
        if self.maze[right] == self.maze[self.start_pos]:
            return True
        if self.maze[below] == self.maze[self.start_pos]:
            return True
        return False

    def is_next_to_target(self, position) -> bool:
        """Is the position to the left of (target on the right) or above the target?
        :param: position: the position to check
        """
        left = (position[0] + 1, position[1])
        above = (position[0], position[1] + 1)
        if self.maze[above] == self.maze[self.target_pos]:
            return True
        if self.maze[left] == self.maze[self.target_pos]:
            return True
        return False

    def print_maze(self):
        for position in self.maze.keys():
            print("{}".format(self.maze[position]), end='')
            if position[1] == self.height - 1:
                print("")

    def generate_interior_walls(self, method='sparse'):
        if method == 'sparse':
            self.generate_interior_walls_sparse_blocks()

    def generate_interior_walls_sparse_blocks(self, fill_percent=20):
        """ partially fill the maze with sparse walls
        :param: fill_percent: how much of the total maze area to fill
        """
        walls_to_make = int((self.width - 2) * (self.height - 2) * fill_percent / 100)
        for position in self.maze.keys():
            if not self.is_wall(position) \
                    and not self.is_next_to_start(position) \
                    and not self.is_next_to_target(position) \
                    and random.random() < fill_percent/100:
                self.maze[position] = self.WALL
                walls_to_make -= 1
            if walls_to_make == 0:
                break


if __name__ == '__main__':
    init_w = 10
    init_h = 20
    this_maze = Maze(init_w, init_h)
    this_maze.print_maze()
