import numpy as np

def minimo(tab, X, Y, cost):
    if X > 0 and Y > 0:
        return min((tab[X-1, Y] + 1,
                    tab[X, Y-1] + 1,
                    tab[X-1, Y-1] + cost
                    ))
    elif X > 0:
        return tab[X-1, Y] + 1
    elif Y > 0:
        return tab[X, Y-1] + 1
    else:
        return 0

def LevenshteinDistance2(word1, word2, CaseSensitive = True):

    if CaseSensitive:
        word1 = word1.lower()
        word2 = word2.lower()

    tab = np.zeros((len(word1), len(word2)))

    for i, e in enumerate(word1):
        tab[i, 0] = i
    for j, e in enumerate(word2):
        tab[0, j] = j

    for X, i in enumerate(word1):
        for Y, j in enumerate(word2):
            if i == j:
                cost = 0
            else:
                cost = 1

            tab[X, Y] = minimo(tab, X, Y, cost)

    print(tab)
    return tab[-1, -1]

def LevenshteinDistanceRecursive(word1, word2, CaseSensitive=False):
    global tab
    if CaseSensitive:
        word1 = word1.lower()
        word2 = word2.lower()

    if word1 == '' or word2 == '':
        return max(len(word1), len(word2))

    if word1[-1] == word2[-1]:
        cost = 0
    else:
        cost = 1

    return min(LevenshteinDistanceRecursive(word1[:-1], word2) + 1,
               LevenshteinDistanceRecursive(word1, word2[:-1]) + 1,
               LevenshteinDistanceRecursive(word1[:-1], word2[:-1]) + cost)


if __name__ == '__main__':
    word1, word2 = "Aromatico", "aro"
    dif = LevenshteinDistanceRecursive(word1, word2, True)
    print(dif)
