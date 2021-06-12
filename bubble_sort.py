def bubble_sort(data):
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp


my_data = [5, 3, 0, 8, 10, 1, 2, 9]


bubble_sort(my_data)

print(my_data)
