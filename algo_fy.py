import heapq

'''
 You are working for a promising new music streaming service “Algo-fy”.
 Algo-fy would like to offer a new ranking feature that will track the top k most streamed songs of the day.

 You’ve been tasked with building a class “AlgoFy” that can track the most streamed songs
 and return an accurate list top k list at any point in time.

 Another team has already developed the song streaming feature: iStream and you will need to integrate with it.
 iStream will send AlgoFy play data as it processes customer requests.
 This data will be batched so the AlgoFy class will need to ingest lists of played songs multiple times

 A song is identified with an integer id number.

 The AlgoFy class will need to have the following methods:
 - Constructor(k): the number of songs to track in the topk
 - streamSongs(List of songIds): Receive a batch of streamed songs => updates internal state
 - getTopK(): return the top k most streamed songs in order

 As an example, the AlgoFy class may see the following usage:
 ranker = new AlgoFy(2)
 ranker.streamSongs([1, 1, 2, 2, 3])
 ranker.streamSongs([3, 3, 3, 1, 2, 1, 3])
 ranker.getTopK() => [3, 1]
 ranker.streamSongs([2, 2, 2, 2, 2])
 ranker.getTopK() => [2, 3]

 You must solve this problem by effectively using the properties of a Priority Queue or Heap.

 You must also provide an explanation of the running time of both getTopK and streamSongs

Code Author: Brendan Torok

Running Time Analysis of get_top_k
--------------------
Instantiating the top_k list takes O(1) time
The calls to create the stream_heap list has a time complexity of O(n) where n is the number of songs added.
The heapify call takes O(n) time as well, where n is the number of songs added to the heal.
The for loop to populate the top_k list runs n times, which at worst is equal to number of unique songs streamed, due 
to the min() call, therefore the loop has a time complexity of O(n). 
The call to append the return value of heappop() takes O(1) time, but the heappop() call takes O(logn) time due to the 
requirement to maintain heap order property after popping. Therefore, the loop has a worst case
time complexity of O(k + logn) 
Returning the top_k list takes O(1) time.
The overall time complexity is therefore calculated as O(n + n + nLogn) which can simplify.
Therefore, the overall time complexity of get_top_k is O(n + n*Logn).

--------------------

Running Time Analysis of stream_songs
Looping through the song IDs and adding them to a dictionary takes O(n) time as each song stream must be evaluated
Assigning each song ID to the dictionary and updating the play count within the for loop takes O(1) time
Therefore the overall time complexity is O(1 + n) time which simplifies to an overall time complexity of O(n) for
stream_songs

'''


class AlgoFy:
    def __init__(self, k):
        self.k = k
        self.song_streams = {}

    def stream_songs(self, songIds):
        # loop through all songs in songIds and create a hashmap, keeping track of the number of streams for each song
        for songId in songIds:
            self.song_streams[songId] = 1 + self.song_streams.get(songId, 0)

    def get_top_k(self):
        # create a max heap by taking the negative of the count value for each song in the song_streams hash map
        stream_heap = [(-count, songId) for songId, count in self.song_streams.items()]
        heapq.heapify(stream_heap)

        # instantiate a list for the top_k songs
        top_k = []
        # loop through whatever is smaller, the number of unique songs streamed or k
        for i in range(min(self.k, len(self.song_streams))):
            # for each k, append the most streamed song. Take index 1 to append songId and not stream count
            top_k.append(heapq.heappop(stream_heap)[1])

        return top_k


class TestAlgoFy:
    def run_unit_tests(self):
        self.test_example()
        self.test_example_2()
        self.test_many_batches()
        self.test_fewer_than_k()
        self.test_empty()

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
        ranker = AlgoFy(2)
        ranker.stream_songs([1, 1, 2, 2, 3])
        ranker.stream_songs([3, 3, 3, 1, 2, 1, 3])
        result = ranker.get_top_k()
        expected_answer = [3, 1]

        self.test_answer("test_example", result, expected_answer)

    def test_example_2(self):
        ranker = AlgoFy(2)
        ranker.stream_songs([1, 1, 2, 2, 3])
        ranker.stream_songs([3, 3, 3, 1, 2, 1, 3])
        ranker.get_top_k()
        ranker.stream_songs([2, 2, 2, 2, 2])

        result = ranker.get_top_k()
        expected_answer = [2, 3]

        self.test_answer("test_example_2", result, expected_answer)

    def test_many_batches(self):
        ranker = AlgoFy(5)

        for i in range(1, 10):
            for j in range(1, 15):
                ranker.stream_songs([i, j])
            ranker.get_top_k()
        ranker.stream_songs([3, 1, 1, 1, 2, 3])
        ranker.stream_songs([5, 4, 4, 3, 2, 2, 2, 1, 1])
        result = ranker.get_top_k()
        expected_answer = [1, 2, 3, 4, 5]

        self.test_answer("test_many_batches", result, expected_answer)

    def test_fewer_than_k(self):
        ranker = AlgoFy(4)

        ranker.stream_songs([1, 2, 3, 1, 2, 3, 1, 2, 1])
        result = ranker.get_top_k()
        expected_answer = [1, 2, 3]

        self.test_answer("test_fewer_than_k", result, expected_answer)

    def test_empty(self):
        ranker = AlgoFy(3)

        result = ranker.get_top_k()
        expected_answer = []

        self.test_answer("test_empty", result, expected_answer)


if __name__ == '__main__':
    test_runner = TestAlgoFy()
    test_runner.run_unit_tests()
