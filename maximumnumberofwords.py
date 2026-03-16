from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for i in range(len(sentences)):
            s = sentences[i]
            temp = 1
            for j in range(len(s)):
                if s[j] == ' ':
                    temp += 1
            ans = max(ans, temp)
        return ans


# input
sentences = ["alice and bob love leetcode",
             "i think so too",
             "this is great thanks very much"]

# create object
obj = Solution()

# get output
print(obj.mostWordsFound(sentences))