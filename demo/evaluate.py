import numpy as np
import time
import similarity as sim


# create test data

numberVectors=1000000
dimensions= 128

index=[]
query = np.array([i for i in range(0, dimensions)])

for i in range(numberVectors):
    random_vector = np.random.rand(dimensions)
    index.append(random_vector)

print("Number of vectors: " + str(len(index)) + "\n\n")

# run

score1, time2=sim.unoptimized(query,index)
score2, time1=sim.optimized(query,index)


# results

percent_change=(time2-time1)/time1
print("\nPercent change: " + str(percent_change))


def errors(score1,score2):
    rankedScore1=sim.rank(score1)
    rankedScore2=sim.rank(score2)
    count = 0
    for i in range(len(rankedScore1)):
        if rankedScore1[i][0]!=rankedScore2[i][0]:
            count+=1
    return count


print("Number of Errors: " + str(errors(score1,score2)))