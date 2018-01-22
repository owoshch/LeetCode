class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # convert both A and B to dict of dicts
        # C[i,j] is equal to sum(A[i][k]*B[k][j])
        
        
        tableA = {}
        tableB = {}
        
        for i, row in enumerate(A):
            for j in range(len(row)):
                if row[j] != 0:
                    tableA.setdefault(i, {})[j] = row[j]

        for i, row in enumerate(B):
            for j in range(len(row)):
                if row[j] != 0:
                    tableB.setdefault(i, {})[j] = row[j]
        
        m = len(A)
        n = len(B[0])
                    
        C = [[0]*n for _ in range(m)]
        for i in tableA:
            # rows in A we need to consider
            for k in tableA[i]:
                # cols in A we need to consider
                if k in tableB:
                    for j in tableB[k]:
                        C[i][j] += tableA[i][k] * tableB[k][j]
                
        return C
        