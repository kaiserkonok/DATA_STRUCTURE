def selection_sort(data):
    for i in range(len(data) - 1):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            temp = data[i]
            data[i] = data[min_index]
            data[min_index] = temp


my_data = [4, 1, 2, 10, 20, 12, 11, 30]

selection_sort(my_data)

print(my_data)

