def addiply(line):
    line = line.split(" ")
    return( str(int(line[0])+ int(line[1])) + " "+  str(int(line[0])*int(line[1]) ) ) 

if __name__ == "__main__":
    with open('input.txt') as file:
        lines = file.readlines()[1:]
        for line in lines:
            print(addiply(line.strip()))
        