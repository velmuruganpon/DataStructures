from functools import wraps
from memory_profiler import profile
import time

# wraps is used to get the __doc__ and __name__ from the child functions
# if we do not give wraps, it will display the __doc__ and __name__ of the parent function timer
# profile is for space complexity

# Decorator
def timer(myFunc):
  @wraps(myFunc)
  def timing(*args, **kwargs):
    startTime = time.time()
    retVal = myFunc(*args, **kwargs)
    endTime = time.time()
    print('"{}" took {:.3f} ms to execute\n'.format(myFunc.__name__, (endTime - startTime) * 1000))
    return retVal
  return timing


@profile
@timer
def findListElement(xs: list, finStr : str) :
  findStr =  [ i for i in xs if i == finStr.lower() ] 
  lenFindXs = len(findStr)
  if lenFindXs > 0:
    print( ( "string found!!!" + "\n")  * lenFindXs )


@profile
@timer
def subArray( xs:list):
  """
  time complexity = O( n * n )
  
  """
  resXs =[]
  lenXs = len(xs)
  for strIdx in range(0,lenXs): # O(n)
    for endIdx in range( strIdx , lenXs): # O(n)
      # print("startIndex : {0} \t endIndex : {1} \t element : xs[{0}:{1}]".format(strIdx, endIdx))
      resXs.append(xs[strIdx:endIdx + 1]) # O(1)
    # print("")
  return resXs