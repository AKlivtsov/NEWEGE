def func(n: int) -> int:
  n_bin = bin(n)[2:]

  if n % 4 == 0:
    n_bin += n_bin[:2]
  else:
    n_bin += bin(n % 4)[2:]

  while n_bin[:-1] == '0':
    n_bin = n_bin[:-1]

  return int(n_bin, 2)

for i in range(999):
  res = func(i)
  print(res, i) 

# ans needs to be 16 
  