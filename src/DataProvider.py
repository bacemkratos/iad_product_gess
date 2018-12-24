import pickle
from pathlib import Path

import  src.Models as Models


directory ='data/'
filename = 'dataset.bin'



def saveData( data ):
    binary_file = open(directory+filename,mode='xb',)
    saveddata = pickle.dump(data, binary_file)
    binary_file.close()


def readData():
    with open(directory+filename, "rb") as f:
        obj = pickle.load(f)
        return obj



def initData():


    my_file = Path(directory+filename)

    if not(my_file.is_file()):
        print("inistializing dataset")
        products = []
        products
        smartphone = Models.Product("Samsung s9","SMARTPHONE","Samsung",{"ecran":"5.8", "os":" Android 8.0 ", "cpu":"Exynos 9810 Octo-Core ", "memory":"32",  "ram":"4","reseau":"wifi/4g", "batterie":"3000 mAh","cam":"2"})
        products.append(smartphone)
        smartphone = Models.Product("iPhone 8","SMARTPHONE","Apple",{"ecran":"4.7", "os":"iOS 11", "cpu":" Apple A11 Bionic, Hexa-core 2.06 ", "memory":"32",  "ram":"2","reseau":"wifi/4g", "batterie":"n/a","cam":"2"})
        products.append(smartphone)
        smartphone = Models.Product("VERSUS V730","TABLETTE","Versus",{"ecran":"7", "os":" Android 6.0 ", "cpu":" Quad-Core 1,3 GHz ", "ram":"1", "memory":"2", "reseau":"wifi/3g", "batterie":"2500 mAh","cam":"2"})
        products.append(smartphone)
        smartphone = Models.Product("iPad Pro 9 ","TABLETTE","Apple",{"ecran":"9", "os":"  iOS 9 ", "cpu":"Apple A9X (2.16 GHz, Dual-Core) ",  "memory":"64", "ram":"2","reseau":"wifi/4g", "batterie":"n/a","cam":"2"})
        products.append(smartphone)
        smartphone = Models.Product("Portable LENOVO IP 120S-11IAP ","PC","Lenovo",{"ecran":"11.6", "os":"windows 10", "cpu":"Intel Celeron Dual Core N3350 ", "memory":"500", "ram":"4","reseau":"wifi", "batterie":"n/a","cam":"1"})
        products.append(smartphone)
        saveData(products)
        print("data saved")



