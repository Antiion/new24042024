import itertools
nice_list = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
            ]

new_list = [i for i1 in nice_list
            for i2 in i1
            for i in i2
            ]
print(new_list)