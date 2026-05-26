class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        t_pointers = 0
        
        for i in s:
            if t_pointers < len(t) and i == t[t_pointers]:
                t_pointers += 1
        
        return len(t[t_pointers:])
