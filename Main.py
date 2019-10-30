import partition
import DBParser
import createfile
import generalize


data = DBParser.makeListOfDictionaries()
clusters = partition.algorithm(data,4000)
print(data[1])

for i in range(1,4000):
    genOfSex = generalize.generalizeSex(clusters[i])
    genOfMaritalStat = generalize.generalizeMaritalStat(clusters[i])
    genOfCountry = generalize.generalizeCountry(clusters[i])
    genOfWorkclass = generalize.generalizeWorkclass(clusters[i])
    createfile.createAnonDataFile(clusters[i],genOfSex,genOfWorkclass,genOfCountry,genOfMaritalStat)
