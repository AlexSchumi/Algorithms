# This version is my implementation of word ladder;
# revise it to test the running time case !!!!!!!!!!!!!
def wordladder(beginword, endword, wordlist):
    """
    :type beginword: string
    :type endword: string
    :type wordlist: a list containing transformation words
    """
    alphabet = []
    for letter in range(97,123):
        alphabet.append(chr(letter))

    stack = []
    stack.append(beginword)
    level = 1

    while stack and len(stack) != 0: # we have elements to transform in this situation
        length = len(stack)
        for cur in stack[:length]: # traverse all the nodes in stack
            if cur != endword:
                for i in range(len(cur)): # cur is a string
                    for j in range(len(alphabet)):
                        str1 = str(cur[:i]+alphabet[j]+cur[i+1:])
                        if str1 in wordlist:
                            stack.append(str1) # if we have this word in wordlist,
                            #we append it to stack
                            wordlist.remove(str1)# remove from original stack to avoid duplication;
            else:
                return level # if we have found the word in the wordlist

        stack = stack[length:]
        if len(stack) != 0:
            level += 1
        print(level)

    return 0

# This is new version for wordladder2 to pass run time test
def wordladder2(beginword, endword, wordlist):

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
#beginWord = "hit"
#endWord = "cog"
#wordList = ["hot","dot","dog","lot","log"]
print(wordladder(beginWord, endWord, wordList))
