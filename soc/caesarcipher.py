def caesar(enc, m, k):
    out = ""
    k = int(k)
    if (enc == True):
        for char in m:
            if ((char >= "A") and (char <= "Z")):
                if ((ord(char) + (k%26)) > 90):
                    char = (k%26) - 90 + ord(char) + 65 - 1
                    char = chr(int(char))
                else:
                    char = ord(char) + (k%26)
                    char = chr(int(char))
            elif ((char >= "a") and (char <= "z")):
                if ((ord(char) + (k%26)) > 122):
                    char = (k%26) - 122 + ord(char) + 97 - 1
                    char = chr(int(char))
                else:
                    char = ord(char) + (k%26)
                    char = chr(int(char))
            out += char

    if (enc != True):
        for char in m:
            if ((char >= "A") and (char <= "Z")):
                if ((ord(char) - (k%26)) < 65):
                    char = 90 - (k%26) + ord(char) - 65 + 1
                    char = chr(int(char))
                else:
                    char = ord(char) -  (k%26)
                    char = chr(int(char))
            elif ((char >= "a") and (char <= "z")):
                if ((ord(char) - (k%26)) < 97):
                    char = 122 - (k%26) + ord(char) - 97 + 1
                    char = chr(int(char))
                else:
                    char = ord(char) -  (k%26)
                    char = chr(int(char))
            out += char
    return out



            