from math import pi

testcases = int(input())
for testcase in range(testcases):
  orbit = float(input())
  r = orbit + (40075 / (2 * pi))
  print(round(2 * pi * r, 1))