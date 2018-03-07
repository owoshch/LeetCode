class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        else:
            max_so_far = prices[1] - prices[0]
            cur_max = prices[1] - prices[0]
            print (max_so_far, cur_max)
            for i in range(1, len(prices) - 1):
                cur_max = max(prices[i + 1] - prices[i], \
                              cur_max + prices[i + 1] - prices[i])
                max_so_far = max(max_so_far, cur_max)
            return max(max_so_far, 0)