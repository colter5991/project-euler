#A dictionary that will use (number_of_tiles, colored_length) as
#its key
cache = {}

#number_of_tiles is the number of spaces left
#colored_length is the number of spaces one colored tile occupies
#cache is a place to store already computed combinations
def numberOfWays(number_of_tiles, colored_length, cache):
	cached_value = cache.get((number_of_tiles, colored_length), None)

	if cached_value != None:
		return cached_value

	# This is the base case of the recursion.  There is no more room
	# for any colored tiles, so all of the remaining tiles must be
	# black tiles.
	elif number_of_tiles < colored_length:
		return 1
	
	else:
		#If the next tile is colored, how many possible combinations
		#are there for the remaining tiles?
		colored = numberOfWays(number_of_tiles-colored_length,
		                       colored_length,
							   cache)
		#If the next tile is black, how many possible combinations
		#are there for the remaining tiles?
		black = numberOfWays(number_of_tiles-1,
							 colored_length,
							 cache)
		
		#The sum of these two is the total number of possibilities
		possibilities =  colored+black
		cache[(number_of_tiles, colored_length)] = possibilities
		return possibilities

# 1 is subtracted because all black is not a valid combination
# according to the problem description
redWays = numberOfWays(50, 2, cache) -1
greenWays = numberOfWays(50, 3, cache) - 1
blueWays = numberOfWays(50,4,cache) - 1

totalWays = redWays + greenWays + blueWays

print(totalWays)