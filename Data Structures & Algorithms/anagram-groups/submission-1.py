class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams where the key is the sorted anagram and the value is the index of the anagram in the set of groups 
        # traverse through the list of strings, for each value, sort the string, search it in the dict, and if it exists, add the anagram to the index of the result
        anagrams = {}
        for word in strs:
            key_word = "".join(sorted(word))
            if key_word in anagrams:
                anagrams[key_word].append(word)
            else:
                anagrams[key_word] = [word]
        return list(anagrams.values())

