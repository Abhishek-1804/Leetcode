class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) > 1:
            mid = len(arr) // 2  # Finding the mid of the array
            left_half = arr[:mid]  # Dividing the elements into 2 halves
            right_half = arr[mid:]

            self.sortArray(left_half)  # Sorting the first half
            self.sortArray(right_half)  # Sorting the second half

            i = j = k = 0

            # Copy data to temp arrays left_half[] and right_half[]
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return arr