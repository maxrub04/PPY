#task_2
def process_data(data):
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

    filtered_data = [item for item in sorted_data if item[1] >= 18 and item[2] == True]

    sorted_names = [item[0].upper() for item in filtered_data]

    ages = [item[1] for item in filtered_data]

    avg_age = sum(ages) / len(ages) if ages else None

    active_count = sum(1 for item in data if item[2] == True)

    return {
        "sorted_names": sorted_names,
        "ages": ages,
        "avg": avg_age,
        "active_count": active_count
    }

data = [ ("Alice", 30, True), ("Bob", 15, True), ("Charlie", 25,
False), ("David", 40, True), ("Eve", 17, False), ("Frank", 20, True)]
print(process_data(data))









