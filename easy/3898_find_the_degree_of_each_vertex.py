"""You are given a 2D integer array matrix of size n x n 
representing the adjacency matrix of an undirected graph 
with n vertices labeled from 0 to n - 1.

matrix[i][j] = 1 indicates that there is an edge between vertices i and j.
matrix[i][j] = 0 indicates that there is no edge between vertices i and j.
The degree of a vertex is the number of edges connected to it.

Return an integer array ans of size n where ans[i] represents the degree of vertex i."""

class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = [None]*len(matrix)
        for i in range(len(matrix)):
            ans[i] = sum(matrix[i])
        return ans