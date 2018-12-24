import numpy as np
import nltk
import operator


# this  fucntion calculate the similarity of word and return a distance which is
# then number of dfferent characters ( like x1 -x2)
def wordsDistance(word, word2):
    if word.lower() == word2.lower():
        return 0
    else:
        return nltk.edit_distance(word.lower(), word2.lower())


# thos function calculate an euclidienne distance between two products
def euclideanDistance(data1, data2):
    ar1 = [data1.name, data1.type, data1.producer, data1.details["ecran"], data1.details["os"], data1.details["cpu"],
           data1.details["memory"], data1.details["ram"], data1.details["reseau"], data1.details["batterie"],
           data1.details["cam"]]
    ar2 = [data2.name, data2.type, data2.producer, data2.details["ecran"], data2.details["os"], data2.details["cpu"],
           data2.details["memory"], data2.details["ram"], data2.details["reseau"], data2.details["batterie"],
           data2.details["cam"]]

    distance = 0
    for x in range(ar1.__len__()):
        distance += np.square(wordsDistance(ar1[x], ar2[x]))
    return np.sqrt(distance)


# this is our KnnModel
def knnModel(trainingSet, testInstance, k):
    distances = {}
    sort = trainingSet
    # first w calculate  distances of our instance from the rest of data set
    for x in range(len(trainingSet)):
        #### Start of STEP 3.1
        dist = euclideanDistance(testInstance, trainingSet[x])

        distances[x] = dist

    # we are going to sort the products from the nearest one to our instance to the furthest
    test = False
    while (test == False):
        test = True
        for x in range(len(trainingSet) - 1):
            if distances[x] > distances[x + 1]:
                aux = distances[x + 1]
                distances[x + 1] = distances[x]
                distances[x] = aux
                aux = sort[x + 1]
                sort[x + 1] = sort[x]
                sort[x] = aux
                test = False

    neighbors = []
    # now we are goiin to take te k-nearest neighbours
    for x in range(k):
        neighbors.append(sort[x])
    classVotes = {}
    # now we are going to vote wich class is this instance ?
    for x in range(len(neighbors)):
        response = neighbors[x].type.lower()

        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1

    # Sort classes bsed on votrs
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    # return result
    return (sortedVotes[0][0])
