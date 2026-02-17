for num in nums:
            freq[num] = freq.get(num, 0) + 1



# Line-by-Line Breakdown

# ## The Code
# ```python
# for num in nums:
#     freq[num] = freq.get(num, 0) + 1
# ```

# ## What This Code Does

# This is a **frequency counter** pattern. It counts how many times each number appears in a list (or any iterable).

# ---

# ## Line 1: `for num in nums:`

# ```python
# for num in nums:
# ```

# **Meaning:** Loop through each element in the collection `nums`

# - `nums` is a list, tuple, or any iterable containing numbers
# - `num` is the current element in each iteration
# - Example: if `nums = [1, 2, 1, 3, 1, 2]`, the loop runs 6 times

# ---

# ## Line 2: `freq[num] = freq.get(num, 0) + 1`

# This line does **three things** in one:

# ### Part A: `freq.get(num, 0)`

# ```python
# freq.get(num, 0)  # Try to get value for key 'num', return 0 if key doesn't exist
# ```

# **What it does:** Looks up the current count for this number in the dictionary

# - `freq` is a dictionary (hash map) that stores number → count mappings
# - `.get(num, 0)` is a dictionary method that:
#   - If `num` exists as a key in `freq`, returns its current value (count)
#   - If `num` doesn't exist, returns the default value `0`

# **Example:**
# ```python
# freq = {1: 2, 2: 1}  # Dictionary so far

# freq.get(1, 0)  # Returns 2 (exists)
# freq.get(2, 0)  # Returns 1 (exists)
# freq.get(3, 0)  # Returns 0 (doesn't exist)
# ```

# ### Part B: `+ 1`

# ```python
# freq.get(num, 0) + 1  # Add 1 to whatever we found
# ```

# **What it does:** Increments the count by 1

# - If number was seen before (count = 2): `2 + 1 = 3`
# - If number is new (count = 0): `0 + 1 = 1`

# ### Part C: `freq[num] = ...`

# ```python
# freq[num] = (new_count)  # Assign the new count back to the dictionary
# ```

# **What it does:** Stores the updated count back in the dictionary

# ---

# ## Complete Example Walkthrough

# ```python
# # Starting with empty dictionary
# freq = {}
# nums = [1, 2, 1, 3, 1, 2]

# # Iteration 1: num = 1
# freq[1] = freq.get(1, 0) + 1  # get(1,0)=0 → 0+1=1 → freq[1]=1
# # freq = {1: 1}

# # Iteration 2: num = 2
# freq[2] = freq.get(2, 0) + 1  # get(2,0)=0 → 0+1=1 → freq[2]=1
# # freq = {1: 1, 2: 1}

# # Iteration 3: num = 1
# freq[1] = freq.get(1, 0) + 1  # get(1,0)=1 → 1+1=2 → freq[1]=2
# # freq = {1: 2, 2: 1}

# # Iteration 4: num = 3
# freq[3] = freq.get(3, 0) + 1  # get(3,0)=0 → 0+1=1 → freq[3]=1
# # freq = {1: 2, 2: 1, 3: 1}

# # Iteration 5: num = 1
# freq[1] = freq.get(1, 0) + 1  # get(1,0)=2 → 2+1=3 → freq[1]=3
# # freq = {1: 3, 2: 1, 3: 1}

# # Iteration 6: num = 2
# freq[2] = freq.get(2, 0) + 1  # get(2,0)=1 → 1+1=2 → freq[2]=2
# # freq = {1: 3, 2: 2, 3: 1}

# # Final result: 1 appears 3 times, 2 appears 2 times, 3 appears 1 time
# ```

# ---

# ## Why Use This Pattern?

# ### Without `.get()` (More verbose):
# ```python
# for num in nums:
#     if num in freq:
#         freq[num] = freq[num] + 1
#     else:
#         freq[num] = 1
# ```

# ### With `.get()` (Elegant one-liner):
# ```python
# for num in nums:
#     freq[num] = freq.get(num, 0) + 1
# ```

# **Benefits:**
# - Shorter and cleaner
# - No need for explicit `if/else`
# - Handles missing keys gracefully
# - Very common pattern in coding interviews and real-world data processing

# ---

# ## Common Variations

# ```python
# # Counting characters in a string
# text = "hello"
# char_count = {}
# for char in text:
#     char_count[char] = char_count.get(char, 0) + 1
# # Result: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# # Counting words in a list
# words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
# # Result: {'apple': 3, 'banana': 2, 'cherry': 1}

# # Using defaultdict (alternative approach)
# from collections import defaultdict
# freq = defaultdict(int)
# for num in nums:
#     freq[num] += 1  # Even simpler!
# ```

# ---

# ## In Simple Terms

# **This code is asking:**
# > "For each number in my list, go to my counting dictionary, get the current count (or 0 if never seen before), add 1 to it, and put it back."

# It's like tallying votes: each time you see a number, you add a mark next to it.


