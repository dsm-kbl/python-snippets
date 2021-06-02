##########################################################
# Lists
L = [123, 'spam', 1.23]
print("Length of the list L : ", len(L))  # Length of a list
# Slicing a list returns a new list
print(L[:-1])
# Concat lists
print(L + [4, 5, 6])
# Append to lists
L.append('NI')
print(L)
# Delete an item in the middle
L.pop(2)  # del L[2] works in a similar way
print(L)

# Sorting a list
M = ['bb', 'cc', 'aa']
M.sort()
print(M)
M.reverse()
print(M)

# Nesting
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])

# Get a column of a matrix
col2 = [row[1] for row in matrix]
print(col2)

print(list(range(4)))
print(list(range(-6, 7, 2)))

# Generators
G = (sum(row) for row in matrix)
print(next(G))
print(next(G))
print(next(G))
