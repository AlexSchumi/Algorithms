class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        index = 0

        while index < len(words):
            count = len(words[index])
            last = index + 1
            while last < len(words):
                if count + len(words[last]) + 1 > maxWidth: break
                count += len(words[last]) + 1
                last += 1
            word = words[index]
            diff = last - index - 1

            if last == len(words) or diff == 0: # deal with last word
                for i in range(index+1, last):
                    word += " "
                    word += words[i]
                for i in range(len(word), maxWidth):
                    word += " "
            else:
                spaces = (maxWidth - count) // diff
                r = (maxWidth - count) % diff
                for i in range(index+1, last):
                    for k in range(spaces, 0, -1):
                        word += " "
                    if r > 0:
                        word += " "
                        r -= 1
                    word += " "
                    word += words[i]
            res.append(word)
            index = last
        return res

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
if __name__ == '__main__':
    print(len(Solution().fullJustify(words, maxWidth)[0]))
