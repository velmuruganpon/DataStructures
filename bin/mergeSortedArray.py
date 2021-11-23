def getLength(xs: list):
  return len(xs)

def swapElements(xs:list, i:int, j:int):
  temp = xs[i]
  xs[i] = xs[j]
  xs[j] = temp


def bubbleSort(xs: list):
  length = getLength(xs)
  for i in range(0,length):
    for j in range(i+1, length):
      if xs[i] > xs[j]:
        swapElements(xs, i, j)
  return xs


def sortChoice(xs: list):
  if getLength(xs) <= 100:
    bubbleSort(xs)
  return xs


def sortArray(*xargs):
  for i in xargs:
    sortChoice(i)


def mergeSortedArray(*xargs):
  xs1 = []
  for i in xargs:
    xs1.extend(i)
  sortArray(xs1)
  return xs1

def compareLengthAndBreak(i, j):
  return True if i == j else False


def mergeSortedTwoArray(xs: list, ys: list):
  zs = []
  sortArray(xs, ys)
  xsLength = getLength(xs)
  ysLength = getLength(ys)
  global i, j
  i = 0
  j = 0
  
  while  i < xsLength or j < ysLength:
    xsEle = xs[i]
    ysEle = ys[j]

    if xsEle < ysEle:
      zs.append(xsEle)
      i = i + 1
      if compareLengthAndBreak(i, xsLength):
        break      
    else:
      zs.append(ysEle)
      j = j + 1
      if compareLengthAndBreak(j, ysLength):
        break
  return zs


xs1 = mergeSortedArray([5,2,3,10], [4,2,1,0,5,21,13], [ 4,9,3,0,6,99])
print(xs1)

zs = mergeSortedTwoArray([10,3,5,2,99,54], [4,89,21,0,79, 54 ])
print(zs)