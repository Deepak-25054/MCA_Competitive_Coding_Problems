'''Given two strings s and t, determine whether they are isomorphic. Two strings are isomorphic if each character in s can be consistently mapped to a character in t, with no two different characters mapping to the same character.'''

class Solution(object):

    def isIsomorphic(self, s, t):

        # Store character mappings
        mapping = {}

        # Store already mapped characters in t
        used = set()

        # Check each character
        for i in range(len(s)):

            # If character already has a different mapping
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False

            # Create a new mapping
            else:
                # t[i] is already mapped to another character
                if t[i] in used:
                    return False

                mapping[s[i]] = t[i]
                used.add(t[i])

        return True