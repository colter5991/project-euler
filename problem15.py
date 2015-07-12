# Each point in the grid can be accessed from either the point directly
# above it, or the point directly to the left of it.  So the number of
# ways to get to a point is the sum of the number of ways to get to
# the point above it and the number of ways to get to the point to
# the left of it.

#A grid to store the number of possible paths to each point
class Grid:
	def __init__(self, width, height):
		self.data = [0]*width*height
		self.width = width
		self.height = height
		
	def get(self, x, y):
		if x<0 or y<0:
			return 0
		else:
			return self.data[x+y*self.width]
		
	def set(self, x, y, value):
		self.data[x+y*self.width] = value

#Create a grid.
grid = Grid(21,21)

#Initialize the first row.  Each point in the first row can only
#be accessed by one path: a path that goes straight to the right.
for x in range(0,21):
	grid.set(x,0,1)

#Determine the number of ways to get to the remaining points.
for y in range(1,21):
	for x in range(0,21):
		number_paths_from_left = grid.get(x-1,y)
		number_paths_from_top = grid.get(x,y-1)
		number_paths = number_paths_from_left + number_paths_from_top
		grid.set(x,y,number_paths)
		
print(grid.get(20,20))