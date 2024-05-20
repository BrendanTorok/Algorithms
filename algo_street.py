"""
 You are working for a promising new stock trading startup called "AlgoStreet."

 You have been tasked with developing a new trading signal that will be incorporated into the
 automatic trading strategy. A new metric has been introduced called

 positive stock pressure, which measures how many consecutive days before today (not includ-
 ing today) have a higher price.

 You will be given daily stock prices for the last N days and must return the list of daily positive
 stock pressures for each day.

 Below is an example for 1 week of data.

 |   Price   | Stock Pressure
 ------------------------------
 | Day 1 |   100     |     1
 ------------------------------
 | Day 2 |   90      |     2
 ------------------------------
 | Day 3 |   95      |     1
 ------------------------------
 | Day 4 |   100     |     1
 -------------------------------
 | Day 5 |   105     |     1
 -------------------------------
 | Day 6 |   110     |     1
 -------------------------------
 | Day 7 |   80      |     7
 -------------------------------

 Implement the function to compute stock pressure.

 To compute positive stock pressure for each stock price, you should find the last day with the
 lower (or equal) price. In other words, the positive stock pressure is the number of days since the
 last day with a lower or equal price.

 You must solve this problem by using a stack as the primary data structure.


Code Author: Brendan Torok

Running Time Analysis of compute_pressure
--------------------
Checking if the list is empty and returning an empty list if it is has a time complexity of O(1)
Instantiating variables has a time complexity of O(1)
Looping through each stock in the list has a time complexity of O(n) because each stock must be iterated over
The while loop does not iterate n times for every element, and only a maximum of n times. Despite being nested,
it does not act as a nested for loop and contributes O(n) time complexity
Setting the last day has a time complexity of O(1)
Adding to the stack has a time complexity of O(1)
Computing the final values has a time complexity of O(n)
Returning the final pressure has a time complexity of O(1)

The overall time complexity of the function is therefore O(n + n) but simplifies to O(n)
"""


def compute_pressure(stock_history: list):
    # if the list provided is empty then return an empty list
    if len(stock_history) == 0:
        return []
    # initialize a stack for price and a second stack for days to keep track of the day of the curr lowest price
    # initialize the pos_pressure list to put into
    stack = []
    days = []
    curr_day = 1
    pos_pressure = []

    # loop through each stock in the list
    for stock_price in stock_history:
        # while the stack is not empty and the stock price is less than then current top of the stack
        # remove the top element in the stack and the top element in the days stack
        while len(stack) != 0 and stock_price < stack[-1]:
            stack.pop()
            days.pop()

        # set the last day to be 0 if the days stack is empty
        # else set the current last day to the top of the days stack
        if len(days) == 0:
            last_day = 0
        else:
            last_day = days[-1]

        # if the stack is empty, or the current price is greater than or equal to the top of stack
        # then append the current price to stack and day to days
        stack.append(stock_price)
        days.append(curr_day)

        # Calculate and append the pressure to the pos pressure list and increment the current day
        pressure_calc = curr_day - last_day
        pos_pressure.append(pressure_calc)
        curr_day += 1

    return pos_pressure


"""
DO NOT EDIT BELOW THIS
Below is the unit testing suite for this file.
It provides all the tests that your code must pass to get full credit.
"""


class TestGeneratePressure:
    def run_unit_tests(self):
        self.test_example()
        self.test_2()
        self.test_3()
        self.test_no_days_provided()
        self.test_large_list()
        self.test_repeating_prices()

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
        stock_history = [100, 90, 95, 100, 105, 110, 80]

        result = compute_pressure(stock_history)
        expected_answer = [1, 2, 1, 1, 1, 1, 7]

        self.test_answer("test_example", result, expected_answer)

    def test_2(self):
        stock_history = [80, 74, 75, 90, 120, 81]

        result = compute_pressure(stock_history)
        expected_answer = [1, 2, 1, 1, 1, 3]

        self.test_answer("test_2", result, expected_answer)

    def test_3(self):
        stock_history = [1, 2, 5, 10, 12, 20]

        result = compute_pressure(stock_history)
        expected_answer = [1, 1, 1, 1, 1, 1]

        self.test_answer("test_3", result, expected_answer)

    def test_no_days_provided(self):
        stock_history = []

        result = compute_pressure(stock_history)
        expected_answer = []

        self.test_answer("test_no_days_provided", result, expected_answer)

    def test_large_list(self):
        stock_history = [100, 90, 80, 85, 90, 95, 100, 105, 110, 120, 140, 120, 100, 80]

        result = compute_pressure(stock_history)
        expected_answer = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 6, 11]

        self.test_answer("test_large_list", result, expected_answer)

    def test_repeating_prices(self):
        stock_history = [10, 10, 10]

        result = compute_pressure(stock_history)
        expected_answer = [1, 1, 1]

        self.test_answer("test_repeating_prices", result, expected_answer)


if __name__ == '__main__':
    test_runner = TestGeneratePressure()
    test_runner.run_unit_tests()
