"""import math
class Solution(object):
    def maxArea(self, height):

        :type height: List[int]
        :rtype: int


        center = int(math.ceil(len(height) / 2))

        most = 0

        for left in range(len(height)):
            for right in range(left, len(height)):
                # print("left: ", left, "right:", right, "area: ", most)
                width = right - left
                h = min(height[right], height[left])

                area = width*h
                if area > most:
                    most = area

        return most
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        most = 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left = left + 1
            else:
                area = height[right] * (right - left)
                right = right - 1

            if area > most:
                most = area

        return most


sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))