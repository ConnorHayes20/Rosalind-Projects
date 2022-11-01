## Installing Python
#import this

## Variables and some Arithmetic
#a = 812
#b = 994

#findHyp = a**2 + b**2
#print(findHyp)

## Strings and Lists
#wordOneStart = 46
#wordOneEnd = 52

#wordTwoStart = 111
#wordTwoEnd = 116

#string = "M2okSXYmnkVgqcQlqHETs2ftMUY9QhOMTLxuOKg9xUqIZzPorzanaGwJi05ynULut0Z1djy2EMYJ47ze9DDnj1pfKpNZszopRjiMo3lxwF5Rqunjubata7i7YqRszHBolYon9bh7mmStaa0PpJF2P9zn5ZZmmWaaJXzqlKFM3XMi95WP2r0byBWt9Mgkqx."

#print(f'{string[wordOneStart:wordOneEnd + 1]} {string[wordTwoStart:wordTwoEnd + 1]}')

## Conditions and loops
#a = 4949
#b = 9370
#result = 0

#for x in range(a, b + 1):
#    if x % 2 != 0:
#        result += x

#print(result)

## Working with Files
#outputFile = []
#with open('imput.txt','r') as f:
#    outputFile = [line for pos, line in enumerate(f.readlines()) if pos % 2 != 0]


#with open('output.txt','w') as f:
#    f.write(''.join([line for line in outputFile]))

#print(outputFile)

## Dictionaries
txtStr = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
wordCountDict = {}

for word in txtStr.split(' '):
    if word in wordCountDict:
        wordCountDict[word] += 1
    else:
        wordCountDict[word] = 1

for key, value in wordCountDict.items():
    print(key, value)

