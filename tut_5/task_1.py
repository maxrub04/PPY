#task_1
def proccess_data(data):

    sorted_data = sorted(data, key=lambda x: x[0])

    filtered_data = [item for item in sorted_data if item[1] >= 5]

    squared_numbers = [item[1] ** 2 for item in filtered_data]

    sorted_strings = [item[0] for item in sorted_data]

    filtered_out_count = len(sorted_data) - len(filtered_data)

    return {
        "sorted_strings": sorted_strings,
        "squared_numbers": squared_numbers,
        "filtered_out_count": filtered_out_count
    }

data = [("apple", 3), ("banana", 7), ("cherry", 2), ("date", 10)]
print(proccess_data(data))









