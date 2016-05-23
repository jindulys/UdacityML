"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    strList = s.split()
    wordDict = {}
    for word in strList:
        if wordDict.has_key(word):
            wordDict[word] = wordDict[word] + 1
        else:
            wordDict[word] = 1
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    countDict = {}
    for key,value in wordDict.iteritems():
        if countDict.has_key(value):
            countDict[value].append(key)
        else:
            countDict[value] = [key]
   
    
    for key, value in countDict.iteritems():
        value.sort()
        countDict[key] = value
    
    
    sortedList = sorted(countDict, reverse=True )
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    remainning = n
    i = 0
    top_n = []
    while remainning > 0 and i < sortedList.count:
        currentWords = countDict[sortedList[i]]
        if remainning < len(currentWords):
            for j in range(remainning):
                top_n.append((currentWords[j], sortedList[i]))
            remainning = 0
        else:
            for j in range(len(currentWords)):
                top_n.append((currentWords[j], sortedList[i]))
            remainning -= len(currentWords)
        i = i+1
        
    return top_n
    
def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)

if __name__ == '__main__':
    test_run()
