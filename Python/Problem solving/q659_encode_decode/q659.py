class Solution:
    charkey = '+'
    def encode(self, strs):
        # write your code here
        output = ""
        for s in strs:
            output += str(len(s)) + self.charkey + s
        return output

    def decode(self, str):
        # write your code here
        output = []
        index = 0
        while index < len(str):
            length = 0
            while str[index] != self.charkey:
                length = length * 10 + int(str[index])
                index += 1
            index += 1
            output.append(str[index:index + length])
            index += length
        return output

if __name__ == "__main__":
    s = Solution()
    encoded = s.encode(["lint","code","love","you"])
    decoded = s.decode(encoded)
    print(encoded)
    print(decoded)
