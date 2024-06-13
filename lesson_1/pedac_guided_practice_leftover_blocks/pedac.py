def calculate_leftover_blocks(remaining_blocks):
    layer = 0
    blocks_necessary = int()

    while remaining_blocks >= blocks_necessary:
        remaining_blocks -= blocks_necessary
        layer += 1
        blocks_necessary = layer**2
    
    return remaining_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True