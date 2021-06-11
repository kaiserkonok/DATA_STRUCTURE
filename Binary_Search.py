def binary_search(data, length, find):
    start = 0
    end = length - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == find:
            return f"Data Found at index {mid}"
        elif find > data[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return "Data Not found"


lists = [1, 2, 3, 4, 5]

find_data = 3

print(binary_search(lists, len(lists), find_data))
