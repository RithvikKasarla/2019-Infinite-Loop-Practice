test_cases = int(input())

for _ in range(test_cases):
    num_boarding_passes = int(input())

    origins = []
    destinations = []
    for _ in range(num_boarding_passes):
        origin, destination = input().split(" ")
        origins.append(origin)
        destinations.append(destination)

    first_location = -1
    for i, destination in enumerate(destinations):
        if destination not in origins:
            first_location = i
            break

    path = [destinations[first_location]]

    current_location = first_location

    while origins[current_location] in destinations:
        path.append(origins[current_location])
        next_location = destinations.index(origins[current_location])
        current_location = next_location

    path.append(origins[current_location])
    print("\n".join(path))
