"""
0th 1st 2nd 3rd 4th 5th 6th 7th 8th 9th 10th 11th 12th 13th 14th 15th 16th 17th 18th 19th 20th 21st 22nd 23rd 24th 25th 26th 27th 28th 29th 30th
"""

def doer(line):
  line = line[:-3]
  lint = int(line)
  lend = int(line[-1])
  if lint > 11 and lint < 20:
    return line + "th"
  if lend == 0:
    return line + "th"
  elif lend == 1:
    return line + "st"
  elif lend == 2:
    return line + "nd"
  elif lend == 3:
    return line + "rd"
  elif lend > 3:
    return line + "th"


with open("input.txt") as input_file:
    lines = input_file.readlines()[1:]

for line in lines:
  print(doer(line))
