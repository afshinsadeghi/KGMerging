import numpy as np
import nltk as nt

# read the files line by line put into arrays
array1 = np.empty((70000, 3), dtype=object)
array2 = np.empty((70000, 3), dtype=object)
counter = 0
lineInFile = ""
ending = ">"
try:
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


    print(array1[0])
    print(array1[0, 1])
    print(array2[0, 1])

    predicates1 = array1[:, [1]]
    predicates2 = array2[:, [1]]


except ValueError:
    print(lineInFile)
    print(lineInFile.rstrip('\n').strip(" .").split("> "))
    print counter