class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            for ch in s:
                encoded.append(ord(ch))
            encoded.append(-1)

        return ",".join(map(str, encoded))

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        encoded = list(map(int, s.split(",")))

        result = []
        word = ""

        for x in encoded:
            if x == -1:
                result.append(word)
                word = ""
            else:
                word += chr(x)

        return result