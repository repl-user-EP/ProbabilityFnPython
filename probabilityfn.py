def factx(x):
  lis = []
  for i in range(x):
    lis.append(x-i)
  r = 1
  for ii in lis:
    r = r*ii
  return r
  
def ncr(n, r):
  nfact = factx(n)
  nrfact = factx(n-r)
  rfact = factx(r)
  combination = nfact/(nrfact*rfact)
  return combination

def npr(n, r):
  nfact = factx(n)
  nrfact = factx(n-r)
  permutation = nfact/(nrfact)
  return permutation


def pascal(k):
  li = []
  print("0: 1")
  k = k+1
  i = 1
  for i in range(k):
    i = i+1
    for ii in range(i+1):
      li.append(str(int(ncr(i, ii))))
    listed = " ".join(li)
    print(str(i)+": "+listed)
    li = []
