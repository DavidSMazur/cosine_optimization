import numpy as np
import time

print("building random vectors")
start_time = time.time() 

norm_and_vecs=[]
no_norm_vecs=[]
num_vecs=1000000

for i in range(num_vecs):
    random_vector = np.random.rand(1000)
    norm=np.linalg.norm(random_vector)
    #data structure has to remain constant with norm_and_vecs
    no_norm_vecs.append((random_vector,0))
    norm_and_vecs.append((random_vector,norm))

end_time = time.time()
print("vector generation time: " + str(end_time - start_time))

print("Number of vectors without norm: " + str(len(no_norm_vecs)))
print("Number of vectors with norm: " + str(len(no_norm_vecs))+"\n")



def norms_calculated(vector1, vector2):
    vector1_arr = np.array(vector1)
    dists = []
    start_time = time.time()
    for i in range(len(vector2)):
        vector2_arr = vector2[i][0]
        norm_2=np.linalg.norm(vector2_arr)
        norm_1=np.linalg.norm(vector1_arr)
        dist=np.dot(vector1_arr,vector2_arr)/(norm_2*norm_1)
        dists.append(dist)
    end_time = time.time()
    t=end_time - start_time
    print("Norms_calculated at run time: " + str(t))
    return (dists,t)

def norms_stored(vector1, vector2):
    vector1_arr = np.array(vector1)
    dists = []
    norm_1=np.linalg.norm(vector1_arr)
    start_time = time.time() 
    for i in range(len(vector2)):
        vector2_arr = vector2[i][0]
        norm_2=vector2[i][1]
        dist=np.dot(vector1_arr,vector2_arr)/(norm_2*norm_1)
        dists.append(dist)
    end_time = time.time()
    t=end_time - start_time
    print("Norms stored: " + str(t))
    return (dists,t)


query=[i for i in range(0, 1000)]

dist_2,t2=norms_calculated(query,no_norm_vecs)
dist_1,t1=norms_stored(query,norm_and_vecs)

percent_change=(t1-t2)/t2
print("Percent change (norms stored): " + str(percent_change))


if dist_1==dist_2:
    print("\noperations are equal")
else:
    print("\noperations are NOT equal")
