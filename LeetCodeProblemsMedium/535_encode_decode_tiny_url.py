"""

"""
import random
class Codec:

    def __init__(self):
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.alphabet_size = len(self.chars)
        self.code_length = 6
        self.long_url_by_code = {}

    def getRandomFixedLengthCode(self):
        code = ""
        for i in range(self.code_length):
            code += self.chars[random.randint(0,self.alphabet_size-1)]
        return code

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        code = self.getRandomFixedLengthCode()
        while code in self.long_url_by_code:
            code = self.getRandomFixedLengthCode()
        self.long_url_by_code[code] = longUrl
        return code


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.long_url_by_code[shortUrl]

if __name__ == "__main__":
    codec = Codec()
    url = 