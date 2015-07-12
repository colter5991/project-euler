cache = {}
#black, red, green, and blue
tileSet = (1,2,3,4)

def numberOfWays(numTiles, tileSet, cache):

	#check to see if this has already been calculated
	data = cache.get(numTiles,None)
	if data != None:
		return data
		
	#This is the base case.  There is only one way to not have
	#any tiles
	elif numTiles == 0:
		return 1
	else:
		ways = 0
		for tile in tileSet:
			if tile <= numTiles: #If the tile isn't too big
				ways += numberOfWays(numTiles-tile, tileSet, cache)
		cache[numTiles] = ways
		return ways
		
print(numberOfWays(50, tileSet, cache))