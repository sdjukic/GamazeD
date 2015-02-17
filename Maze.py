from Geometry import Point, LineSegment
from Ball import Ball

# directions
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

class Maze(object):
    """Main class of our game."""
    def __init__(self, dict_args):
        """Init expects dictionary of the following form:
           Ball: with three arguments, just as for Ball class;
           Target: with two arguments for Point;
           Wall: with pair of tuples for endpoints for LineSegment.
           e.x. {"Ball": [(3,4,5), (4,5,6)], "Target":[(100,90), (30, 45)],
           "Wall": [((0,0), (250,0)), ((0,0), (0,250))]}"""
        self.balls = []
        self.targets = []
        self.walls = []

        for key in dict_args:
            if key in dict_args:
                if key == 'Ball':
                    for v in dict_args['Ball']:
                        self.balls.append(Ball(v[0], v[1], v[2]))
                elif key == 'Target':
                    for v in dict_args['Target']:
                        self.targets.append(Point(v[0], v[1]))
                elif key == 'Wall':
                    for v in dict_args['Wall']:
                        self.walls.append(LineSegment(v[0], v[1]))



    def move(self, direction):
        """Function that will move all balls in the given direction."""
        ray_distance = 255 # later this will be the length of the maze
        if direction == 'up':
            moving_direction = UP
        elif direction == 'down':
            moving_direction = DOWN
        elif direction == 'left':
            moving_direction = LEFT
        elif direction == 'right':
            moving_direction = RIGHT
        else:
            # Raise some exception
            pass
        
        for ball in self.balls:
            ball_pos = ball.get_position()
            ball_x, ball_y = ball_pos.get_x(), ball_pos.get_y()
            move_ray = LineSegment([ball_x, ball_y], [ball_x + ray_distance * moving_direction[0], ball_y + ray_distance * moving_direction[1]])
            min_distance = float('inf')
            intersection_point = Point(0,0)
            for wall in self.walls:
                intersection_check = move_ray.do_intersect(wall)
                if intersection_check[0] and move_ray._in_segment(intersection_check[1]):
                    intersection_distance = ball_pos.euclidean_distance(intersection_check[1]) 
                    if intersection_distance < min_distance:
                        min_distance = intersection_distance
                        intersection_point = intersection_check[1]
                        # if I place ball here then all checks after the first one will result in
                        # collision since ball will be placed IN the point of the intersection
                        # move it a bit
                        intersection_point.set_x(intersection_point.get_x() - moving_direction[0] * 5)
                        intersection_point.set_y(intersection_point.get_y() - moving_direction[1] * 5)
            
            ball.change_position(intersection_point)
            
      
    def reached_target(self):
        """Function that checks whether all balls in maze reached their target locations."""
        result = []
        # TODO see if list comprehension can be used
        for index in enumerate(self.balls):
            result.append(index[1].get_position().euclidean_distance(self.targets[index[0]]) < 0.05)
          
        return result
                    
params = {}         
params["Ball"] = [(10, 20, 10)]
params["Target"] = [(245,245)]
params["Wall"] = [((0,0), (0,250)), ((0,0), (250,0)), ((250,0),(250,250)), ((0,250),(250,250))]

maze = Maze(params)
