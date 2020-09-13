from pandas import DataFrame
from sklearn.cluster import KMeans
import random
import numpy as np
import time
import sys

number_of_data_points=int(sys.argv[2])
number_of_clusters=int(sys.argv[1])
def get_random_cluster_points(number_points, number_dim):
    mu = np.random.randn()
    sigma = np.random.randn()
    p = sigma * np.random.randn(number_points, number_dim) + mu
    return p

t1 = time.time()
p = get_random_cluster_points(number_of_data_points, 2)
#t1 = time.time()
kmeans = KMeans(n_clusters=number_of_clusters,n_jobs=1,tol=-0).fit(p)
#t2 = time.time()

#time_avg = t2-t1
#print('time_total:' + str(time_avg))
centroids = kmeans.cluster_centers_
t2 = time.time()
time_avg = t2-t1
print('time_total:' + str(time_avg))
