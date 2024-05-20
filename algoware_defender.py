"""
You are working for a new cybersecurity company “AlgoWare Defender” on a decoding tool.
The decoding tool is meant to help reverse a nefarious one way encoding scheme of letters to digits.

The encoding scheme coverts letter strings into numeric strings by
converting each letter to a digit based on its place in the alphabet.

Here is the encoding table
A : 1
B : 2
…
Z : 26

For example, the string ZAB maps to 2612.

The nefarious part of this scheme is that it is not reversible!

However, if you are given 2612 this could be decoded in multiple ways

26 1 2 = ZAB
2 6 12 = BFL
2 6 1 2 = BFAB
26 12 = ZL

AlgoWare Defender’s decoding tool will have a few components; you are working on the first piece:
determining how many decodings are possible. For example, there are 4 decodings for 2612

You must write a function: findNumDecodings
which when given a string of digits returns the number of possible decodings.

Your program must be efficient and must use dynamic programming.

You must also provide an explanation of the running time of your code

Code Author: Brendan Torok

Running Time Analysis
--------------------
Checking if the string length is equal to 0 takes O(1) time
Initializing the tracker list takes O(n) time where n is the length of the string
Initializing the base cases takes O(1) time
Iterating through the string takes O(n) time where n is the length of the list
Checking the string values and updating the tracker list takes O(1) time
Creating the combination integer from the string values takes O(1) time
Returning the last index of the tracker array takes O(1) time

Therefore the overall time complexity is O(n) where n is the length of the string input
"""
from itertools import combinations


def find_num_decodings(string: str):
    # return 1 if the string is empty, only 1 way to decode an empty string
    if len(string) == 0:
        return 1

    # create tracker list, initialized to all be 0, for the number of elements in the list plus 1
    tracker = [0] * (len(string) + 1)

    # base case initialization, if there is one only char, there is 1 way to decode
    tracker[0] = 1
    # if the first char of the string is not 0, then there is a minimum of 1 way to decode so the index is
    # updated to be 1, otherwise it is left as 0 since there are no valid ways to decode if the string starts with 0
    if string[0] != '0':
        tracker[1] = 1

    # iterate from 2 to n + 1 to populate tracker, keeping track of how many decodings there are.
    # start at index 2 since base cases for i = 0 and 1 have already been set
    for i in range(2, len(string) + 1):
        # decode for single digits, checking index string i-1, if it is not 0, then update the curr tracker index
        if string[i - 1] != '0':
            tracker[i] = tracker[i] + tracker[i - 1]

        # add the previous two digits together and check if they are between 10 and 26, if so add to the tracker
        # use tracker i - 2 to add to the current tracker index, as there are i-2 ways to decode in addition to i-1
        combination = int(string[i - 2:i])
        if combination in range(10, 27):
            tracker[i] = tracker[i] + tracker[i - 2]

    # return the last element in the tracker list, this is the element containing the number of ways to decode
    return tracker[-1]


class TestFindNumDecodings:
    def run_unit_tests(self):
        self.test_example()
        self.test_empty()
        self.test_single()
        self.test_double()
        self.test_invalid_1()
        self.test_invalid_2()
        self.test_normal_1()
        self.test_normal_2()
        self.test_normal_3()
        self.test_many_ones()

    def print_test_result(self, test_name, result):
        color = "\033[92m" if result else "\033[91m"
        reset = "\033[0m"
        print(f"{color}[{result}] {test_name}{reset}")

    def test_answer(self, test_name, result, expected):
        if result == expected:
            self.print_test_result(test_name, True)
        else:
            self.print_test_result(test_name, False)
            print(f"Expected: {expected} \nGot:      {result}")

    def test_example(self):
        result = find_num_decodings("2612")
        expected_answer = 4

        self.test_answer("test_example", result, expected_answer)

    def test_empty(self):
        result = find_num_decodings("")
        expected_answer = 1

        self.test_answer("test_empty", result, expected_answer)

    def test_single(self):
        result = find_num_decodings("8")
        expected_answer = 1

        self.test_answer("test_single", result, expected_answer)

    def test_double(self):
        result = find_num_decodings("25")
        expected_answer = 2

        self.test_answer("test_double", result, expected_answer)

    def test_invalid_1(self):
        result = find_num_decodings("0")
        expected_answer = 0

        self.test_answer("test_invalid_1", result, expected_answer)

    def test_invalid_2(self):
        result = find_num_decodings("1200")
        expected_answer = 0

        self.test_answer("test_invalid_2", result, expected_answer)

    def test_normal_1(self):
        result = find_num_decodings("123456789")
        expected_answer = 3

        self.test_answer("test_normal_1", result, expected_answer)

    def test_normal_2(self):
        result = find_num_decodings("1011121314151617181920212223242526")
        expected_answer = 86528

        self.test_answer("test_normal_2", result, expected_answer)

    def test_normal_3(self):
        result = find_num_decodings("1232020410105")
        expected_answer = 3

        self.test_answer("test_normal_3", result, expected_answer)

    def test_many_ones(self):
        result = find_num_decodings("1111111111111111111111111111111111111111")
        expected_answer = 165580141

        self.test_answer("test_many_ones", result, expected_answer)


if __name__ == '__main__':
    test_runner = TestFindNumDecodings()
    test_runner.run_unit_tests()
