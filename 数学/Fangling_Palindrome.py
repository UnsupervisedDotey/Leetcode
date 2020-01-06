class Solution:
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if x == -2147447412:
			return False
		elif x >= 0 and x <= 2147483648:
			xlist = list(str(x))
			length = len(xlist)

			if length%2 == 0:
				lr_len = int(length/2)
				bool = 1
				for each in range(lr_len):
					if int(xlist[each]) == int(xlist[lr_len+lr_len-each-1]):
						bool = bool * 1
					else:
						bool = bool * 0
				if bool == 1:
						bool = True
				elif bool ==0:
					bool = False
					
				return bool
			
			elif length == 1:
				return True
			else:
				middle = int((length+1)/2)-1
				lr_len = int((length-1)/2)

				bool = 1
				for each in range(lr_len):
					if int(xlist[each]) == int(xlist[middle + lr_len - each]):
						bool = bool * 1
					else:
						bool = bool * 0

				if bool == 1:
					bool = True
				elif bool ==0:
					bool = False
					
				return bool
			
			

		elif x< 0 and x >= -2147483648:
			xlist = list(str(x))
			xlist = xlist[1:]

			length = len(xlist)

			if length%2 == 0:
				lr_len = int(length/2)
				bool = 1
				for each in range(lr_len):
					if int(xlist[each]) == int(xlist[lr_len+lr_len-each-1]):
						bool = bool * 1
					else:
						bool = bool * 0
				if bool == 1:
						bool = True
				elif bool ==0:
					bool = False
					
				return bool
			
			elif length == 1:
				bool = False			
			else:
				middle = int((length+1)/2)-1
				lr_len = int((length-1)/2)

				if int(xlist[middle]) == 0:
					bool = False
					return bool
				else:
					bool = 1
					for each in range(lr_len):
						if int(xlist[each]) == int(xlist[middle + lr_len - each]):
							bool = bool * 1
						else:
							bool = bool * 0

					if bool == 1:
						bool = True
					elif bool ==0:
						bool = False
					return bool
			
			return bool



			





x = 101
sol = Solution()
sol.isPalindrome(x)