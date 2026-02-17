# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


class Solution(object):
    def topKFrequent(self, nums, k):

        freq = {}

        # Step 1: Count frequency
        for num in nums: #this means going through each number in the input list 'nums', here 
            #nums can be list , tuple or any iterable object that contains numbers ,teh loop will iterate through each element in that list and assign it to the variable 'nums' one by one 
            freq[num] = freq.get(num, 0) + 1 #this is counting the frequency of each number in the input list 'nums' and storing it in a dictionary called 'freq'.
#             #.get(num, 0) is a dictionary method that:

# If num exists as a key in freq, returns its current value (count)

# If num doesn't exist, returns the default value 0
        # Step 2: Sort by frequency descending
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # freq.items()  # Returns a view of dictionary key-value pairs as tuples
        # sorted(freq.items(), key=lambda x: x[1], reverse=True)  # Sorts items by frequency (value) in descending order
        #key = lambda x: x[1] means we want to sort by the second element of each tuple (the frequency count)
        #reverse=True means we want the highest frequencies first (descending order)

        # Step 3: Take first k elements
        result = []

        for i in range(k): #this loop will run k times, where k is the number of most frequent elements we want to return.
            result.append(sorted_items[i][0]) # sorted_items[i] gives us the i-th tuple in the sorted list, which is (number, frequency). sorted_items[i][0] gives us the number itself (the first element of the tuple), which we append to the result list.

        return result # Finally, we return the result list, which contains the k most frequent elements from the input list 'nums'.

