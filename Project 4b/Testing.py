from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

def q5():
    print "Q5: PenData Running:"
    print "--------------------"

    penResults = []
    for i in range(5):
        penResults.append(testPenData()[1])
    print "--------------------"

    print "Max: ", max(penResults)
    print "Average: ", average(penResults)
    print "Standard Deviation: ", stDeviation(penResults)

    print "--------------------"

    print("Car Data")
    print("--------------------")
    carResults = []
    for i in range(5):
        carResults.append(testCarData()[1])

    print "Max: ", max(carResults)
    print "Average: ", average(carResults)
    print "Standard Deviation: ", stDeviation(carResults)

def q6(function):

    print "Q6: PenData Running:"
    print "--------------------"

    acc = {}
    for numPercepts in range(0, 41, 5):
        acc[numPercepts] = []
        for i in range(0, 5):
            nnet, error = function([numPercepts])
            acc[numPercepts].append(error)

    print acc
    print "~~~~~~~~~~~~~~~~~~~~DATA~~~~~"
    for numPercepts in range(0, 41, 5):
        runs = acc[numPercepts]
    print numPercepts
    print "   Max:", max(runs)
    print "   Average:", average(runs)
    print "   Standard Deviation:", stDeviation(runs)

q6(testPenData)
q6(carData)

