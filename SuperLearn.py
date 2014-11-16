from pylab import zeros, sin, cos, normal, random
from Tilecoder import numTilings, tilecode

# initialize weights appropriately here
# initialize step size parameter appropriately here
# initialize your global list of tile indices here
weights = zeros(968)
stepSize = 0.1
tileIndices = [-1] * 8

def f(in1,in2):
    tilecode(in1, in2, tileIndices)
    # Calculate the estimated function value for the inputs in1, in2
    f = 0
    for index in tileIndices:
    	f += weights[index]
    return f
    	
def learn(in1,in2,target):
    global stepSize
    global weights
    # Update step size
    #stepCount += 1
    #stepSize = 1/stepCount
    #stepSize = 0.1
    fValue = f(in1, in2)
    # Update weights
    for index in tileIndices:
    	weights[index] = weights[index] + stepSize * (target - fValue)
    #stepSize /= 2

def test1():
   for in1,in2,target in \
         [ (0.1, 0.1, 2.0), \
           (4.0, 2.0, -1.0), \
           (5.99, 5.99, 3.0), \
           (4.0, 2.1, -1.0) ]:
        before = f(in1,in2)
        learn(in1,in2,target)
        after = f(in1,in2)
        print('Example (', in1, ',', in2, ',', target, '):', end=' ') 
        print('    f before learning: ', before, end=' ') 
        print('    f after learning : ', after)
    
def targetFunction(in1,in2):
    return sin(in1-3.0)*cos(in2) + normal(0,0.1)

def train(numSteps):
    for i in range(numSteps):
        in1 = random() * 6.0
        in2 = random() * 6.0
        target = targetFunction(in1,in2)
        learn(in1,in2,target)
    
def writeF(filename):
    fout = open(filename, 'w')
    steps = 50
    for i in range(steps):
        for j in range(steps):
            target = f(i * 6.0/steps, j * 6.0/steps)
            fout.write(repr(target) + ' ')
        fout.write('\n')
    fout.close()
        
def MSE(sampleSize):
    totalSE = 0.0
    for i in range(sampleSize):
        in1 = random() * 6.0
        in2 = random() * 6.0
        error = targetFunction(in1,in2) - f(in1,in2)
        totalSE = totalSE + error * error
    print('The estimated MSE: ', (totalSE / sampleSize))
    
def test2():
    train(20)
    writeF('f20')
    MSE(10000)
    for i in range(10):
        train(1000)
        MSE(10000)
    writeF('f10000')

test2()

