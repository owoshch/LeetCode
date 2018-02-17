'''
Approach #1: Dynamic Programming (Postfix Variation) [Accepted]
Intuition

Let's work on a simpler problem: T = 'ab'. Whenever we find some 'b' in S, we look for the most recent 'a' that occurred before it, and that forms a candidate window 'a' = S[i], ..., S[j] = 'b'.

A weak solution to that problem would be to just search for 'a' every time we find a 'b'. With a string like 'abbb...bb' this would be inefficient. A better approach is to remember the last 'a' seen. Then when we see a 'b', we know the start of the window is where we last saw 'a', and the end of the window is where we are now.

How can we extend this approach to say, T = 'abc'? Whenever we find some 'c' in S, such as S[k] = 'c', we can remember the most recent window that ended at 'b', let's say [i, j]. Then our candidate window (that is, the smallest possible window ending at k) would be [i, k].

Our approach in general works this way. We add characters to T one at a time, and for every S[k] = T[-1] we always remember the length of the candidate window ending at k. We can calculate this using knowledge of the length of the previous window (so we'll need to remember the last window seen). This leads to a dynamic programming solution.

Algorithm

As we iterate through T[j], let's maintain cur[e] = s as the largest index such that T[:j] is a subsequence of S[s: e+1], (or -1 if impossible.) Now we want to find new, the largest indexes for T[:j+1].

To update our knowledge as j += 1, if S[i] == T[j], then last (the largest s we have seen so far) represents a new valid window [s, i].

In Python, we use cur and new, while in Java we use dp[j] and dp[~j] to keep track of the last two rows of our dynamic programming.

At the end, we look at all the windows we have and choose the best.

'''

class Solution(object):
    def minWindow(self, S, T):
        cur = [i if x == T[0] else None
               for i, x in enumerate(S)]
        #At time j when considering T[:j+1],
        #the smallest window [s, e] where S[e] == T[j]
        #is represented by cur[e] = s.
        for j in xrange(1, len(T)):
            last = None
            new = [None] * len(S)
            #Now we would like to calculate the candidate windows
            #"new" for T[:j+1].  'last' is the last window seen.
            for i, u in enumerate(S):
                if last is not None and u == T[j]: new[i] = last
                if cur[i] is not None: last = cur[i]
            cur = new

        #Looking at the window data cur, choose the smallest length
        #window [s, e].
        ans = 0, len(S)
        for e, s in enumerate(cur):
            if s >= 0 and e - s < ans[1] - ans[0]:
                ans = s, e
        return S[ans[0]: ans[1]+1] if ans[1] < len(S) else ""
