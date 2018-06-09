def LevenshteinDistance(word1, word2, CaseSensitive=False):

    if CaseSensitive:
        word1 = word1.lower()
        word2 = word2.lower()

    if word1 == '' or word2 == '':
        return max(len(word1), len(word2))

    if word1[-1] == word2[-1]:
        cost = 0
    else:
        cost = 1

    return min(LevenshteinDistance(word1[:-1], word2) +1,
               LevenshteinDistance(word1, word2[:-1]) + 1,
               LevenshteinDistance(word1[:-1], word2[:-1]) + cost)



if __name__ == '__main__':
    tab = LevenshteinDistance("Aromatico", "aromatico")
    print(tab)
