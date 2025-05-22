def isomorphic_string(s, t): # Two Hash Maps
    '''
    TC: O(n)
    AS: O(1)
    '''
    if len(s) != len(t):
        return False

    sMap = {}
    tMap = {}

    for c1, c2 in zip(s, t):
        if c1 in sMap:
            if sMap[c1] != c2:
                return False
        else:
            sMap[c1] = c2

        if c2 in tMap:
            if tMap[c2] != c1:
                return False
        else:
            tMap[c2] = c1

    return True


def isomorphic_string(s, t): # One Hash Map, One Set
    '''
    TC: O(n)
    AS: O(1)
    '''
    if len(s) != len(t):
        return False

    sMap = {}
    tset = set()

    for c1, c2 in zip(s, t):
        if c1 in sMap:
            if sMap[c1] != c2:
                return False
        else:
            if c2 in tset: ## c2 is mapped to some other character so we can't remap to
                return False
            sMap[c1] = c2
            tset.add(c2)

    return True