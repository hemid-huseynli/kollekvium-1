def rotate_list(array, k):
    k = k % len(array)
    return array[-k:] + array[:-k]

my_list = [1, 2, 3, 4, 5]
k = 2
rotated_list = rotate_list(my_list, k)
print(rotated_list)