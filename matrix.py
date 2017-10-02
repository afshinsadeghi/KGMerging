import numpy as np
import nltk as nt

# read the files line by line put into arrays
array1 = np.empty((70000, 3), dtype=object)
array2 = np.empty((70000, 3), dtype=object)
counter = 0
lineInFile = ""
ending = ">"
#try:
with open('dataset/sampleDB1.ttl', 'r') as file1:
    for lineInFile in file1:
        lineInFile = lineInFile.rstrip('\n').strip(" .").split("> ")
        for n in range(0, 3, 1):
            if lineInFile[n][0] == "<":
                lineInFile[n] = lineInFile[n] + ending
            array1[counter, n] = lineInFile[n]
        counter += 1

counter = 0
with open('dataset/sampleDB2.ttl', 'r') as file2:
    for lineInFile in file2:
        lineInFile = lineInFile.rstrip('\n').strip(" .").split("> ")
        for n in range(0, 3, 1):
            if lineInFile[n][0] == "<":
                lineInFile[n] = lineInFile[n] + ending
            array2[counter, n] = lineInFile[n]
        counter += 1
counter = 0

print ("Number of triples in dataset 1 =", array1.shape[0])
print ("Number of triples in dataset 2 =", array2.shape[0])

print("First triple in dataset 1")
print(array1[0])
print("Predicate of first triple in dataset 1")
print(array1[0, 1])
print("Predicate of first triple in dataset 2")
print(array2[0, 1])

predicates1 = array1[:, [1]]
predicates2 = array2[:, [1]]
print("First 10 predicates of triple in dataset 1")
print (predicates1[0:10])
# next merging the two matrixes into one. and remove repeated predicates
# put all predicates in one place to make them unique
unionPredicates= np.union1d(predicates1,predicates2)   # union itself make them unique
#    uniquePredicates = np.unique(unionPredicates)
print ("All predicates without repetition = ", unionPredicates.size) #10 predicates
print (unionPredicates)
unionPredicatesIndex = np.arange(unionPredicates.size)

subjects1 = array1[:, [0]]
subjects2 = array2[:, [0]]
print("First 10 subjects of triple in dataset1")
print (subjects1[0:10])
#Get all subjects without repetition
unionSubjects = np.union1d(subjects1, subjects2)
print ("All subjects without repetition = ", unionSubjects.size) # 13250 subjects
print (unionSubjects[0:10])
unionSubjectsIndex = np.arange(unionSubjects.size)


objects1 = array1[:, [2]]
objects2 = array2[:, [2]]
print("First 10 objects of triple in dataset1")
print (objects1[0:10])
#Get all subjects without repetition
unionObjects = np.union1d(objects1, objects2)
print ("All objects without repetition = ", unionObjects.size) # 54512 objects
print (unionObjects[0:10])
unionObjectsIndex = np.arange(unionObjects.size)
print ("##############")

for i in range(array1.shape[1]):
    for j in range(unionPredicates.size):
        if array1[i, 1] == unionPredicates[unionPredicatesIndex[j]]:
            array1[i, 1] = unionPredicatesIndex[j]

print (array1[0:10, [1]])
#except ValueError:
#    print(lineInFile)
#    print(lineInFile.rstrip('\n').strip(" .").split("> "))
#    print counter

