from Geometry import Point

class Ball(object):
    """Class that represents ball in our maze."""
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                if key == 'Point':
                    self.position = Point(dictionary[key])
                elif key == 'size':
                    self.size = dictionary[key]
            for key in kwargs:
                setattr(self, key, kwargs[key])
