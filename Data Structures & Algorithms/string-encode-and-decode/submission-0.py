class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_list = [f"{len(l)}#{l}" for l in strs]

        encode_string = "".join(encoded_list)
        # print(encode_string)
        return encode_string


    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        # if len(s) >= 2:
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            
            str_len = int(s[i:j])
            # print(str_len)
            result.append(s[j+1:j+str_len + 1])
            i = j + 1 + str_len
            # print (i)

        # else:
        #     return [""]
        # print(result)
        return result
