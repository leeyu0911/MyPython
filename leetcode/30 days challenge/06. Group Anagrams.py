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
    
        class_strs = []
        for i in strs:
            if sorted(list(i)) not in class_strs:
                class_strs.append(sorted(list(i)))

        r_strs = []
        for i in class_strs:
            r_strs.append([])

        for i in strs:
            r_strs[class_strs.index(sorted(list(i)))].append(i)
            
        return r_strs



print(Solution.groupAnagrams(0, ["eat","tea","tan","ate","nat","bat"]))
print(Solution.groupAnagrams(0, ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]))
