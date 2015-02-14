import yaml
from Geometry import Point, LineSegment
from Ball import Ball

class Maze(object):
    """Main class of our game."""
    def __init__(self, path_to_conf_file):
        stream = open(path_to_conf_file, 'r')
        values = yaml.load(stream)
        self.balls = []
        self.walls = []

        for key in values:
            if key == 'Ball':
                self.balls.append(Ball(values[key]))
            elif key == 'walls':
                for index in range(0, len(values[key]), 2):
                    self.walls.append(LineSegment(values[key][index], values[key][index+1]))
            else:
               setattr(self, key, values[key])
        
    def _parse_walls():
        """Function that will make line segment out of walls."""


        


   
