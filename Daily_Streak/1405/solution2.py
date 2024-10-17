def longestDiverseString(self, a: int, b: int, c: int) -> str:
    s = [[a, 'a'], [b, 'b'], [c, 'c']]  # Karakter sayıları ve karakterlerin eşleştirildiği bir liste oluştur.
    ans = []  # Sonuç dizisi.

    while True:
        s.sort()  # Listeyi sıralar; en az bulunan karakter en başta, en çok bulunan karakter en sonda.

        # İki önceki karakterin son iki karakter ile aynı olup olmadığını kontrol et
        if len(ans) >= 2 and ans[-2] == ans[-1] == s[2][1]:
            i = 1  # İki önceki karakter son iki karakter ile aynıysa, en fazla bulunan karakteri ekle.
        else:
            i = 2  # Aksi takdirde, en fazla bulunan karakteri ekle.

        if s[i][0]:  # Eğer seçilen karakterin sayısı sıfır değilse
            ans.append(s[i][1])  # Karakteri sonuç dizisine ekle
            s[i][0] -= 1  # Seçilen karakterin sayısını bir azalt.
        else:
            break  # Eğer sıfırsa döngüyü kır.

    return ''.join(ans)  # Sonuç dizisini birleştir ve döndür.
