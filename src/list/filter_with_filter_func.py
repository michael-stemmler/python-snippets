original_list = ['first', 'second', 'third', 'fourth', 'fifth']

# filter for all elements containing the character 'i'
filtered_list = filter(lambda s: 'i' in s, original_list)

print(list(filtered_list))
