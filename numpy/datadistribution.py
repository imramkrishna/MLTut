from numpy import random
import numpy as np
#this random function generate an array of size specified in size parameters where each element can only be between 3,5,7,9 and is probablity of occurance is p array, here it is just probablity, it doesnot gurantee fix occurance
x=random.choice([3,5,7,9],p=[0.1,0.3,0.5,0.1],size=(10))
print(x)
y=random.choice([1,2,3,4,5,6,7,8,9,10],p=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1],size=(10))
print(y)
z=np.array([1,2,3,4,5,6,7,8,9,10])
random.shuffle(z)
print("Suffled Array : ",z)#this function shuffles the array randomly --> works on the original array
print("Random permutation of array : ",random.permutation(z))#this function returns a new array which is a shuffled version of the original array -->returns a new array

