from math import sqrt

def dist(a, b):
  return sqrt(a**2 + b**2)

def solver(a, b, pa=0, pb=0, n = 1):
  if n >= 51: return 1
  na = pa**2 - pb**2 + a
  nb = 2*pa*pb + b
  if dist(na, nb) >= 100: return 1
  return 1 + solver(a, b, na, nb, n + 1)

with open('official_ipt.txt', 'r') as iptfile:
  num_cases = int(iptfile.readline())
  for i in range(num_cases):
    a, b = iptfile.readline().split(" ")
    b = "".join(list(b)[:-1])
    print("{}+{}i".format(a, b), end=" ")

    a, b = float(a), float(b)
    out = solver(a, b)
    
    if out <= 10:
      print("RED")
      continue
    elif out <= 20:
      print("ORANGE")
      continue
    elif out <= 30:
      print("YELLOW")
      continue
    elif out <= 40:
      print("GREEN")
      continue
    elif out <= 50:
      print("BLUE")
      continue
    else:
      print("BLACK")
      continue