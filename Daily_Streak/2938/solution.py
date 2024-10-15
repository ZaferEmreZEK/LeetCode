class Solution(object):
    def minimumSteps(self, s):
        steps = 0 #minimum steps
        black = 0 #readed black count
        n = len(s) #length of the input

        # iteration from the end to the beginning
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                black += 1
                steps += n - i - black

        return steps

        