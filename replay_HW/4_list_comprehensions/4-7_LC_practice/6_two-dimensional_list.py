# ref_list = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# formula = 4*i + 1 + j

print([
    [(4*i+1) + j for i in range(3)]
    for j in range(4)
            ])
