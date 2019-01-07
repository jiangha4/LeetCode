class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        all_nums = list()
        for x in range(0, num+1):
            count = 0
            binary = self.numToBin(x)
            for ele in binary:
                if ele == 1:
                    count = count + 1
            all_nums.append(count)
        return all_nums
        
    def numToBin(self, num):
        binary = list()
        while num > 0:
            binary.append(num%2)
            num = int(num/2)
        return binary