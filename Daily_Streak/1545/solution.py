class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        #soru recursive'im diye bağırıyor
        #istenen fonksiyonları da yazıyoruz
        def reverse(text):
            temp = ""
            liste = list(text)[::-1]
            for chr in liste:
                temp += chr

            return temp

        def invert(text):
            temp = ""
            for chr in text:
                if(chr == "0"):
                    temp += "1"
                else:
                    temp += "0"
            
            return temp

        def reFound(n):
            text = ""
            while True:
                if n == 1:
                    return "0"
                ex_text = reFound(n - 1) 
                text =  ex_text + "1" + reverse(invert(ex_text)) 
                return text
        
        text = reFound(n)
        return text[k - 1]

        