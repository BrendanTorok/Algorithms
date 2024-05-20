"""

2Sum Problem Statement
Given an array of integers nums and an integer target, find the two integers that add up to a target.
The answer should be returned as an array of the two indices into the array  in ascending order.
If there is no solution return None.

You should assume that there is at most 1 solution
"""


def two_sum(nums: list, target: int):
    # First create a loop that goes from index 0 to the length of the nums list
    # this will choose the first index for a comparison value
    for x in range(0, len(nums)):
        # Create a second loop, starting at an index one above the x index for comparison
        # it is important the value is one index higher than the x index
        # so the same index is not used twice for comparison
        for y in range((x + 1), len(nums)):
            # complete comparison to target once both index values are found
            # simply add both values and compare to target value
            if nums[x] + nums[y] == target:
                # directly reference the index in order to deal with duplicate values
                return [x, y]
    # If there is no two values in the file that add to the target
    # then return None
    return None


class TestingBase:
    def print_test_result(self, test_name, result):
        color = "\033[92m" if result else "\033[91m"
        reset = "\033[0m"
        print(f"{color}[{result}] {test_name}{reset}")

    def test_answer(self, test_name, expected, result):
        if result == expected:
            self.print_test_result(test_name, True)
        else:
            self.print_test_result(test_name, False)
            print(f"Expected: {expected} \nGot:      {result}")


class TestTwoSum(TestingBase):
    def run_unit_tests(self):
        self.test_example()
        self.test_simple()
        self.test_no_answer()
        self.test_duplicate_values()
        self.test_longer_list()

    def test_example(self):
        nums = [3, 4, 5, 10]
        target = 13
        expected = [0, 3]
        self.test_answer("test_example", expected, two_sum(nums, target))

    def test_simple(self):
        nums = [1, 3, 7]
        target = 8
        expected = [0, 2]
        self.test_answer("test_simple", expected, two_sum(nums, target))

    def test_no_answer(self):
        nums = [1, 4, 6]
        target = 8
        expected = None
        self.test_answer("test_no_answer", expected, two_sum(nums, target))

    def test_duplicate_values(self):
        nums = [1, 4, 4, 6]
        target = 8
        expected = [1, 2]
        self.test_answer("test_duplicate_values", expected, two_sum(nums, target))

    def test_longer_list(self):
        nums = [2, 6, 3, 10, 5, 7, 1, 1, 3]
        target = 15
        expected = [3, 4]
        self.test_answer("test_longer_list", expected, two_sum(nums, target))


if __name__ == '__main__':
    test_runner = TestTwoSum()
    test_runner.run_unit_tests()
