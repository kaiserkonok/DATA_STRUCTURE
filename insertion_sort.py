# Insertion algorithm with python
def insertion_sort(data):
    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j] < data[j - 1]:
            temp = data[j]
            data[j] = data[j - 1]
            data[j - 1] = temp
            j = j - 1


my_data = [5, 4, 3, 2, 1, 0]

insertion_sort(my_data)

print(my_data)
