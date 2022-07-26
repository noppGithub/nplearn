# store the mapping of the characters of s to t
# if a character in s is already mapped, then check if that character is in t

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_mapped = set()

        for cs, ct in zip(s, t):

            if cs in s_to_t:
                if s_to_t[cs] != ct:
                    return False
            elif ct in t_mapped:
                return False
            s_to_t[cs] = ct
            t_mapped.add(ct)

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("egg", "add"))