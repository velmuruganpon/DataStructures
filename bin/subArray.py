from common import subArray


# 10 elements - 0.669 seconds
# 20 elements - 2.448 seconds
# 100 elements - 3.875 ms
# without print statements 500 elements - 1101.084 ms 
# without print statements 600 elements - 2752.036 ms

xs = [ i for i in range(0,5) ]

if __name__ == "__main__":
  outXs = subArray(xs)
  print(outXs)
