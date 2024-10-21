class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        #bu çözümde yine recursive kullanacağız


        def backtrack(start, seen):
            if start == len(s): #eğer listenin sonuna gelinmişse dur
                return 0
            
            max_split = 0
            #ilk başta end değeri 1 ile başlıyor her seferinde 1 artıyor
            #böylece tüm kombinasyonları deniyoruz 
            for end in range(start + 1, len(s) + 1): 
                substring = s[start:end]
                if substring not in seen:# seen set kümesinde unique'lik kontrolü yapıyoruz
                    seen.add(substring)
                    max_split = max(max_split, 1 + backtrack(end, seen))
                    seen.remove(substring)
            return max_split
        
        return backtrack(0, set())