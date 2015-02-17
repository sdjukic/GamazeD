from Geometry import Point

class Ball(object):
    """Class that represents ball in our maze."""
    def __init__(self, size = 0, *position):
        self.size = size
        self.position = Point(position[0], position[1])

    
    def get_position(self):
        return self.position
        
    
    def change_position(self, new_position):
        self.position = new_position