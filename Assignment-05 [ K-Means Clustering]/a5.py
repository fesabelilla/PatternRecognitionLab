# -*- coding: utf-8 -*-
"""patt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YTl-g3Kzyt0c6c3MvoymaNrIteglLPPL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive

drive.mount('/content/gdrive')

root_path = '/content/gdrive/My Drive/PatternAssignment5/'

df = pd.read_csv('/content/gdrive/My Drive/PatternAssignment5/data_k_mean.txt',sep=" ",header=None)

K = input("Enter number of clusters: ")

K = int(K)
# Select random observation as centroids
Centroids = (df.sample(n=K))
plt.scatter(df[0],df[1],c='black')
plt.scatter(Centroids[0],Centroids[1],c='red')
plt.show()

print(df)

df = df.to_numpy();

centroids = df[np.random.choice(df.shape[0],K), :]
minm = np.zeros(K)

centroids

print(df)

value = [ [ i[0] , i[1] , 5000 ] for i in df]

print(value)

for z in range(300):

    cnt = 0
    for i in range(len(value)):

        for j in range(K):
            minm[j] = np.sqrt( ((value[i][0] - centroids[j][0])**2) + ((value[i][1] - centroids[j][1])**2) )
        
        ## Return the minimum of an array 
        temp1 = np.where(minm == np.amin(minm))
        #print("Temp1 : ", temp1,"\n")
        temp1 = np.array(temp1)

        if(value[i][2] != temp1.item(0)):
            value[i][2] = temp1.item(0)
            #print("Points : ",value,"\n")
            cnt = cnt + 1

    if(cnt == 0):
        break
    for i in range(K):
        temp = [[x[0],x[1]] for x in points if x[2]==i]
        temp = np.array(temp)
        centroids[i] = [ sum(x)/len(x) for x in zip(*temp)]

print(value)

centroids = pd.DataFrame(centroids)

centroids

plt.figure(figsize = (20, 30))

color = ['c','m','k','b','y','g','r']
marker = ['o','o','o','o','o','o','o','o']

a,b = plt.subplots()

for i in range(K):
    temp=[[j[0],j[1]] for j in value if j[2]==i]
    temp=np.array(temp)
    lvl ="Cluster " + str(i+1)
    b.scatter(temp[:,0], temp[:,1], marker = marker[i], color = color[i], label = lvl)

legend = b.legend()

plt.show()

