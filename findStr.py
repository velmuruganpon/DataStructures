from common import findText, timer

xs = ['vel', 'vel', 'raj']
findStr = 'vel'

@timer
def main(xs:list, findStr : str):
  findText(xs,findStr.lower())
  

if __name__ == "__main__":
  main(xs, findStr)

