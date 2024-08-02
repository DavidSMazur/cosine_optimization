import numpy as np
import time

def getDotProduct(vector1, vector2): 
    return np.dot(vector1,vector2)

def cosineSimilarity(vector1,vector2):
    dotProduct = getDotProduct(vector1,vector2)
    norm1=np.linalg.norm(vector1)
    norm2=np.linalg.norm(vector2)
    return dotProduct / (norm1 * norm2)

def normalizeVector(vector):
    norm =  np.linalg.norm(vector)
    return vector/norm

    newVector=[]
    for i in range(len(vector)):
        newVector.append(vector[i])
    print(norm)
    return newVector

def normalizeIndex(index):
    newIndex=[]
    for i in range(len(index)):
        newIndex.append(normalizeVector(index[i]))
    return newIndex


def unoptimized(vector, index):
    scores = []
    start_time = time.time()

    #run time begins
    for i in range(len(index)):
        dist = cosineSimilarity(vector,index[i])
        scores.append((index[i].tolist(),dist))

    runTime = time.time() - start_time
    print("Unoptimized: " + str(runTime))
    return (scores,runTime)

def optimized(vector, index):
    scores = []
    newIndex = normalizeIndex(index)
    vector = normalizeVector(vector)
    start_time = time.time() 

    #run time begins
    for i in range(len(newIndex)):
        dist = getDotProduct(vector,newIndex[i])
        scores.append((index[i].tolist(),dist))

    runTime = time.time() - start_time
    print("Optimized: " + str(runTime))
    return (scores,runTime)

def rank(scores):
    return sorted([scores],key=lambda x: x[1])

