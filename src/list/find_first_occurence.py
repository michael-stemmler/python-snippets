original_list = ['first', 'second', 'third', 'fourth', 'fifth']

# search for the first element which contains character 'o'
first_elem = next(x for x in original_list if 'o' in x)

print(first_elem)