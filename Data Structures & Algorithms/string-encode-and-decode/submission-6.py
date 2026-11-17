class Solution:

    def encode(self, strs: List[str]) -> str:
        i=0
        s=""
        while(i<len(strs)):
            s+=str(len(strs[i]))+"#"+strs[i]
            i=i+1
        return s


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1

            ans.append(s[i:i+length])
            i += length

        return ans

