def isPalindrome(s): 
    rev = s[::-1] 
    if (s == rev): 
        return True
    return False

with open("Probinput.txt") as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    test = lines [0]
    lines = lines[1::]
    wrong = []
    place = 0
    t=0
    for x in range(0,int(test.strip())):
        t = lines[0]
        print("lines:",lines)
        del lines[:int(place)]
        print("2 lines:",lines,place)

        pal = True
        fal = "False"
        place = place + int(t)
        for y in range(0,int(t.strip())):
            if not isPalindrome(lines[y]):
                pal = False
                fal += str(1+x)
        if len(fal) > 5:
            wrong.append(fal)
        else:
            wrong.append("True")
    for z in wrong:
        print(z)
                
            
    
