import math

numTilings = 8
tileSize = 0.6
oneDimensionTileCount = 11

def tilecode(in1,in2,tileIndices):
	for i in range(numTilings):
		# Calculate the translated coordinates in the current tiling
		newX, newY = getTranslatedCoordinates(in1, in2, i)
		# Calculate the index of the coordinates in the current tiling
		tileIndices[i] = getTileIndices(newX, newY, i)
		
    
def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)

# Translate the given coordinates from the input space to coordinates in the 
# tiling with index tileIndex and return the pair of translated coordinates
def getTranslatedCoordinates(in1, in2, tileIndex):
	shiftValue = (tileIndex * tileSize) / numTilings
	index1 = in1 + shiftValue
	index2 = in2 + shiftValue
	return index1, index2

# Calculate the index of the coordinates given a point in the tiling space with
# index tileIndex
def getTileIndices(x, y, tileIndex):
	# Calculate the starting tile index
	startingIndex = (oneDimensionTileCount * oneDimensionTileCount) * tileIndex
	# Calculate the indicies of the point in the perspective of the current tiling
	tileIndex1 = math.floor(x / tileSize)
	tileIndex2 = math.floor(y / tileSize)
	# Find the row offset from the starting tile
	rowOffset = oneDimensionTileCount * tileIndex2
	# Return the index of the point in the array containing all points of all tilings
	return startingIndex + rowOffset + tileIndex1

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
    
