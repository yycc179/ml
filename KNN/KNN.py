from numpy import *
import operator
import os

def createDataSet():
    group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']  # four samples and two classes
    return group, labels


def KNNClassify(newInput, dataSet, labels, k):
    numSamples = dataSet.shape[0]  # shape[0] stands for the num of row

    ## step 1: calculate Euclidean distance
    # tile(A, reps): Construct an array by repeating A reps times
    # the following copy numSamples rows for dataSet
    diff = tile(newInput, (numSamples, 1)) - dataSet  # Subtract element-wise
    squaredDiff = diff ** 2  # squared for the subtract
    squaredDist = sum(squaredDiff, axis=1)  # sum is performed by row
    distance = squaredDist ** 0.5

    ## step 2: sort the distance
    # argsort() returns the indices that would sort an array in a ascending order
    sortedDistIndices = argsort(distance)

    classCount = {}  # define a dictionary (can be append element)
    for i in xrange(k):
        ## step 3: choose the min k distance
        voteLabel = labels[sortedDistIndices[i]]

        ## step 4: count the times labels occur
        # when the key voteLabel is not in dictionary classCount, get()
        # will return 0
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    ## step 5: the max voted class will return
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key

    return maxIndex


def img2vector(filename):
    rows = 32
    cols = 32
    imgVector = zeros((1, rows * cols))
    fileIn = open(filename)
    for row in xrange(rows):
        lineStr = fileIn.readline()
        for col in xrange(cols):
            imgVector[0, row * 32 + col] = int(lineStr[col])

    return imgVector


def loadDataSet():
    print "---getting traning set..."
    dataSetDir = './knn/'
    trainingFileList = os.listdir(dataSetDir + 'trainingDigits')
    numSamples = len(trainingFileList)

    train_x = zeros((numSamples, 1024))
    train_y = []
    for i in xrange(numSamples):
        filename = trainingFileList[i]

        train_x[i, :] = img2vector(dataSetDir + 'trainingDigits/%s' % filename)

        label = int(filename.split('_')[0])
        train_y.append(label)

    print "---Getting testing set..."
    testingFileList = os.listdir(dataSetDir + 'testDigits')
    numSamples = len(testingFileList)
    test_x = zeros((numSamples, 1024))
    test_y = []
    for i in xrange(numSamples):
        filename = testingFileList[i]
        test_x[i, :] = img2vector((dataSetDir + 'testDigits/%s' % filename))

        label = int(filename.split('_')[0])
        test_y.append((label))

    return train_x, train_y, test_x, test_y


def testHandWritingClass():
    print 'step 1: load data...'
    train_x, train_y, test_x, test_y = loadDataSet()

    print 'step 2: training...'
    pass

    print 'step 3: testing...'
    numTestSamples = test_x.shape[0]
    matchCount = 0
    for i in xrange(numTestSamples):
        predict = KNNClassify(test_x[i], train_x, train_y, 3)
        if predict == test_y[i]:
            matchCount += 1
        else:
            print 'predict: %d, test: %s' % (predict, test_y[i])

    accuracy = float(matchCount) / numTestSamples

    print 'step 4: show the result...'
    print 'the classify accuracy is: %.2f%%' % (accuracy * 100)

testHandWritingClass()
# m = zeros((1, 2))
# m[0, 1] = 2
# print m
# b = tile(m, (2, 1))
# print b
# c = b ** 2
# print c
# d = sum(c, axis=1)
# print d
# e = d ** 0.5
# print e
# print argsort([1,5,3])