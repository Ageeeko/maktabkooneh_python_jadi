number = int(input())
english = dict()
french = dict()
german = dict()
for i in range(number):
    word = input().split(" ")
    english[word[1]] = word[0]
    french[word[2]] = word[0]
    german[word[3]] = word[0]

sentence = input().split(" ")
for index,i in enumerate(sentence):
    if i in english:
        sentence[index] = english[i]
    elif i in french:
        sentence[index] = french[i]
    elif i in german:
        sentence[index] = german[i]

print(' '.join(sentence))
