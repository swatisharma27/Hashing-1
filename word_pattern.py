class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        '''
        TC : O(n)
        AS: O(1)
        '''

        sMap = {}
        tset = set()
        s = s.split(" ")

        if len(pattern) != len(s):
            return False

        for c1, c2 in zip(pattern, s):
            if c1 not in sMap:
                if c2 in tset:
                    return False
                sMap[c1] = c2
                tset.add(c2)
            else:
                if sMap[c1] != c2:
                    return False
        return True
    
