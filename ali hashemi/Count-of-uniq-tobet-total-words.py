
import re


inp = input("input your sentence: ")
inp = inp.lower()
toBeVerb = {"am", "is", "are", "was", "were"}

inp = re.split(',|:|`|\\s', inp)
inp2 = []
for item in inp:
    if item:
        inp2.append(item)

inp = inp2

inpSet = set(inp)

print('Number of Total Words: {}'.format(len(inp)))

print('Number of Unique word: {}'.format(len(inpSet)))

print('Repeated words: ')

inpDict = dict()
for word in inp:
    if word in inpDict:
        inpDict[word] += 1
    else:
        inpDict[word] = 1
for key in inpDict:
    if inpDict[key] != 1:
        print(key, inpDict[key])



print('Number of to be verbs:')
for tobe in toBeVerb:
    count = inp.count(tobe)
    if count:
        print('{} repeat: {}'.format(tobe, count))




