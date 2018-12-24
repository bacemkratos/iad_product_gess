from builtins import print

import  src.DataProvider

from src.DataProvider import initData ,readData

import src.KNNCore as knn
import src.Models as models

# we are trying to look what is this roduct ?
smartphone = models.Product("Samsung s9","?","Samsung",{"ecran":"5.8", "os":" Android 8.0 ", "cpu":"Exynos 9810 Octo-Core ", "memory":"32",  "ram":"4","reseau":"wifi/4g", "batterie":"3000 mAh","cam":"2"})

#this is our initial data set
datatrain = readData()

# we will print the result of  wahat type  is this object
print(knn.knnModel(datatrain,smartphone,4))