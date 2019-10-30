import partition
import DBParser
import createfile
import random
import time

data = DBParser.makeListOfDictionaries()

curTime = time.time()
print(curTime, "\n")

catDict = {'workclass' : [], 'education' : [], 'maritalStatus' : [], 'occupation' : [], 'relationship' : [], 'sex' : [], 'nativeCountry' : [], 'salaryPerYear' : []}

# Convert the categorical data to numerical data
def convertCatToNum(x):
  coordinate=[]
  for colName in x:
    if(colName in catDict):
      if(x[colName] not in catDict[colName]):
        catDict[colName].append(x[colName])
        
      coordinate.append(catDict[colName].index(x[colName]) + 1)
    elif(colName != 'race'):
      coordinate.append(int(x[colName]))
      
  coordinate.append(x['race'])
  return coordinate


# Range of coordinates
def rangeOfCoord(coordinates):
  maxR = coordinates[0][0:14]
  minR = coordinates[0][0:14]
  for coordinate in coordinates:
    for i in range(14):
      if(coordinate[i] > maxR[i]):
        maxR[i] = coordinate[i]
      elif(coordinate[i] < minR[i]):
        minR[i] = coordinate[i]
        
  return maxR, minR


# Place n centroids randomly
def randomCentroid(maxR, minR, n):
  centds = []
  while(len(centds) < n):
    centd = []
    for i in range(14):
      coord = random.randrange(minR[i], maxR[i]+1, round((maxR[i]-minR[i])/n)+1)
      centd.append(coord)
    if(centd not in centds):
      centds.append(centd)
  return centds

# Calculating distance between point and distance
def calDistance(pt, centd):
  dist = 0
  for i in range(14):
    dist = dist + abs(pt[i] - centd[i])
  return dist

# Calculate distance of each point to all the centroids
def clusterPoints(pts, centds,n):
  clusters={}
  
  for pt in pts:
    distPointAndCent = 1000000000
    centroid = 0
    ind = pts.index(pt)
    for i in range(n):
      temp = calDistance(pt, centds[i])

#      if(ind not in dist):
#        dist[ind] = [temp]
#      else:
#        dist[ind].append(temp)
#        
      if(distPointAndCent > temp):
        distPointAndCent = temp
        centroid = i

#    dist[ind].append(centroid)
    if(centroid not in clusters):
      clusters[centroid] = [pt]
    else:
      clusters[centroid].append(pt)

  return clusters


# Calculating average distance and assigning new centroids
def newCentroids(clsts, centds):
  for i in clsts:
    newCentd = [0]*14
    for j in clsts[i]:
      for k in range(14):
        newCentd[k] = newCentd[k]+j[k]
    for k in range(14):
      newCentd[k] = round(newCentd[k]/len(clsts[i]))
    centds[i] = newCentd
  return centds




# n - Number of clusters
def partition(data, n): # n - Number of clusters
  
  # pionts[] - list of all point vectors
  points = []
  
  # centrids[] - list of n centroid vectors
  centroids = []
  
  # distance[] - list of distance vectors from centroids to point of all points
  distance = []
  
  # Convert the categorical data to numerical data
  for x in data:
    points.append(convertCatToNum(x))
  
  # Getting the range of coordinates
  maxRange, minRange = rangeOfCoord(points)
  
  # Place n centroids randomly
  centroids = randomCentroid(maxRange, minRange, n)

  # Calculate distance of each point to all the centroids
  prevCentroids = []
  
  counter=1
  clusters = clusterPoints(points, centroids, n)
  
  while(prevCentroids != centroids):
    print(counter)
    prevCentroids = centroids.copy()
    centroids = newCentroids(clusters, centroids)
    clusters = clusterPoints(points, centroids, n)
    counter = counter + 1
    
    
  for i in clusters:
    print(len(clusters[i]))
    
  elapTime = time.time() - curTime

  print(elapTime)
  
    
  # Place all the points in the cluster which have least distance to the centroid
  
  
partition(data, 1000)