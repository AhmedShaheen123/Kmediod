import pandas as pd
from numpy import linalg as la
from scipy.spatial import distance
import math

class Kmediod:
    def __init__(self, iter):
        self.iter = iter

    def fit(self, data, FixedRow):
        mediod = {}
        if self.iter > len(data):
            self.iter = len(data)
        for i in range(self.iter):
            cost = []
            for row in range(len(df)):
                x1 = distance.euclidean(df.values[row], df.values[FixedRow])
                x2 = distance.euclidean(df.values[row], df.values[i])
                cost.append(min(x1, x2))
            mediod[i] = sum(cost)
        centroid = min(mediod, key=mediod.get)
        return centroid, FixedRow


# data
df = pd.read_csv('Mall_Customers.csv')

df.info()
df.drop(['CustomerID', 'Gender'], axis=1, inplace=True)
model = Kmediod(300)


