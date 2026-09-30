class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res     

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0

        while left < len(s):
            right = left

            # Find the separator #
            while s[right] != "#":
                right += 1

            # Get length
            length = int(s[left:right])

            # Move past #
            left = right + 1

            # Extract string
            res.append(s[left:left + length])

            # Move to next encoded string
            left += length

        return res