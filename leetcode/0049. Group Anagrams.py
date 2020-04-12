'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        # list版
        # class_strs = []
        # for i in strs:
        #     temp = sorted(i)
        #     if temp not in class_strs:
        #         class_strs.append(temp)

        # r_strs = []
        # for i in class_strs:
        #     r_strs.append([])

        # for i in strs:
        #     r_strs[class_strs.index(sorted(i))].append(i)
        # return r_strs

        # dict版
        dic = dict()
        for i in strs:
            temp = ''.join(sorted(i))
            print(temp)
            if temp in dic:
                dic[temp].append(i)
            else:
                dic[temp] = [i]
        return dic.values()




print(Solution.groupAnagrams(0, ["eat","tea","tan","ate","nat","bat"]))
print(Solution.groupAnagrams(0, ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]))



import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)  # 創建預設字典 
        for i in strs:
            dic[''.join(sorted(i))].append(i)
        return dic.values()

