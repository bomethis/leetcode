class Solution:
    def uniqueMorseRepresentations(words):
        dicts = {
            "a": ".-",
            "b": "-...",
            'c': "-.-.",
            'd': "-..",
            'e': ".",
            'f': "..-.",
            'g': "--.",
            'h': "....",
            'i': "..",
            'j': ".---",
            'k': "-.-",
            'l': ".-..",
            'm': "--",
            'n': "-.",
            'o': "---",
            'p': ".--.",
            'q': "--.-",
            'r': ".-.",
            's': "...",
            't': "-",
            'u': "..-",
            'v': "...-",
            'w': ".--",
            'x': "-..-",
            'y': "-.--",
            'z': "--.."}
        i = 0
        lwords =[]
        for word in words:
            lword = list(word)  # convert imutible str into a list in order to replace letters in each index
            for i in range(len(word)):
                lword[i] = dicts[word[i]]  # replace each letter with corresponding morse code
            jword = ''.join(lword)  # convert the morse code back into a str
            lwords.append(jword)
        return len(set(lwords))  # return the count of unique transformations


words = ["gin", "zen", "gig", "msg"]

print(Solution.uniqueMorseRepresentations(words))



# Success
# Details
# Runtime: 40 ms, faster than 71.72% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 13.2 MB, less than 43.43% of Python3 online submissions for Unique Morse Code Words.
