from itertools import combinations
class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Bitwise OR nedir?:
        #sayıların 2'lik sistemdeki karşılık-
        #larının altalta toplanmasıyla elde
        #edilir. Örneğin;
        # 3  011        0,0 -> 0
        # 2  010        0,1 -> 1
        #OR_______      1,1 -> 1
        #    011

        #elimizdeki nums dizisinin max
        #bitwise OR'u zaten elimizdeki
        #elemanların hepsinin olduğu
        #durumdur. 

        #ADIMLAR
        #1) fonk1: dizinin alt
        #kümelerini bulan.
        #2) max BitwiseOR bulunmalı
        #3) altkümeler içindeki max BitwiseOR
        #kuralına uyan altkümeler sayılmalı
        
        #liste içindeki max BTOR'u bulma
        def mxController(liste1):

            mxBtOR = 0
            for num in liste1:
                mxBtOR |= num
            return mxBtOR

        # alt kümeler
        def controller(nums):
            kumeler = []
            count = 0
            mx = mxController(nums)
            for i in range(len(nums) + 1):
                for kume in combinations(nums,i):
                    if(mx == mxController(kume)):
                        count += 1
            return count
        
        return controller(nums)




