import random
with open('/Users/afshin/Downloads/KGresearch/datasets/DBpedia/dbpediaperson1.ttl', 'r') as file:
 array1=[]
 array2 =[]
 items = [1 , 2, 3] # if one put in the first array, if 2 put in the second array , if 3 put in both arrays
 for lineInFile in file:
     choice = random.sample(items,1)
     choice = choice[0]
     if choice == 1:
         array1.append(lineInFile)
     if choice == 2:
        array2.append(lineInFile)
     if choice == 3:
        array1.append(lineInFile)
        array2.append(lineInFile)

with open('/Users/afshin/Downloads/KGresearch/datasets/DBpedia/sampleDB1.ttl', 'w') as file2:
    for row in array1:
        file2.write(row)  # python will convert \n to os.linesep
with open('/Users/afshin/Downloads/KGresearch/datasets/DBpedia/sampleDB2.ttl', 'w') as file3:
    for row2 in array2:
        file3.write(row2)  # python will convert \n to os.linesep


file.close()
file2.close()
file3.close()