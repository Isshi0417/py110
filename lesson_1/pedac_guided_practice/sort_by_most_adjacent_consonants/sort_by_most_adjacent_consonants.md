# PEDAC Guided Practice: Sort by Most Adjacent Consonants

## Step 1: Understand the Problem

### Sort Strings by Most Adjacent Consonants

*Given a list of strings, return a new list where the strings are sorted based on the highest number of adjacent consonants a string contains. If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.*

### Tasks

*You are provided with the problem description above. Your tasks for this step are:*

- *Make notes of your mental model for the problem, including:*
  - *inputs and outputs.*
  - *explicit and implicit rules.*
- *Write a list of clarifying questions for anything that isn’t clear.*

### Notes

**Input:** a set list of strings

**Output:** a new list of sorted strings based on the highest number of adjacent consonants

**Explicit Rules:**

- Strings must be sorted based on the highest number of adjacent consonants a string contains
- If two strings contain the same number of adjacent consonants, they should retain their original order
- Consonants are adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.

**Implicit Rules:**

- Strings can have more than one words.

**Questions**

- Do strings always contain more than one words?
- Can a string contain no adjacent consonants?
- What does “space between consonants in adjacent words” mean?
- Is it case sensitive?
- Should it be sorted in descending or ascending order?

## Step 2: Examples and Test Cases

*You are provided with the following test cases for this problem:*

```python
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
```

*Regarding your initial mental model and questions from Step 1, make some notes about the test cases. Do the test cases confirm or refute different elements of your original analysis and mental mode? Do they answer any of the questions you had, or do they perhaps raise further questions?*

### Clarifications

It clarifies the “space between consonants” a little more. In the second test case, the program considers ‘n’ and ‘c’ in ‘can can’ to be adjacent to one another. It can also be assumed that the strings can have more than one words or one word, but not an empty string. Since the input are all lowercase, it can be assumed that the program does not need to be case sensitive. The list should be sorted in descending order.

## Step 3: Data Structures

*For this step, with reference to your analysis from the two preceding steps, make some notes regarding whether you need to use any particular data structures in your solution. If so, which ones?*

### Notes

Both the inputs and outputs are lists, meaning the data structure will most likely be a list.

## Step 4: Algorithm

*For this step, use your analysis of the problem so far to write out a high-level algorithm that solves the problem at an abstract level. Avoid too much implementation detail at this stage.*

### High-level Algorithm

1. Determine the highest number of adjacent consonants within a string for each string in the list.
2. Sort the list based on the calculated highest number of consonants.
3. Return the sorted list.

### Algorithm

1. Remove spaces from the string
2. Initialize maximum consonants variable
3. Initialize adjacent consonants string variable
4. Iterate through each letter in the list
   - Add it to adjacent consonants string if letter is a consonant
   - Set the maximum consonant count to length of the adjacent consonants string if the letter is a vowel, greater in length than the current maximum consonants count, and adjacent consonants string has a length greater than 1.
   - Reset the adjacent consonants string
5. Return the maximum consonants count

## Step 5: Implement a Solution in Code

*Based on all of your notes and analysis so far, implement a working solution in Python. Your solution should pass all of the test cases provided.*



