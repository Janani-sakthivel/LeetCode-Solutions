class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:  # if list is empty
            return ""

        # Take the first word as base
        prefix = strs[0]

        # Compare with all other words
        for word in strs[1:]:
            # Reduce prefix until it matches the start of word
            while word.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix