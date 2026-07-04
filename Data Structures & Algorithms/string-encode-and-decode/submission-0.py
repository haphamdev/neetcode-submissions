class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            for c in s:
                if c == ' ': 
                    result += '? '
                elif c == '?':
                    result += f'??'
                else:
                    result += c
            result += '?&'
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        current = ''
        i = 0
        while i < len(s):
            c = s[i]
            if c == '?':
                next = s[i+1]
                if next == '?':
                    current += '?'
                elif next == ' ':
                    current += ' '
                elif next == '&':
                    result.append(current)
                    current = ''
                i += 2
            else:
                current += c
                i += 1
        return result

