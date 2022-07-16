class Solution:
    def addBinary2(self, a: str, b: str) -> str:
        # if a or b is empty, return the other one
        if a == "" or b == "":
            return a if a else b
        # if a and b are not empty, add them together
        else:
            # convert the strings to integers
            a = int(a, 2)  # type: ignore
            b = int(b, 2)  # type: ignore
            # add them together
            c = a + b
            # convert the result to binary
            c = bin(c)[2:]  # type: ignore
            # return the result
            return c

    def addBinary(self, a: str, b: str) -> str:
        """
        look at the least important digit > add digits > reverse the result > join it
        """
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while carry or i >= 0 or j >= 0:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        result.reverse()
        return "".join(result)
