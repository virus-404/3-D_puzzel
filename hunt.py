#!/usr/bin/env python3
import os

def __main__():

    global graph

    letters = [i for i in 'ntsariolawepcodiva']
    with open("result.txt","w") as target:
        pass

    graph = []
    dictionary  = open("words.txt","r")

    print ('>>> 3-D Hunt <<<')

    for x in range(3):
        graph.append([])
        for y in range(2):
            graph[x].append([])
            for z in range(3):
                graph[x][y].append(letters.pop(0))

    words = [line.strip() for line in dictionary.readlines()]
    dictionary.close()
    
    for floor in range(3):
        for row in range(2):
            for letter in range(3):
                search(floor, row, letter, words)

def search(i,j,k, words, prefix = ''):
    prefix += graph[i][j][k]

    candidates = []

    for word in words:
        if prefix == word:
            add_word(prefix)
        elif word.startswith(prefix):
            candidates.append(word)
        else:
            pass

    if len(candidates) > 0:
        for inc in [-1,1]:
            if (i + inc in range(3)):
                search(i+inc,j,k,candidates,prefix)
        for inc in [-1,1]:
            if (j + inc in range(2)):
                search(i,j+inc,k,candidates,prefix)
        for inc in [-1,1]:
            if (k + inc in range(3)):
                search(i,j,k+inc,candidates,prefix)


def add_word (word):
    with open('./result.txt', 'a') as file:
        file.write(word + '\n')

if __name__ == '__main__':
    __main__()
