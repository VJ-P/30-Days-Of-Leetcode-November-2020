class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        ext = q
        refl = p
        
        while ext%2 == 0 and refl%2 == 0:
            ext = ext/2
            refl = refl/2
        
        if ext%2 == 0 and refl%2 != 0:
            return 0
        elif ext%2 != 0 and refl%2 == 0:
            return 2
        elif ext%2 != 0 and refl%2 != 0:
            return 1
        else:
            return -1