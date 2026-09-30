class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s = s2[:len(s1)]

        left = 0
        right = len(s1) - 1

        while right < len(s2):

            if sorted(s1) == sorted(s):
                return True

            # Remove left character
            s = s[1:]
            left += 1

            # Move right
            right += 1

            # Add new character
            if right < len(s2):
                s += s2[right]

        return False