def get_average():
    with open("../Examples/data.txt","r") as file:
        Data = file.readlines()
    values = Data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local

average = get_average()
print(get_average())