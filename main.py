import sys

sys.path.append('bin/')
from common import foList

xs = [ 'vel', 'raj' ,' abi']
a = foList(xs)
print(id(a))
