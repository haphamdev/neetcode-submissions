class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            counter = [0] * 26

            for c in s:
                index = ord(c) - 97
                counter[index] += 1
            
            key = ','.join(map(str,counter))
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]

        result = []
        for k in d:
            result.append(d[k])

        return result
