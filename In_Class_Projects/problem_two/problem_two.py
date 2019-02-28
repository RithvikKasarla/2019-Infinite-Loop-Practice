import os

with open(os.path.join(os.path.dirname(__file__), "Prob02.in.txt"))  as input_file:
    lines = input_file.readlines()[1:]
    
    vowels = ["a","e","i","o","u"]
    for line in lines:
        counter = 0
        z = list(line)
        for c in z:
            if c.lower() in vowels:
                counter += 1
        print(counter)