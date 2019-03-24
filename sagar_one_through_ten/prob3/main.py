#1st, 2nd, 3rd, 4th, 5th, 6th, 7th, ... 11th, 12th ... 15th, 17th, 21st, 22nd, 23rd, 24th

def suffix(line):
    line = list(line)
    line = line[:-2]
    curr = line[-2:]
    curr = "".join(curr)
    line = "".join(line)
    if not (int(curr) > 10 and int(curr) < 20) and (curr[-1] in ['1', '2', '3']):
        curr_last = curr[-1]
        
        if curr_last == '1': return line + "st"
        elif curr_last == '2': return line + "nd"
        else: return line + "rd"
    else:
        return line + "th"

if __name__ == '__main__':
    print(suffix('1th'))