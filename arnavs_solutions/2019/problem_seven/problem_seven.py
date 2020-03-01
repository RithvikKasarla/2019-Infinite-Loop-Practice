test_cases = int(input())

for _ in range(test_cases):
    list_length = int(input())

    first_value = float(input())
    brightness_values = [first_value]
    maximum = first_value
    minimum = first_value

    for _ in range(list_length - 1):
        value = float(input())
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value
        brightness_values.append(value)

    for value in brightness_values:
        converted = (value - minimum) / (maximum - minimum) * 255
        print(round(converted))
