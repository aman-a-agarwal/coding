class Solution:
    def searchInsert(self, nums, target: int) -> int:
        j = 0

        low, high = 0, len(nums)
        mid = low + (high - low) // 2

        while mid != low:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid
            else:
                high = mid
            mid = low + (high - low) // 2
        return mid if target <= nums[mid] else mid + 1

    def circularSearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        low = 1
        high = len(nums)
        mid = (low + high) / 2
        while nums[mid] > nums[mid - 1] and low != mid:
            if low == mid:
                mid = len(nums)
                break
            if nums[0] < nums[mid]:
                low = mid
            else:
                high = mid
            mid = (low + high) / 2
        # new array start at mid
        low, high = (0, mid) if target >= nums[0] and target <= nums[mid - 1] else (mid, len(nums))
        mid = (high + low) / 2
        while low != mid:
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                low = mid
            else:
                high = mid
            mid = (high + low) / 2
        return -1 if nums[low] != target else low

    def maxSubArray(self, nums) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            if cur_sum > 0:
                cur_sum += num
            else:
                cur_sum = num
            max_sum = max(cur_sum, max_sum)
        return max_sum

    def set_Zeroes(self, matrix) -> int:
        i_list = set()
        j_list = set()

        i = 0
        for el in matrix:
            j = 0
            for item in el:
                if (item == 0):
                    j_list.add(j)
                    i_list.add(i)
                j += 1
            i += 1

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i in i_list or j in j_list):
                    matrix[i][j] = 0

    """
    def generate(self, numRows):
        # Optimal solution
        # :type numRows: int
        # :rtype: List[List[int]]

        if numRows == 0:
            return []
        res = [[1]]
        for j in range(numRows - 1):
            prev = res[-1]
            next = [1]
            for i in range(len(prev) - 1):
                next.append(prev[i] + prev[i + 1])
            next.append(1)
            res.append(next)
        return res
    """

    def generatePascalsTriangle(self, numRows):
        pascal = []
        for i in range(numRows):
            pascal.append([1] * (i + 1))

        for row in range(len(pascal)):
            if (row > 1):
                for col in range(len(pascal[row])):
                    if ((col > 0) and (col < row)):
                        pascal[row][col] = pascal[row - 1][col - 1] + pascal[row - 1][col]
        return pascal

    def Pascal2(self, numRows: int):
        if numRows == 0:
            return []
        res = [[1]]
        for j in range(numRows - 1):
            prev = res[-1]
            next = [1]
            for i in range(len(prev) - 1):
                next.append(prev[i] + prev[i + 1])
            next.append(1)
            res.append(next)
        return res

    """
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return d[target - num], i
            d[num] = i
    """

    def twoSum(self, nums: [int], target: int) -> [int]:
        i = 0
        for num in nums:
            j = i + 1
            for num2 in nums[i + 1:]:
                if ((num + num2) == target):
                    return [i, j]
                j = j + 1
            i = i + 1

    def majorityElement(self, nums: [int]) -> int:
        counter = dict()

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
            if counter[num] > (len(nums) / 2):
                return num

    def plusOne(self, digits: [int]) -> [int]:
        index = len(digits) - 1
        for num in digits[::-1]:
            if (num == 9):
                digits[index] = 0
                index -= 1
            else:
                digits[index] += 1
                break
        if sum(digits) == 0:
            digits = [1] + ([0] * (len(digits)))
        return digits

    def selectionSort(self, A):
        for i in range(len(A)):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(A)):
                if A[min_idx] > A[j]:
                    min_idx = j

                    # Swap the found minimum element with
            # the first element
            A[i], A[min_idx] = A[min_idx], A[i]

    def findKthLargest(self, nums: [int], k: int) -> int:
        for i in range(k):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(nums)):
                if nums[min_idx] < nums[j]:
                    min_idx = j

                    # Swap the found minimum element with
            # the first element
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

        return nums[k - 1]

    def areRotations(self, string1, string2):
        # Check if sizes of two strings are same
        if len(string1) != len(string2):
            return 0

        # Create a temp string with value str1.str1
        temp = string1 + string1

        # Now check if str2 is a substring of temp
        # string.count returns the number of occurences of
        # the second string in temp
        if (temp.count(string2) > 0):
            return 1
        else:
            return 0

    def consecutiveGreyCode(self, num1, num2):
        if (len(num1) != len(num2)):
            return 0

        xor = num1 ^ num2
        if sum(xor) == 1:
            return 1
        else:
            return 0

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # print(node)
        # node.val = node.next.val
        # node.next = node.next.next

        node = node.next
        print(node)

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        lag = ListNode(0)
        lag.next = head
        cur = cur.next

        for i in range(n):
            cur = cur.next

        while (cur != None):
            cur = cur.next
            lag = lag.next

        print(lag)

        lag.next = lag.next.next

        return head

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        """
        merged_head = ListNode(0)

        while (l2 and l1):
            if (l2.val < l1.val):
                merged_head.next = l2
                l2 = l2.next
            else:
                merged_head.next = l1
                l1 = l1.next
            merged_head = merged_head.next

        if (l1):
            merged_head.next = l1
        if (l2):
            merged_head.next = l2

        return merged_head"""

        res = ListNode(0)
        iter = res
        while l1 and l2:
            if l1.val < l2.val:
                iter.next = l1
                l1 = l1.next
            else:
                iter.next = l2
                l2 = l2.next
            iter = iter.next
        if l1:
            iter.next = l1
        if l2:
            iter.next = l2
        return res.next

    def isPalindrome(self, head):

        if (head is None):
            return True

        curr = head
        prev = None

        while (curr != None):
            temp = ListNode(curr.val)
            temp.next = prev

            curr = curr.next
            prev = temp

        if (prev is None):
            return True

        while (head != None):
            if (head.val != prev.val):
                return False
            head = head.next
            prev = prev.next

        return True
