strs = ["eat","tea","tan","ate","nat","bat"]

def group_anagrams(strs): # Sorting every element and then making it a key approach
    """
    TC : O(n * (klogk + k))
    AS:  O(n * k)
    """
    groups = {}
    for i in strs:
        j = "".join(sorted(i))
        if j in groups:
            if i not in groups[j]:
                groups[j].append(i)
        else:
            groups[j] = [i]
    return list(groups.values())


print(group_anagrams(strs))

'''------------------------------------------------------------'''


strs = ["eat","tea","tan","ate","nat","bat"]
def group_anagrams2(strs): # Using prime multiplication
    """
    TC : O(n * k)
    AS:  O(n)
    """
    primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
    ]

    groups = {}

    for element in strs:
        product = 1
        for ch in element:
            product *= primes[ord(ch)-ord('a')] # Map char to prime

        if product in groups:
            groups[product].append(element)
        else:
            groups[product] = [element]
    
    return list(groups.values()) 

print(group_anagrams2(strs))