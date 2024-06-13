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