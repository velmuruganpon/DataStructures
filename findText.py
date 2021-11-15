def findText(xs: list, finStr : str) :
  findStr =  [ i for i in xs if i == finStr ] 
  lenFindXs = len(findStr)
  if lenFindXs > 0:
    print( ( "string found!!!" + "\n")  * lenFindXs )