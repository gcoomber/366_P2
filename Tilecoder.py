numTilings = 8
tileSize = 0.6
oneDimensionTileCount = 11

def tilecode(in1,in2,tileIndices):
	# Calculate the indicies in each of the tilings
	for tilingIndex in range(numTilings):
		# get local tile coordinates 
		tileX = int( (in1 + (tilingIndex*tileSize)/numTilings) / 0.6)
		tileY = int( (in2 + (tilingIndex*tileSize)/numTilings) / 0.6)

		# get the local tile number (between 0 and oneDimensionTileCount^2)
		localTileNumber = tileX + tileY*(oneDimensionTileCount)

		# get the global tile number and populate the tileIndices vector
		globalTileNumber = tilingIndex*(pow(oneDimensionTileCount,2)) + localTileNumber
		tileIndices[tilingIndex] = globalTileNumber

def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
    
