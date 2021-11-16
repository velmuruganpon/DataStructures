from functools import wraps
import time

# wraps is used to get the __doc__ and __name__ from the child functions
# if we do not give wraps, it will display the __doc__ and __name__ of the parent function timer

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


def findText(xs: list, finStr : str) :
  findStr =  [ i for i in xs if i == finStr.lower() ] 
  lenFindXs = len(findStr)
  if lenFindXs > 0:
    print( ( "string found!!!" + "\n")  * lenFindXs )