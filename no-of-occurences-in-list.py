# Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.
# 
# Example 1:
# 
# Input:
# N = 7, X = 2
# Arr[] = {1, 1, 2, 2, 2, 2, 3}
# Output: 4
# Explanation: 2 occurs 4 times in the
# given array.

class Solution:

	def count(self,arr, n, x):
		# code here
		counter = 0
		for i in arr:
		    if i == x:
		        counter += 1
		return counter
