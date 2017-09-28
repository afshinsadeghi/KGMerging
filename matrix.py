import numpy as np
import nltk as nt

# read the files line by line put into arrays
array1 = []
array2 = []
with open('dataset/sampleDB1.ttl', 'r') as file1:
    for lineInFile in file1:
         array1.append(lineInFile.rstrip('\n').strip(" ").split(" "))

with open('dataset/sampleDB2.ttl', 'r') as file2:
    for lineInFile in file2:
        array2.append(lineInFile.rstrip('\n'))

nArray1 = np.array(array1)
nArray2 = np.array(array2)
print( nArray1[0:2:1])
print( nArray2[0:2:1])

#predicates1= nArray1[:,1]
#predicates2= nArray2[:,1]