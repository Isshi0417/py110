# PEDAC Guided Practice: Leftover Blocks

### Step 1: Understand the Problem

#### Leftover Blocks

*You have a number of building blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:*

- *The building blocks are cubes.*
- *The structure is built in layers.*
- *The top layer is a single block.*
- *A block in an upper layer must be supported by four blocks in a lower layer.*
- *A block in a a lower layer can support more than one block in an upper layer.*
- *You cannot leave gaps between blocks.*

*Write a program that, given the number of available blocks, calculates the number of blocks left over after building the tallest possible valid structure.*

#### Tasks

*You are provided with the problem description above. Your task for this step are:*

- *Make notes of your mental model for the problem, including:*
  - *inputs and outputs.*
  - *explicit and implicit rules.*

- *Write a list of clarifying questions for anything that isn’t clear.*

#### Problem

**Input**: Integer representing the number of building blocks available

**Output**: Integer representing the number of left over building blocks after building the tallest possible structure



**Rules:**

- *Explicit:* 
  - Building blocks are cubes.
  - The structure is built in layers.
  - The top layer of the structure only has one block.
  - A block in the upper layer must be supported by four blocks in a lower layer.
  - A block in a lower layer can support more than one block in an upper layer.
  - There cannot be gaps between blocks.
- *Implicit:*
  - The number of blocks in a layer is its squared value.



**Questions:**

- Can the lower layer have more blocks than necessary?

### Step 2: Example and Test Cases

*You are provided with the following test cases for this problem:*

```python
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
```

*Regarding your initial mental model and questions from Step 1, make some notes about the test cases. Do the test cases confirm or refute different elements of your original analysis and mental mode? Do they answer any of the questions you had, or do the perhaps raise further questions?*

#### Notes

The test cases confirm that the structures form a shape that resembles a pyramid. The base gets larger as more layers are added to the structure. It seems like the program should take out the unnecessary blocks and count it as a left over block.

