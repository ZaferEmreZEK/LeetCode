class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        #tek yer değişikliğiyle oluşturabileceğim
        #en büyük sayıyı oluşturacaksam;
        #sol baştan başlayarak "liste içindeki en
        #büyük sayı bu mu?" diye kontrol ederim.
        #eğer o ise ellemem, değilse liste
        #liste içindeki en büyük sayıyla yer
        #değiştirip döngüden çıkarım.

        #öncelikle int değeri listeye atıyoruz.
        str_num = str(num)
        int_list = []
        for chr in str_num:
            int_list.append(int(chr))
        #liste içinde dönerek en büyük mü
        #kontrolü yapacağız.
        temp = 0 #geçici eleman
        mx_temp = 0
        for i in range(len(int_list)):
            print(i,"---")
            print(max(int_list[i:]))
            max_deger = max(int_list[i:])
            if int_list[i] != max_deger:
                print("girdi")
                temp = int_list[i]
                print("int_list[i]",int_list[i],"temp ", temp)

                # Listeyi ters çeviriyoruz
                reversed_list = int_list[i:][::-1]

                # Ters listede en büyük değeri bul ve indeksini al
                max_value = max(reversed_list)
                reversed_index = reversed_list.index(max_value)

                # Orijinal listede max_value'nun son geçtiği yerin indeksini hesapla
                index_temp = len(int_list) - 1 - reversed_index
                
                mx_temp = int_list[index_temp]
                print("max ",int_list[index_temp])
                int_list[index_temp] = temp
                int_list[i] = mx_temp
                break

        new_num = 0
        for chr in int_list:
            new_num = new_num * 10 + chr

        return new_num



