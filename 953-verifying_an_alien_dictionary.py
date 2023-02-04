class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        lexi = {}
        for i, val in enumerate(order):
            lexi[val] = i
        for i in range(len(words) - 1):
            n = i + 1
            ix = 0
            while ix <= len(words[i]) and ix <= len(words[n]):
                val_i = lexi[words[i][ix]] if ix < len(words[i]) else -1
                val_n = lexi[words[n][ix]] if ix < len(words[n]) else -1
                if val_i < val_n:
                    break
                elif val_i == val_n:
                    ix += 1
                else:
                    return
        return True
