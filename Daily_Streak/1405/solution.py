import random
class Solution(object):
    def longestDiverseString(self, a, b, c):
        #happiness oluşturacak seviyede eleman kalana kadar bozan elemanları sil
        #en fazla tekrar eden harfin sayısı, diğer iki sayının toplamının
        #iki katına kadar olabilir
        def sayiKontrol(a, b, c):
            mins = (b + c + 1) * 2
            if(a > mins):
                # a'dan silmemiz lazım
                a = mins
            return a
            
        def happinessControl(liste):
            chr_counter = 1
            before_chr = liste[0]
            copy_list = liste[:]
            del copy_list[0]

            for chr in copy_list:
                if (chr == before_chr):
                    chr_counter += 1
                else:
                    before_chr = chr
                    chr_counter = 1
                
                if(chr_counter >= 3):
                    return False
            
            return True


        if(a >= b and a >= c):
            #a en büyük
            a = sayiKontrol(a,b,c)

        elif(b >= a and b >= c):
            #b en büyük
            b = sayiKontrol(b,a,c)
        else:
            #c en büyük
            c = sayiKontrol(c,b,a)

        #hepsini bir listeye at
        str_list = []
        my_dict = {"a": a, "b": b, "c": c}
        for chr, num in my_dict.items():
            for i in range(num):
                str_list.append(chr)
        
        
        


        #liste içinde değişiklik yap ve kontrol et uyuyor mu diye
        while(not happinessControl(str_list)):
            random.shuffle(str_list)
        
        #sıra doğru stringe çevir ve döndür
        rtrn_string = "".join(str_list)
        return rtrn_string


if __name__ == "__main__":
    solution = Solution()
    result = solution.longestDiverseString(4,42,7)
    print("Oluşturulan dizi:", result)



            
    




        