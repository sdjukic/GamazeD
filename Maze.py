import yaml

class Maze(object):
	"""Main class of our game."""
	def __init__(self, path_to_conf_file):
		stream = open(path_to_conf_file, 'r')
		values = yaml.load(stream)
		# Use keys in the values dict to initialize members of the class
