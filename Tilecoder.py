numTilings = 8
tileSize = 0.6
tileOffset = 1 / numTilings
oneDimensionTileCount = 10

def tilecode(in1,in2,tileIndices):
	# Calculate the indicies in each of the tilings
	for i in range(numTilings):
		    
    
def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)

def getTranslatedCoordinated(in1, in2, tileIndex):
	index1 = in1 + (tileIndex * tileSize) / 

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
    
