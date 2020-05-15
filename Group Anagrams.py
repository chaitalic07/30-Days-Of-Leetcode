class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ag_dict = defaultdict(list)
        
        for word in strs:
            sorted_word = sorted(word)
            ag_dict[tuple(sorted_word)].append(word)
                
        return ag_dict.values()