def LevenshteinDistance(word1, word2):
    l_word1, l_word2 = len(word1), len(word2)

    if word1 == '' or word2 == '':
        return max(l_word1, l_word2)

    if word1[-1] == word2[-1]:
        cost = 0
    else:
        cost = 1

    return min(LevenshteinDistance(word1[:-1], word2) +1,
               LevenshteinDistance(word1, word2[:-1]) + 1,
               LevenshteinDistance(word1[:-1], word2[:-1]) + cost)



if __name__ == '__main__':
    tab = LevenshteinDistance("Aromatico", "kek")
    print(tab)
