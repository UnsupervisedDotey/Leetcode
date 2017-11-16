class Solution:
	def reverse(self, x):

		if x > 0:

			x = list(map(int,str(x)))
			x = x[::-1]
			results=0
			for i in range(len(x)):
				results += x[i] * (10**(len(x)-i-1))

			if results > 2147483647:
				return 0

			return results
		elif x < 0:
			x = x*(-1)
			x = list(map(int,str(x)))
			x = x[::-1]
			results=0
			for i in range(len(x)):
				results += x[i] * (10**(len(x)-i-1))
			
			if results < -2147483647:
				return 0

			return -results
		else:
			return 0




x=120
hi=Solution()
hi.reverse(x)