# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l, r = 0, reader.length() - 1
        while l < r:
            length = r - l + 1
            half = length // 2
            if length % 2 == 0:
                # Compare two halves: [l, l+half-1] vs [l+half, r]
                compare = reader.compareSub(l, l + half - 1, l + half, r)
                if compare == 1:
                    r = l + half - 1
                else:
                    l = l + half
            else:
                # Odd length: leave the middle element out
                compare = reader.compareSub(l, l + half - 1, l + half + 1, r)
                if compare == 1:
                    r = l + half - 1
                elif compare == -1:
                    l = l + half + 1
                else:
                    return l + half
        return l


