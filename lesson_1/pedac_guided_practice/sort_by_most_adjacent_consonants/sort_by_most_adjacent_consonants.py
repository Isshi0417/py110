'''A simple program that sorts the given list of strings into a descending order based
   on the number of adjacent consonants.'''

def count_max_adjacent_consonants(string):
    '''Counts largest count of adjacent consonants'''
    string = ''.join(string.split(' '))
    max_consonants_count = 0
    adjacent_consonants = ''
    for letter in string:
        if letter in 'bcdfghjklmnpqrstuvwxyz':
            adjacent_consonants += letter
            if len(adjacent_consonants) > max_consonants_count:
                if len(adjacent_consonants) > max_consonants_count:
                    max_consonants_count = len(adjacent_consonants)
        else:
            if len(adjacent_consonants) > max_consonants_count:
                if len(adjacent_consonants) > 1:
                    max_consonants_count = len(adjacent_consonants)

            adjacent_consonants = ''

    return max_consonants_count

def sort_by_consonant_count(strings):
    '''Sorts list in descending order'''
    strings.sort(key = count_max_adjacent_consonants, reverse = True)
    return strings

# Test cases
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
