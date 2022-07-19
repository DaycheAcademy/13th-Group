varInput = input("please enter text").lower()

txtChecker = (' ', '\\', '|', ',', '.', ';', ":", '/', '*', '-', '+', '!', '@', '#', '$', '%', '^', '&', '(', ')', '=', '_', '[', ']', '?', '<', '>', '{', '}')

tobeList = ('being', 'are', 'am', 'is', 'was', 'were', 'been')

countText = 0
listChar = list()
i = 0
while i < len(varInput):
    t = ''
    c = i
    while c < len(varInput):
        if varInput[c] in txtChecker:
            i += 1
            break
        t += varInput[c]
        c += 1
        i = c
    listChar.append(t)

listChar = [i for i in listChar if len(i) > 1 ]
setChar = set(listChar)
interSet = setChar.intersection(set(tobeList))

dictCountTobe = dict.fromkeys(tobeList,0)

for val in tobeList:
    if val in listChar:
        dictCountTobe[val] = listChar.count(val)


print(f'All char: {varInput.__len__()}\nAll word: {len(listChar)}\nAll unique words:{len(setChar)}\nAll tobe: {len(interSet)}\n')
print("tobe:")
for k, v in dictCountTobe.items():
    print('{}: {}'.format(k,v))
