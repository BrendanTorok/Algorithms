import heapq
import math

"""
 You are working for a promising new “flight hacking” startup “AlgoJet”.
 The startup aims to find ultra-cheap flights by combining multiple flights from various airlines and by taking portions of multi leg flights.

 A database of flights is loaded into the AlgoFlight algorithm every morning with all offered flights.
 Flights will have:
 - Source
 - destination
 - price

 After initializing the system, customers can enter a source and destination city and get the cheapest flight (You will only need to return the price of the flight).

 If no flight path reaches the destination from the source, return -1

 You must solve this problem using a hand made graph data structure and Dijkstra’s algorithm.

 You are given the flight class which will be used to pass the list of flights.

 You will implement two methods:
 - initializeFlightGraph(List of flight objects)
 - getCheapestFlight(source, destination)

 You must provide a running time analysis of the getCheapestFlight function

 Code Author: Brendan Torok

 Running Time Analysis of get_cheapest_flight
  --------------------
 
 Checking if source is the destination has a time complexity of O(1)
 Initializing the prices of each flight to infinity has a time complexity of O(n) where n is the number of cities
 Initializing the price for the source city to be 0 has a time complexity of O(1)
 initializing the priority queue with the source city has a time complexity of O(1) since there is only the 
 source city in the queue
 
 The time complexity of the while loop is O(n) where n is the number of potential flights
 Popping from the queue has a time complexity of O(logm) where m is the number of elements in the queue
 Checking if the current city is the destination has a time complexity of O(1)
 
 Calculating the cost has a time compelxity of O(1)
 Adding the new city with the lowest cost to the heap has a time complexity of O(logm) where m is the number of cities
 in the heap since the heap order property must be maintained
 Checking if the price to the destination is infinity after the while loop is completed has a time complextiy of O(1)
 Returning the final price to the destination has a time complextiy of O(1)
 
 
 This time complexity is therefore O(n + nlogm) where n is the number of flights and m is the number of 
 potential cities visited. This simplifies to O(nlogm).
 --------------------
 
 """


class Flight:
    def __init__(self, source, destination, price):
        self.source = source
        self.destination = destination
        self.price = price


class AlgoJet:
    def __init__(self):
        self.graph = {}  # Recommended graph is {city: {destination : best_price}}

    def initialize_flight_graph(self, flights: list[Flight]):
        for flight in flights:

            # if the source is not currently in the graph, then initialize an empty value for dictionary for future
            # destinations that may be added
            if flight.source not in self.graph:
                self.graph[flight.source] = {}

            # if the destination is not mapped to the source, add the destination and initialize to infinity
            if flight.destination not in self.graph[flight.source]:
                self.graph[flight.source][flight.destination] = math.inf

            # update the flight prices to be the lowest value
            if self.graph[flight.source][flight.destination] > flight.price:
                self.graph[flight.source][flight.destination] = flight.price

        # add any destinations that might not have sources to the graph
        for flight in flights:
            if flight.destination not in self.graph:
                self.graph[flight.destination] = {}

    def get_cheapest_flight(self, source, destination):
        # error handling if source is destination
        if source == destination:
            return 0

        # Initialize price to each city as infinity
        prices = {city: math.inf for city in self.graph.keys()}
        # The price to the source city is 0 since you are already there
        prices[source] = 0
        # Initialize a priority queue with key 0 (price to city) and source (city to process)
        pq = [(0, source)]
        # while the priority queue is not empty, continue analyzing the price to the current city
        while pq:
            # pop the current cost of travel and the new city from the queue
            curr_cost, curr_city = heapq.heappop(pq)

            # if we reach the destination, then break out of the while loop
            if curr_city == destination:
                break

            # iterate through the potential destinations and flight prices for the current city
            for next_city, price in self.graph[curr_city].items():
                # update the current distance traveled for the potential new city
                cost = curr_cost + price

                # check if the new city price is lower than the currently calculated price to the new city
                # if the current destination price is lower, then cheaper path is found so the distance must be updated
                # and the destination along with the new lowest price is added to the queue
                if cost < prices[next_city]:
                    prices[next_city] = cost
                    # cities with the cheapest flights are given priority in this queue, so add cheapest flight to queue
                    heapq.heappush(pq, (cost, next_city))

        # return -1 if destination is not reachable in the graph
        if prices[destination] == math.inf:
            return -1

        # after the destination is reached and the while loop is broken, we return the shortest price to the
        # destination
        return prices[destination]


class TestAlgoFlights:
    def run_unit_tests(self):
        self.test_example()
        self.test_unreachable_destination()
        self.test_same_source_and_destination()
        self.test_cycle()
        self.test_multiple_flights()


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
        algo_jet = AlgoJet()
        flights = [
            Flight("A", "B", 100),
            Flight("A", "C", 150),
            Flight("B", "C", 40),
            Flight("B", "D", 200),
            Flight("C", "D", 100),
            Flight("C", "E", 120),
            Flight("D", "E", 80),
        ]
        algo_jet.initialize_flight_graph(flights)
        result1 = algo_jet.get_cheapest_flight("A", "E")
        result2 = algo_jet.get_cheapest_flight("A", "D")
        result3 = algo_jet.get_cheapest_flight("A", "C")
        result4 = algo_jet.get_cheapest_flight("B", "E")

        self.test_answer("test_example_1", result1, 260)
        self.test_answer("test_example_2", result2, 240)
        self.test_answer("test_example_3", result3, 140)
        self.test_answer("test_example_4", result4, 160)

    def test_unreachable_destination(self):
        algo_jet = AlgoJet()
        flights = [
            Flight("A", "B", 100),
            Flight("B", "C", 150),
            Flight("D", "E", 100),
        ]

        algo_jet.initialize_flight_graph(flights)

        result = algo_jet.get_cheapest_flight("A", "E")
        self.test_answer("test_unreachable_destination", result, -1)

    def test_same_source_and_destination(self):
        algo_jet = AlgoJet()
        flights = [
            Flight("A", "B", 100),
            Flight("B", "C", 150),
            Flight("C", "D", 100),
        ]

        algo_jet.initialize_flight_graph(flights)

        result = algo_jet.get_cheapest_flight("A", "A")
        self.test_answer("test_same_source_and_destination", result, 0)

    def test_cycle(self):
        algo_jet = AlgoJet()
        flights = [
            Flight("A", "B", 200),
            Flight("B", "C", 150),
            Flight("C", "D", 120),
            Flight("C", "A", 180),
            Flight("C", "B", 100),
            Flight("B", "E", 300),

        ]

        algo_jet.initialize_flight_graph(flights)

        result = algo_jet.get_cheapest_flight("A", "E")
        self.test_answer("test_cycle", result, 500)

    def test_multiple_flights(self):
        algo_jet = AlgoJet()
        flights = [
            Flight("A", "B", 200),
            Flight("B", "C", 150),
            Flight("A", "C", 140),
            Flight("A", "C", 180),
            Flight("A", "B", 100),
            Flight("B", "E", 300),
            Flight("B", "E", 250),
            Flight("C", "E", 220),

        ]

        algo_jet.initialize_flight_graph(flights)

        result = algo_jet.get_cheapest_flight("A", "E")
        self.test_answer("test_multiple_flights", result, 350)



if __name__ == '__main__':
    test_runner = TestAlgoFlights()
    test_runner.run_unit_tests()