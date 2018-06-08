import numpy as np

def LevenshteinDistance(word1, word2):
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
                cost = 2

            tab[X, Y] = cost + min(( tab[X-1, Y],
                      tab[X, Y-1],
                      tab[X-1, Y-1]
                      ))

    print(tab)
    return tab[-1, -1]



if __name__ == '__main__':
    tab = LevenshteinDistance("Arroz", "aroz")
    print(tab)
