"""

call_the_roll

python 1st exp.

@author:MHWang 09118139

"""

import csv  # read files
import random      # get a missing student
import string # use string to get random letters
import time # calculate the executing time of codes

def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

studentList = []  # save students from the file
tempList = []
wholeList = []  # save all data
wholeDict = {}
wholeSet = set()
wholeTuple = ()
resultList = [] # save the result
timeList = []

with open('d://utf8_python.csv', encoding='utf-8', mode = 'r') as f:
    students = csv.reader(f)
    for people in students:
        count = 0
        if people:
            studentList.append(people)
            tempList.append(tuple(people))
            wholeList.append(tuple(people))


wholeList.append(('09005424','孔祥龙'))


print("successfully get students' information!")

dataType = [1,2,3,4]

# 1-->integer
# 2-->floating-point number
# 3-->string
# 4-->tuple

for i in range(1000000):        # make 1 million data mixture
    data = random.choice(dataType)
    if data == 1:
        newData = random.randint(1,101)   # get randomized int data from 1 to 100
        wholeList.append(newData)


    elif data == 2:
        newData = random.uniform(0.0,10.0)     # get randomized float data from 0.0 to 10.0
        wholeList.append(newData)

    elif data == 3:
        newData = random.choice(string.ascii_letters)     # get randomized str data from alphabet
        wholeList.append(newData)

    else:
        newData = (random.randrange(1,11),random.randrange(1,11))      # get randomized tuple data
        wholeList.append(newData)



while(True):
    missingStudent = random.choice(studentList)
    if (missingStudent != ['09118139', '王明灏']):break
wholeList.remove(tuple(missingStudent))

# use 4 ways to save the data


wholeSet = set(wholeList)
wholeDict = dict(zip(range(len(wholeList)),wholeList))

# random shuffle
random.shuffle(wholeList)
wholeTuple = tuple(wholeList)

# to calculate the waste of time


# using list:
start_time = time.time()
countList = 0
for people in tempList :
    countList += 1
    if people not in wholeList:break
end_time = time.time()
ptime = end_time - start_time
timeList.append(ptime)
resultList.append(('被百万大军van O->的朋友是：',people,'搜索次数是：',countList,'所用时间是：',timeList[0],'数据类型是：',type(wholeList)))

# using set:

start_time=time.time()
countSet = 0
for people in tempList:
    countSet += 1
    if people not in wholeSet:break
end_time = time.time()
ptime = end_time - start_time
timeList.append(ptime)
resultList.append(('被百万大军van O->的朋友是：',people,'搜索次数是：',countSet,'所用时间是：',timeList[1],'数据类型是：',type(wholeSet)))

# using tuple:

start_time=time.time()
countTuple = 0
for people in tempList:
    countTuple += 1
    if people not in wholeTuple:break
end_time = time.time()
ptime = end_time - start_time
timeList.append(ptime)
resultList.append(('被百万大军van O->的朋友是：',people,'搜索次数是：',countTuple,'所用时间是：',timeList[2],'数据类型是：',type(wholeTuple)))

# using dict:

start_time=time.time()
countDict = 0
for people in tempList:
    countDict += 1
    if people not in wholeDict.values():break
end_time = time.time()
ptime = end_time - start_time
timeList.append(ptime)
resultList.append(('被百万大军van O->的朋友是：',people,'搜索次数是：',countDict,'所用时间是：',timeList[3],'数据类型是：',type(wholeDict)))

resultList.sort(key=lambda timeList:timeList,reverse=False)

for i in range(0,4):
    print(resultList[i])