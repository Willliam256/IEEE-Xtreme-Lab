
"""
The string anagram is a string with the same characters and the order can only be different. 
To understand how anagram works, you can see the example of anagram that is “TRIANGLE “ and 
“INTEGRAL”, “SILENT” and “LISTEN” are the anagrams of each other.

"""


def isAnagram(wordList) -> bool:
    #capture the two strings to compare

    anagramWords = []
    tempWord = ""

    for i in range(0, len(wordList)):
        currWord = wordList[i]

        for j in range(i+1, len(wordList)):
            tempWord = wordList[j]
            
            if (sorted(currWord) == sorted(tempWord)):
                if currWord not in anagramWords:
                    anagramWords.append(currWord)
                    anagramWords.append(tempWord)
        # anagramWords.append("==")
        
    count = len(anagramWords)
    print(count)
    print(anagramWords)

words = int(input())
lst = []
for x in range(words):
    lst.append(input())



if  __name__ == "__main__":

    # lst = ["cats", "caller", "dogs", "cellar", "parrots", "recall"]
    # lst = ["diapers","disease", "burned", "praised", "viewer", "despair", "burden", "review","viewre"]

    isAnagram(lst)









